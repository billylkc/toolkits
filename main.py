import grpc
import logging

from concurrent import futures
from protos import text_pb2
from protos import text_pb2_grpc
from src.model.text import Text


def serve():
    port = 50052
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    text_pb2_grpc.add_TextServicer_to_server(Text(), server)

    server.add_insecure_port('[::]:{}'.format(port))
    print("Hosting server on port {}".format(port))

    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()
