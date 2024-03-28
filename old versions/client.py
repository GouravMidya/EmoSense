import grpc
import messaging_pb2_grpc
import messaging_pb2
import google.protobuf.empty_pb2

class ChatClient:

    def __init__(self, host, port):
        self.channel = grpc.insecure_channel(f'{host}:{port}')
        self.stub = messaging_pb2_grpc.ChatServiceStub(self.channel)

    def send_message(self, username, message):
        chat_message = messaging_pb2.ChatMessage(username=username, message=message)
        response = self.stub.SendMessage(chat_message)
        print(f'Message sent: {username}: {message}')

    def receive_messages(self):
        for chat_message in self.stub.ReceiveMessage(google.protobuf.empty_pb2.Empty()):
            print(f'Message received: {chat_message.username}: {chat_message.message}')

if __name__ == '__main__':
    client = ChatClient('localhost', 50051)
    client.send_message('Alice', 'Hello Prathamesh')
    #client.receive_messages()
