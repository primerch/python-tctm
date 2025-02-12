'''

我先在要给6年级的孩子讲解了多线程socket服务端同时为多个客户端服务，他们之前已经学习过socket使用，并完成了循环的服务端模型可以一个一个处理客户端连接和收发消息，
这部分我的讲解逻辑是这样的：
问题： 为什么第一个客户端只要不退出，后面的客户端就不能和服务端收发消息
解决 ：耗时的内层循环创建为一个子线程，不要影响主线程中的accept循环执行
问题： 如何实现
解决 ：
第一步 ： 先把耗时的任务：收发消息的内层循环独立写成一个函数。
第二部： 在原内层循环的位置创建新线程，放入第一步定义的任务函数，并将收发消息的套接字cSocket通过Thread传递给线程函数，
第三步： 启动线程

这是我的服务端代码：
class Server:
    def __init__(self,ip,port):
        self.ip = ip
        self.port = port
        self.socket = socket()
        self.socket.bind((ip, port))
        self.socket.listen()

    def run(self):
        # 1. 添加无限循环，循环处理多个客户端的请求
        while True:
            print('等待链接。。。')
            cSocket, cAddr = self.socket.accept()
            # 2. 改为守护线程
            t = threading.Thread(target=self.handle, args=[cSocket])
            t.start()

    def handle(self, cSocket):
        while True:
            req = cSocket.recv(1024).decode()
            print('接收到的消息：', req)
            if not req:
                break
            cSocket.send('你好，我收到你的消息了！'.encode())
        cSocket.close()

请根据以上内容帮我使用中文，根据以上知识点出5道单选题，主要考察代码和代码实现步骤，题目语言通俗易懂，不要超出代码范围，不需要答案.

'''
