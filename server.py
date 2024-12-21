import socket

HOST = '127.0.0.1'
PORT = 65432

clients = {}

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        while True:
            conn, addr = s.accept()
            print(f"Connected by: {addr}")
            with conn:
                while True:
                    data = conn.recv(1024)
                    if not data:
                        break
                    print(data.decode())

if __name__ == '__main__':
    main()