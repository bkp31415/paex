import grpc
import json
from concurrent import futures

# import the generated classes
import rule_pb2
import rule_pb2_grpc

class CodeRun:
    def __init__(self, block):
        if block['code'] == 'avg':
            matrix = block['data']
            return avg(matrix)


# create a class to define the pods functions
class CodeServicer(rule_pb2_grpc.CodeServicer):

    def exec(self, request, context):
        request = json.loads(request.block)
        response = rule_pb2.Block()
        response.block = CodeRun(request).result()
        return response

class Executor:
    """
    The Executor performs atomic computations on various nodes in a cluster with data 
    recieved from the service application.
    """
	def __init__(self, url):
        print('Starting server. Listening on port:', url)
        # create a gRPC server
        self.server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
        rule_pb2_grpc.add_CodeServicer_to_server(CodeServicer(), self.server)
        self.server.add_insecure_port(url)
        self.server.start()
