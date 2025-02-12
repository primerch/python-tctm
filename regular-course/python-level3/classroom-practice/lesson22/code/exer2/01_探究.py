'''

这是我写好的客户端连接服务端，并发送接收消息的类，这个类放在client.py中：
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

我在刚刚的登录窗口中如何才能使用client.py文件中这个类和类中的方法？
在登录窗口的代码中，哪个位置用Client类创建client对象，建立与服务端连接？
又在哪个位置调用方法发送登录消息，接收结果？

'''
