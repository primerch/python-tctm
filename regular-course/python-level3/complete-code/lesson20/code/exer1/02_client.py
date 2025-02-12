from socket import *


# 1. 使用面向对象编程的方式定义客户端类Client
class Client:
    def __init__(self, ip, port):
        self.socket = socket()
        self.socket.connect((ip, port))

    def run(self):
        self.socket.send('童童，你好！我是小派。'.encode())
        res = self.socket.recv(1024).decode()
        print('客户端收到的消息：', res)
        self.socket.close()


# 2. 创建客户端对象client，传入域名:l345.61it.cn和端口号：10021
client = Client('l345.61it.cn', 10021)
# 3. 调用run()方法
client.run()
