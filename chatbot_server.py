import grpc
from concurrent import futures
import replicate
from dotenv import load_dotenv
import os
import chatbot_pb2
import chatbot_pb2_grpc

load_dotenv()

REPLICATE_API_TOKEN = os.getenv('REPLICATE_API_TOKEN')

class ChatbotService(chatbot_pb2_grpc.ChatbotServicer):
    def Chat(self, request_iterator, context):
        history = []
        for request in request_iterator:
            user_input = request.message
            system_message = "You are a helpful assistant."
            prompt = f"{system_message}\n\n{user_input}"
            
            buffer = ""
            in_think = False
            think_content = []
            final_answer = []
            
            # Start streaming from Replicate
            stream = replicate.stream(
                "deepseek-ai/deepseek-r1",
                input={
                    "top_p": 1,
                    "prompt": prompt,
                    "max_tokens": 20480,
                    "temperature": 0.7,
                    "presence_penalty": 0,
                    "frequency_penalty": 0,
                },
                
            )

            for event in stream:
                buffer += str(event)
                
                while True:
                    if not in_think and '<think>' in buffer:
                        parts = buffer.split('<think>', 1)
                        before_think = parts[0]
                        buffer = parts[1] if len(parts) > 1 else ""
                        
                        if before_think:
                            final_answer.append(before_think)
                            yield chatbot_pb2.ChatResponse(message=before_think, is_thinking=False)
                        
                        in_think = True
                    
                    elif in_think and '</think>' in buffer:
                        parts = buffer.split('</think>', 1)
                        think_part = parts[0]
                        buffer = parts[1] if len(parts) > 1 else ""
                        
                        think_content.append(think_part)
                        yield chatbot_pb2.ChatResponse(thought_process=think_part, is_thinking=True)
                        
                        in_think = False
                    
                    else:
                        break
                
                if not in_think and buffer:
                    final_answer.append(buffer)
                    yield chatbot_pb2.ChatResponse(message=buffer, is_thinking=False)
                    buffer = ""
            
            if buffer:
                if in_think:
                    think_content.append(buffer)
                    yield chatbot_pb2.ChatResponse(thought_process=buffer, is_thinking=True)
                else:
                    final_answer.append(buffer)
                    yield chatbot_pb2.ChatResponse(message=buffer, is_thinking=False)
            
            history.append((user_input, "".join(final_answer)))

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    chatbot_pb2_grpc.add_ChatbotServicer_to_server(ChatbotService(), server)
    server.add_insecure_port('[::]:50051')
    print("Starting server on port 50051...")
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()