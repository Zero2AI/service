# R1Storm Chatbot gRPC Implementation

This project implements a chatbot using gRPC for client-server communication, based on the DeepSeek-R1 model.

## Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

## Setup

1. Clone the repository:
   ```
   git clone https://github.com/your-repo/r1storm.git
   cd r1storm
   ```

2. Create a virtual environment (optional but recommended):
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. pip install -r requirements.txt
     ```

4. Generate the gRPC code from the protobuf definition:
   ```
   python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. chatbot.proto
   ```

5. Set up your Replicate API token:
   Create a `.env` file in the project root and add your Replicate API token:
   ```
   REPLICATE_API_TOKEN=your_api_token_here
   ```

## Running the Application

1. Start the server:
   ```
   python server.py
   ```

2. In a new terminal, run the client:
   ```
   python client.py
   ```

3. Start chatting with the bot through the client interface.

4. To exit the chat, type 'exit' or 'quit'.

## Project Structure

- `chatbot.proto`: Protocol Buffers definition file
- `server.py`: gRPC server implementation
- `client.py`: gRPC client implementation
- `chatbot_pb2.py` and `chatbot_pb2_grpc.py`: Generated Python files from the proto file (these will be created when you run the gRPC tools command)
- `server_requirements.txt`: Requirements file for the server
- `client_requirements.txt`: Requirements file for the client

## Notes

- This implementation uses streaming gRPC for real-time communication between the client and server.
- The server uses the Replicate API to interact with the DeepSeek-R1 model.
- Make sure to keep your Replicate API token confidential and do not share it publicly.
- The server and client have separate requirements files. Make sure to install the appropriate requirements depending on which component you're running.

## Troubleshooting

If you encounter any issues, please ensure that:
- All required packages are installed using the appropriate requirements file
- The gRPC code has been generated correctly
- The Replicate API token is set correctly in the .env file
- The server is running before starting the client

For any other problems, please open an issue in the repository.