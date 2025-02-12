from socket import *
import threading


class Server:
    def __init__(self, ip, port):
        self.socket = socket()
        self.socket.bind((ip, port))
        self.socket.listen()

    def run(self):
        while True:
            print('等待链接。。。')
            connSocket, addr = self.socket.accept()
            # 2.创建子线程t，执行handle方法，传入参数connSocket，并启动线程t

            while True:
                req = connSocket.recv(1024).decode()
                print('接收到的消息：', req)
                if not req:
                    break
                connSocket.send('你好，我收到你的消息了！'.encode())
            connSocket.close()
        self.socket.close()

    # 1. 定义handle方法，封装run方法中内层循环和关闭连接socket的代码


server = Server('0.0.0.0', 10021)
server.run()
