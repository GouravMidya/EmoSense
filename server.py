import grpc
from concurrent import futures
import messaging_pb2
import messaging_pb2_grpc
import time
import google.protobuf.empty_pb2


class ChatServiceServicer(messaging_pb2_grpc.ChatServiceServicer):

    def __init__(self):
        self.messages = []

    def SendMessage(self, request, context):
        self.messages.append(request)
        return google.protobuf.empty_pb2.Empty()

    def ReceiveMessage(self, request, context):
        for message in self.messages:
            yield message

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    messaging_pb2_grpc.add_ChatServiceServicer_to_server(ChatServiceServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print('Server started. Listening on port 50051.')
    server.wait_for_termination()

if __name__ == '__main__':
    serve()