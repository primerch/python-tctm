from socket import *


# 1. 使用面向对象编程的方式定义服务端类Server
class Server:
    def __init__(self, ip, port):
        self.socket = socket()
        self.socket.bind((ip, port))
        self.socket.listen()

    def run(self):
        print('等待客户端连接...')
        connSocket, addr = self.socket.accept()
        req = connSocket.recv(1024).decode()
        print('接收到客户端的消息：', req)
        connSocket.send('你好，我是服务端。我收到你的消息了！'.encode())
        connSocket.close()
        self.socket.close()


# 2. 创建服务端对象server，传入ip：0.0.0.0和端口号：10021
server = Server('0.0.0.0', 10021)
# 3. 调用run方法，启动服务端
server.run()
