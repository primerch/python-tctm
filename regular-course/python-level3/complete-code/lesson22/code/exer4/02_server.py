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
        req = connSocket.recv(1024).decode()
        if not req:
            return
        req = json.loads(req)
        return req

    def run(self):
        while True:
            print('等待连接...')
            connSocket, addr = self.socket.accept()
            t = threading.Thread(target=self.handle, args=[connSocket])
            t.start()

    def handle(self, connSocket):
        while True:
            req = self.recvMsg(connSocket)
            print('接收到的消息：', req)
            if not req:
                break
            # 2. 判断消息命令是否为登录命令，如果是，调用login方法
            if req['cmd'] == 'login':
                self.login(connSocket, req)

        connSocket.close()

    # 1. 定义login方法，处理客户端登录请求
    def login(self, connSocket, req):
        sender = req['sender']
        self.connSockets[sender] = connSocket
        self.avatars[sender] = req['content']
        print(self.connSockets)
        print(self.avatars)
        msg = Message(req['cmd'], req['sender'] + '登录成功', '服务器')
        self.sendMsg(connSocket, msg, 200)


if __name__ == '__main__':
    server = Server('0.0.0.0', 10041)
    server.run()
