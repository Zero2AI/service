import grpc
import appstorm_pb2
import appstorm_pb2_grpc

def run():
    channel = grpc.insecure_channel('localhost:50055')
    stub = appstorm_pb2_grpc.AppStormServiceStub(channel)

    # Test GenerateApp
    response = stub.GenerateApp(appstorm_pb2.GenerateAppRequest(
        email="rockon_deep45@yahoo.com",
        password="123456",
        prompt="Build me a chat app"
    ))
    print("GenerateApp response:", response)

    # Test PublishNFT
    # nft_response = stub.PublishNFT(appstorm_pb2.PublishNFTRequest())
    # print("PublishNFT response:", nft_response)

if __name__ == '__main__':
    run()
