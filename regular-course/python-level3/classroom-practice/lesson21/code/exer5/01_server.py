import json
import socket
import threading


# 预留的message类
class Message:
    def __init__(self, cmd, content, sender, to=None):
        self.cmd = cmd
        self.content = content
        self.sender = sender
        self.to = to


class Server:
    def __init__(self, ip, port):
        self.socket = socket.socket()
        self.socket.bind((ip, port))
        self.socket.listen()

    # 1. 对sendMsg和recvMsg方法进行特定的修改
    def sendMsg(self, msg):
        msg = json.dumps(msg.__dict__)
        self.socket.send(msg.encode())

    def recvMsg(self):
        req = self.socket.recv(1024).decode()
        req = json.loads(req)
        return req

    def run(self):
        while True:
            print('等待链接。。。')
            connSocket, cAddr = self.socket.accept()
            t = threading.Thread(target=self.handle, args=[connSocket])
            t.start()

    def handle(self, connSocket):
        while True:
            # 2. 修改下行代码，调用recvMsg接收请求消息
            req = connSocket.recv(1024).decode()
            print('服务端收到的消息：', req)
            if not req:
                break
            # 3. 修改下行代码，定义回复消息对象，调用sendMsg方法发送消息
            connSocket.send('你好，我收到你的消息了！'.encode())
        connSocket.close()


if __name__ == '__main__':
    server = Server('0.0.0.0', 10031)
    server.run()
