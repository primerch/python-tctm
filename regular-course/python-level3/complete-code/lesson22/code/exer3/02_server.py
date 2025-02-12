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
        # 1. 定义连接socket字典和用户头像字典
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
            # 2. 获取登录者用户名
            sender = req['sender']
            # 3. 把连接socket存到连接socket字典，把头像存到用户头像字典
            self.connSockets[sender] = connSocket
            self.avatars[sender] = req['content']
            # 4. 输出连接socket字典和用户头像字典
            print(self.connSockets)
            print(self.avatars)
            msg = Message(req['cmd'], req['sender'] + '登录成功', '服务器')
            self.sendMsg(connSocket, msg, 200)
        connSocket.close()


if __name__ == '__main__':
    server = Server('0.0.0.0', 10041)
    server.run()
