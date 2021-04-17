# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from protos import text_pb2 as protos_dot_text__pb2


class TextStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.ExtractKeywords = channel.unary_unary(
                '/pbuf.Text/ExtractKeywords',
                request_serializer=protos_dot_text__pb2.KeywordRequest.SerializeToString,
                response_deserializer=protos_dot_text__pb2.KeywordResponse.FromString,
                )
        self.ExtractSummary = channel.unary_unary(
                '/pbuf.Text/ExtractSummary',
                request_serializer=protos_dot_text__pb2.SummaryRequest.SerializeToString,
                response_deserializer=protos_dot_text__pb2.SummaryResponse.FromString,
                )
        self.ExtractTfIdf = channel.unary_unary(
                '/pbuf.Text/ExtractTfIdf',
                request_serializer=protos_dot_text__pb2.TFRequest.SerializeToString,
                response_deserializer=protos_dot_text__pb2.TFResponse.FromString,
                )


class TextServicer(object):
    """Missing associated documentation comment in .proto file."""

    def ExtractKeywords(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ExtractSummary(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ExtractTfIdf(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_TextServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'ExtractKeywords': grpc.unary_unary_rpc_method_handler(
                    servicer.ExtractKeywords,
                    request_deserializer=protos_dot_text__pb2.KeywordRequest.FromString,
                    response_serializer=protos_dot_text__pb2.KeywordResponse.SerializeToString,
            ),
            'ExtractSummary': grpc.unary_unary_rpc_method_handler(
                    servicer.ExtractSummary,
                    request_deserializer=protos_dot_text__pb2.SummaryRequest.FromString,
                    response_serializer=protos_dot_text__pb2.SummaryResponse.SerializeToString,
            ),
            'ExtractTfIdf': grpc.unary_unary_rpc_method_handler(
                    servicer.ExtractTfIdf,
                    request_deserializer=protos_dot_text__pb2.TFRequest.FromString,
                    response_serializer=protos_dot_text__pb2.TFResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'pbuf.Text', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Text(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def ExtractKeywords(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/pbuf.Text/ExtractKeywords',
            protos_dot_text__pb2.KeywordRequest.SerializeToString,
            protos_dot_text__pb2.KeywordResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ExtractSummary(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/pbuf.Text/ExtractSummary',
            protos_dot_text__pb2.SummaryRequest.SerializeToString,
            protos_dot_text__pb2.SummaryResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ExtractTfIdf(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/pbuf.Text/ExtractTfIdf',
            protos_dot_text__pb2.TFRequest.SerializeToString,
            protos_dot_text__pb2.TFResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)