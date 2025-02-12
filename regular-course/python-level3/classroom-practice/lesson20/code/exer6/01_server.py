import socket


class Server:
    def __init__(self, ip, port):
        self.socket = socket.socket()
        self.socket.bind((ip, port))
        self.socket.listen()

    def run(self):
        # 1. 添加无限循环

        # 2. 给下面9行代码添加一个缩进
        print('等待链接。。。')
        connSocket, addr = self.socket.accept()
        while True:
            req = connSocket.recv(1024).decode()
            if not req:
                break
            print('服务端收到的消息：', req)
            connSocket.send('你好，我是服务端。我收到你的消息了！'.encode())
        connSocket.close()
        self.socket.close()


server = Server('0.0.0.0', 10021)
server.run()
