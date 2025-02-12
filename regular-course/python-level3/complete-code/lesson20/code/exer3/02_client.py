from socket import *


class Client:
    def __init__(self, ip, port):
        self.socket = socket()
        self.socket.connect((ip, port))

    def run(self):
        # 1. 添加无限循环
        while True:
            # 2. 获取输入消息内容
            content = input("请输入消息内容：")
            # 3. 如果内容为空，就跳过当前循环并重新输入
            if not content:
                continue
            # 4. 发送输入的内容，并给下面3行代码添加一个缩进
            self.socket.send(content.encode())
            res = self.socket.recv(1024).decode()
            print('客户端收到的消息：', res)
        self.socket.close()


client = Client('l345.61it.cn', 10021)
client.run()
