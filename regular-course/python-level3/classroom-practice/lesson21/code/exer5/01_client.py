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
        res = self.socket.recv(1024).decode()
        res = json.loads(res)
        return res

    def run(self):
        while True:
            content = input('请输入用户名：')
            if not content:
                continue
            msg = Message('login', content, content)
            self.sendMsg(msg)
            res = self.recvMsg()
            code = res['code']
            msg = res['msg']
            print('状态码', code, '消息：', msg)
        self.socket.close()


client = Client('localhost', 10031)
client.run()
