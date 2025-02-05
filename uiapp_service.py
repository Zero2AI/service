import grpc
from concurrent import futures
import uiapp_pb2
import uiapp_pb2_grpc
from gradio_client import Client

# Define the Gradio Client pointing to your Gradio app
gradio_client = Client("http://98.80.124.52:9001/")

class UIAppService(uiapp_pb2_grpc.UIAppServicer):
    def Predict(self, request, context):
        """
        Calls the remote Gradio server with the user's input.
        """
        result = gradio_client.predict(
            history=[],
            user_input=request.user_input,
            api_name="/process_message"
        )
        return uiapp_pb2.PredictResponse(result=result)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    uiapp_pb2_grpc.add_UIAppServicer_to_server(UIAppService(), server)
    server.add_insecure_port("[::]:50051")  # Runs on port 50051
    server.start()
    print("Server started at port 50051")
    server.wait_for_termination()

if __name__ == "__main__":
    serve()
