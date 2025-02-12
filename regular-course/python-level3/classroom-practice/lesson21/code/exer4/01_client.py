# 定义recvMsg方法：http://l345.61it.cn:8080/l3/day21/practice/p1/index.html
from socket import *
import json


class Message:
    def __init__(self, cmd, content, sender, to=None):
        self.cmd = cmd
        self.content = content
        self.sender = sender
        self.to = to


class Client:
    def __init__(self, ip, port):
        self.socket = socket()
        self.socket.connect((ip, port))

    def sendMsg(self, msg):
        msg = json.dumps(msg.__dict__)
        self.socket.send(msg.encode())

    # 1. 定义recvMsg方法

    def run(self):
        while True:
            content = input('请输入用户名：')
            if not content:
                continue
            msg = Message('login', content, content)
            self.sendMsg(msg)
            # 2.把下行代码修改为调用recvMsg方法接收响应
            res = self.socket.recv(1024).decode()
            # 3. 获取响应状态码和消息，并输出查看

            print('客户端收到的消息是：', res)
        self.socket.close()


client = Client('l345.61it.cn', 10031)
client.run()
