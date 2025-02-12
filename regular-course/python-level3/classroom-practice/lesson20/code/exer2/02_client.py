from socket import *


class Client:
    def __init__(self, ip, port):
        self.socket = socket()
        self.socket.connect((ip, port))

    def run(self):
        self.socket.send("童童，你好！我是小派。".encode())
        res = self.socket.recv(1024).decode()
        print('客户端收到的消息：', res)
        self.socket.close()


client = Client('localhost', 10021)
client.run()
