from socket import *


class Client:
    def __init__(self, ip, port):
        self.socket = socket()
        self.socket.connect((ip, port))

    def run(self):
        while True:
            content = input('请输入发送的内容：')
            if not content:
                continue
            self.socket.send(content.encode())
            res = self.socket.recv(1024).decode()
            print('客户端收到的消息：', res)
        self.socket.close()


client = Client('localhost', 10021)
client.run()
