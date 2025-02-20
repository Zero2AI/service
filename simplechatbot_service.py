from concurrent import futures
import logging
import grpc
import simplechatbot_pb2
import simplechatbot_pb2_grpc
from gradio_client import Client


class simplechatbot(simplechatbot_pb2_grpc.simplechatbotServicer):

    def predict(self, request, context):
        try:
            # Initialize the Gradio client
            space_client = Client(
                #src='https://zero2ai-simplechat.hf.space/'
                src='http://52.204.24.135:9128'
            )

            # Call the predict method
            output1 = space_client.predict(
                request.input1, api_name='/predict'
            )

            # Return the response
            return simplechatbot_pb2.predict_resp(output1=output1)

        except Exception as e:
            # Handle all exceptions
            context.set_code(grpc.StatusCode.INTERNAL)
            context.set_details(f"Error calling Gradio API: {str(e)}")
            return simplechatbot_pb2.predict_resp(output1="")


# Main server body
def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=4), 
                         options=[('grpc.max_message_length', 64*1024*1024),
                                  ('grpc.max_send_message_length', 64*1024*1024),
                                  ('grpc.max_receive_message_length', 64*1024*1024)])
    simplechatbot_pb2_grpc.add_simplechatbotServicer_to_server(simplechatbot(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    serve()