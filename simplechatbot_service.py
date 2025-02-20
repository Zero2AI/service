from concurrent import futures
import logging
import grpc
import simplechatbot_pb2
import simplechatbot_pb2_grpc
import httpx
from fastapi import FastAPI, HTTPException

app = FastAPI()

class simplechatbot(simplechatbot_pb2_grpc.simplechatbotServicer):

    async def predict(self, request, context):
        try:
            async with httpx.AsyncClient() as client:
                response = await client.post(
                    "http://52.204.24.135:9128/predict",
                    json={"input1": request.input1}
                )
                response.raise_for_status()
                result = response.json()

            return simplechatbot_pb2.predict_resp(output1=result["output1"])

        except httpx.HTTPStatusError as e:
            context.set_code(grpc.StatusCode.INTERNAL)
            context.set_details(f"HTTP error: {e.response.status_code} - {e.response.text}")
            return simplechatbot_pb2.predict_resp(output1="")
        except Exception as e:
            context.set_code(grpc.StatusCode.INTERNAL)
            context.set_details(f"Error calling API: {str(e)}")
            return simplechatbot_pb2.predict_resp(output1="")

# ... existing code ...

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    serve()