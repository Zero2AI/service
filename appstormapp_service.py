from concurrent import futures
import grpc
import time
import appstormapp_pb2
import appstormapp_pb2_grpc

# Mock functions for apiService logic
def init_session():
    return "mock_token", "mock_session_id"

def login(email, password, token, sessionId):
    return "login_token", "login_session", 123  # userId

def create_app(userId, token, sessionId, prompt):
    return "temp_app_id", "app_session_id"

def poll_app_status(appSessionId, appId, token, sessionId):
    # Simulate app ready state
    finalAppId = "final_app_id_456"
    return finalAppId

def get_share_link(finalAppId, token, sessionId):
    #return f"https://devchat.appstorm.ai/apps/{finalAppId}"
    return f"https://appstormapi4snet.zero2ai.net/generate-app"

# Service class
class AppStormServiceServicer(appstormapp_pb2_grpc.AppStormServiceServicer):
    
    def GenerateApp(self, request, context):
        try:
            token, sessionId = init_session()
            loginToken, loginSession, userId = login(request.email, request.password, token, sessionId)
            appId, appSessionId = create_app(userId, loginToken, loginSession, request.prompt)
            finalAppId = poll_app_status(appSessionId, appId, loginToken, loginSession)
            url = get_share_link(finalAppId, loginToken, loginSession)
            return appstormapp_pb2.GenerateAppResponse(success=True, url=url)
        except Exception as e:
            return appstormapp_pb2.GenerateAppResponse(success=False, error=str(e))
    
    def PublishNFT(self, request, context):
        return appstormapp_pb2.PublishNFTResponse(
            success=True,
            message="NFT publishing endpoint placeholder",
            data=""
        )

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

if __name__ == '__main__':
    serve()
