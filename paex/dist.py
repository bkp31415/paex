import grpc

# import the generated classes
import rule_pb2
import rule_pb2_grpc

class Distributor:
    """ 
    The Distributor class provides necessary logic to distribute code and associated data 
    onto the various nodes in a cluster. 

    blocks - array of data values and their associated code
    lock - a variable that counts up to the max number of pods available

    __init__() - generates the blocks and makes a call for execution on cluster
    exec() - passes the data and associate code value to the executors
    """
	def __init__(self, data, nodes = ['localhost:50051']):
        self.nodes = nodes

        for i in range(1, len(nodes)+1):
            self.channels[i] = grpc.insecure_channel(self.nodes[i])
            self.stubs[i] = rule_pb2_grpc.CodeStub(channel)

        self.blocks = []
        for block in blocks:
            self.exec(block)
            while self.lock >= len(nodes):
                pass

        
    def exec(self, block):
        """
        Create a gRPC connection to one of the pods executing code and pass the data and 
        code to execute. Code is a key that corresponds to the actual process that needs
        to be executed on the pods parallelly.

        TODO: needs to be async
        """
        self.lock += 1
        for stub in self.stubs:
            rule_pb2.Block(block)

        
