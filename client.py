import grpc
import chatbot_pb2
import chatbot_pb2_grpc

def run():
    # Increase timeout to 30 seconds
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
        # Add timeout to the gRPC call
        responses = stub.Chat(generate_messages(), timeout=30)
        for response in responses:
            if response.is_thinking:
                print("Assistant is thinking:")
                print(response.thought_process)
            else:
                print("Assistant:", response.message)
    except grpc.RpcError as e:
        if e.code() == grpc.StatusCode.DEADLINE_EXCEEDED:
            print("Error: The request timed out. The server took too long to respond.")
        elif e.code() == grpc.StatusCode.UNAVAILABLE:
            print("Error: The server is currently unavailable. Please try again later.")
        else:
            print(f"An error occurred: {e.code()}: {e.details()}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        print("\nChat session ended.")
        channel.close()

if __name__ == '__main__':
    run()