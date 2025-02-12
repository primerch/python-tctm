"""
第一段提示词：

```
这是我的服务端代码：
import socket
class Server:
    def __init__(self,ip,port):
        self.socket = socket.socket()
        self.socket.bind((ip, port))
        self.socket.listen()
    def run(self):
        print('等待链接。。。')
        connSocket, addr = self.socket.accept()
        while True:
            req = connSocket.recv(1024).decode()
            if not req:
                break
            print('服务端收到的消息：', req)
            connSocket.send('你好，我是服务端。我收到你的消息了！'.encode())
        connSocket.close()
        self.socket.close()
server = Server('localhost', 10021)
server.run()
```
当第一个客户端连接后，只要不退出，第二个客户端就没办法连接收发消息，这是为什么？
如何让多个客户端同时连接到一个服务端？

"""

"""
第二段提示词：

我是一名6年级小学生，你能为我通俗的解释一下线程是什么，请使用家里大扫除的场景进行类别讲解。

"""

"""
提醒：
1. 如果GPT首次生成的回答你觉得不好理解，
    可以点击重新生成按钮，多试几次，GPT一定会给你满意的答复

"""
