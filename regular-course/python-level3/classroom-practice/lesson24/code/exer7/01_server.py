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
        self.connSockets = {}
        self.avatars = {}

    def sendMsg(self, connSocket, msg, code):
        msg = json.dumps({'code': code, 'msg': msg.__dict__})
        connSocket.send(msg.encode())

    def recvMsg(self, connSocket):
        try:
            req = connSocket.recv(1024).decode()
            req = json.loads(req)
            return req
        except Exception as e:
            print(e)

    def run(self):
        while True:
            print('等待连接...')
            connSocket, clientAddr = self.socket.accept()
            t = threading.Thread(target=self.handle, args=[connSocket])
            t.start()

    def handle(self, connSocket):
        while True:
            req = self.recvMsg(connSocket)
            print('接收到的消息：', req)
            if not req:
                break
            if req['cmd'] == 'login':
                self.login(connSocket, req)
        self.quit(connSocket)

    def quit(self, connSocket):
        connSocket.close()
        for name, cSocket in self.connSockets.items():
            if connSocket == cSocket:
                del self.connSockets[name]
                del self.avatars[name]
                break

    def login(self, connSocket, req):
        sender = req['sender']
        if sender in self.connSockets:
            msg = Message('login', '该账号已登录', '服务器')
            self.sendMsg(connSocket, msg, 401)
            return
        # 1. 将登录消息字典req转换成登录消息对象msg

        for cSocket in self.connSockets.values():
            # 2. 将req修改为msg
            self.sendMsg(cSocket, req, 200)
        self.connSockets[sender] = connSocket
        self.avatars[sender] = req['content']
        print(self.connSockets)
        print(self.avatars)
        msg = Message(req['cmd'], self.avatars, '服务器')
        self.sendMsg(connSocket, msg, 200)


if __name__ == '__main__':
    server = Server('0.0.0.0', 10061)
    server.run()
