"""
第一段提示词：

这是我的服务端代码：
class Server:
    def __init__(self, ip, port):
        ...
    def sendMsg(self,connSocket,code, msg):
        msg = json.dumps({'code':code,'msg':msg.__dict__})
        connSocket.send(msg.encode())
    def recvMsg(self,connSocket):
        res = connSocket.recv(1024).decode()
        res = json.loads(res)
        return res
    def run(self):
        while True:
            print('等待链接。。。')
            connSocket, cAddr = self.socket.accept()
            t = threading.Thread(target=self.handle, args=[connSocket])
            t.start()
    def handle(self, connSocket):
        while True:
            # 3. 修改下列代码，调用recvMsg接收请求消息
            req = self.recvMsg(connSocket)
            print('接收到的消息：', req)
            if not req:
                break
            msg = Message(req['cmd'], '你好，我收到你的消息了！', '服务器')
            self.sendMsg(connSocket,200,msg)
        connSocket.close()
当我的程序客户端退出时，服务端报这个错误:
json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)
请问原因是什么如何解决。

"""
