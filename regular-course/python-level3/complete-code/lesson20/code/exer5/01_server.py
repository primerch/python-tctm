import socket


class Server:
    def __init__(self, ip, port):
        self.socket = socket.socket()
        self.socket.bind((ip, port))
        self.socket.listen()

    def run(self):
        print('等待链接。。。')
        connSocket, addr = self.socket.accept()
        while True:
            req = connSocket.recv(1024).decode()
            # 1.如果收到的消息为空，则结束循环，关闭套接字
            if not req:
                break
            print('服务端收到的消息：', req)
            connSocket.send('你好，我是服务端。我收到你的消息了！'.encode())
        connSocket.close()
        self.socket.close()


server = Server('0.0.0.0', 10021)
server.run()
