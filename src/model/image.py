from protos import image_pb2
from protos import image_pb2_grpc
import pandas as pd


class Image(image_pb2_grpc.ImageServicer):
    def TextImage(self, request, context):
        return
