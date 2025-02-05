import grpc
import uiapp_pb2
import uiapp_pb2_grpc

def run():
    channel = grpc.insecure_channel("localhost:50051")
    stub = uiapp_pb2_grpc.UIAppStub(channel)

    user_input = "Hello!!"
    response = stub.Predict(uiapp_pb2.PredictRequest(user_input=user_input))
    print(f"Server response: {response.result}")

if __name__ == "__main__":
    run()
