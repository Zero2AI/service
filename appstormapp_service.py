from concurrent import futures
import grpc
import time
import requests
import appstormapp_pb2
import appstormapp_pb2_grpc

BASE_URL = "https://appstormapi4snet.zero2ai.net"

class AppStormServiceServicer(appstormapp_pb2_grpc.AppStormServiceServicer):
    
    def GenerateApp(self, request, context):
        try:
            payload = {
                "email": request.email,
                "password": request.password,
                "prompt": request.prompt
            }
            response = requests.post(f"{BASE_URL}/generate-app", json=payload)
            data = response.json()

            if data.get("success"):
                return appstormapp_pb2.GenerateAppResponse(success=True, url=data.get("url", ""))
            else:
                return appstormapp_pb2.GenerateAppResponse(success=False, error=data.get("error", "Unknown error"))
        except Exception as e:
            return appstormapp_pb2.GenerateAppResponse(success=False, error=str(e))

    def PublishNFT(self, request, context):
        try:
            response = requests.post(f"{BASE_URL}/publishNFT", json={})
            data = response.json()
            return appstormapp_pb2.PublishNFTResponse(
                success=data.get("success", False),
                message=data.get("message", ""),
                data=data.get("data", "")
            )
        except Exception as e:
            return appstormapp_pb2.PublishNFTResponse(success=False, message="", data=str(e))

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    appstormapp_pb2_grpc.add_AppStormServiceServicer_to_server(AppStormServiceServicer(), server)
    server.add_insecure_port('[::]:50055')
    print("gRPC server running on port 50055")
    server.start()
    try:
        while True:
            time.sleep(86400)
    except KeyboardInterrupt:
        server.stop(0)

if __name__ == "__main__":
    serve()
