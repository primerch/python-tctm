import json
import socket
import threading


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

    def sendMsg(self, connSocket, code, msg):
        msg = json.dumps({'code': code, 'msg': msg.__dict__})
        connSocket.send(msg.encode())

    def recvMsg(self, connSocket):
        req = connSocket.recv(1024).decode()
        # 1. 如果收到的消息是为空，则返回None

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
            req = self.recvMsg(connSocket)
            print('服务端收到的消息：', req)
            if not req:
                break
            msg = Message(req['cmd'], req['sender'] + '登录成功', '服务器')
            self.sendMsg(connSocket, 200, msg)
        connSocket.close()


if __name__ == '__main__':
    server = Server('0.0.0.0', 10031)
    server.run()
