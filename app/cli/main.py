import grpc
import helloworld_pb2

with open('roots.pem', 'rb') as f:
        creds = grpc.ssl_channel_credentials(f.read())
        channel = grpc.secure_channel('myservice.example.com:443', creds)
        stub = helloworld_pb2.GreeterStub(channel)
