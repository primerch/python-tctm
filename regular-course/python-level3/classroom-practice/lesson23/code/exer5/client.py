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

    def recvMsg(self):
        # 1. 使用try-except捕获接收消息时的异常，并输出异常。

        # 2. 修改接收数据的最大字节数为1024*1000
        res = self.socket.recv(1024).decode()
        print(res)
        res = json.loads(res)
        return res
