import logging
import grpc
import sys
import z2ai_text_2_image_pb2
import z2ai_text_2_image_pb2_grpc


def run():
    with grpc.insecure_channel('localhost:50051', options=[
        ('grpc.max_send_message_length', 64*1024*1024),
        ('grpc.max_receive_message_length', 64*1024*1024),
    ]) as channel:
        stub = z2ai_text_2_image_pb2_grpc.z2ai_text_2_imageStub(channel)

        input1 = sys.argv[1]

        response = stub.predict(
            z2ai_text_2_image_pb2.predict_req(input1=input1))

        print(response.fileName1)

        with open(response.fileName1, mode='wb') as f:
            f.write(response.fileBytes1)


if __name__ == '__main__':
    logging.basicConfig()
    run()
