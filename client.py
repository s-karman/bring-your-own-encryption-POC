import json
import socket

HOST = '127.0.0.1'
PORT = 65432

username = ''

class Message:
    def __init__(self, data, port, server_code):
        self.port = port
        self.server_code = server_code
        self.data = data
        self.data = username

    def to_json(self):
        return json.dumps(self)


def create_message():
    pass


def init_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        message = input("Message to send: ")
        s.sendall(message.encode())
        #data = s.recv(1024)
        print("SENT")
    #print(data.decode())


if __name__ == '__main__':
    username = input("USERNAME: ")
    init_server()
