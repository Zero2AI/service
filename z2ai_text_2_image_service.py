
# Server Imports
from concurrent import futures
import logging
import os
import grpc
import z2ai_text_2_image_pb2
import z2ai_text_2_image_pb2_grpc
from gradio_client import Client


class z2ai_text_2_image(z2ai_text_2_image_pb2_grpc.z2ai_text_2_imageServicer):

    def predict(self, request, context):
        space_client = Client(src='whiter4ven/text-to-image')

        fileName1 = space_client.predict(request.input1, api_name='/predict')
        with open(fileName1, mode='rb') as f:
            blob_data_1 = bytes(f.read())

        return z2ai_text_2_image_pb2.predict_resp(fileName1=fileName1, fileBytes1=blob_data_1)


# main server body
def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=4), options=[('grpc.max_message_length', 64*1024*1024),
                                                                             ('grpc.max_send_message_length', 64*1024*1024),
                                                                             ('grpc.max_receive_message_length', 64*1024*1024)])
    z2ai_text_2_image_pb2_grpc.add_z2ai_text_2_imageServicer_to_server(
        z2ai_text_2_image(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()
