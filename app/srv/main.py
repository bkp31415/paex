import grpc
import helloworld_pb2
from concurrent import futures

server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
with open('key.pem', 'rb') as f:
        private_key = f.read()
        with open('chain.pem', 'rb') as f:
                certificate_chain = f.read()
                server_credentials = grpc.ssl_server_credentials( ( (private_key, certificate_chain), ) )
                # Adding GreeterServicer to server omitted
                server.add_secure_port('myservice.example.com:443', server_credentials)
                server.start()
                # Server sleep omitted
