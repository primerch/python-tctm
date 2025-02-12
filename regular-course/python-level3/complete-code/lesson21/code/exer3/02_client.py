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

    # 1. 定义sendMsg方法，将消息对象转换为json字符串发送
    def sendMsg(self, msg):
        msg = json.dumps(msg.__dict__)
        self.socket.send(msg.encode())

    def run(self):
        while True:
            content = input('请输入用户名：')
            if not content:
                continue
            # 2. 创建登录时消息对象
            msg = Message('login', content, content)
            # 3. 把下行代码修改为调用sendMsg发送消息
            self.sendMsg(msg)
            res = self.socket.recv(1024).decode()
            print('客户端收到的消息是：', res)
        self.socket.close()


client = Client('l345.61it.cn', 10031)
client.run()
