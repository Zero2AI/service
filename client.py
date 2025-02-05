import grpc
import chatbot_pb2
import chatbot_pb2_grpc

def run():
    channel = grpc.insecure_channel('localhost:50051')
    stub = chatbot_pb2_grpc.ChatbotStub(channel)

    def get_user_input():
        return input("You: ")

    def generate_messages():
        while True:
            user_input = get_user_input()
            if user_input.lower() in ['exit', 'quit']:
                break
            yield chatbot_pb2.ChatRequest(message=user_input)

    try:
        responses = stub.Chat(generate_messages())
        for response in responses:
            if response.is_thinking:
                print("Assistant is thinking:")
                print(response.thought_process)
            else:
                print("Assistant:", response.message, end='')
        print("\nChat session ended.")
    except grpc.RpcError as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    run()