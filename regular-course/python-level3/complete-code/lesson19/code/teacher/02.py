'''

我先在要给6年级的孩子讲解使用python socket进行网络通信，我的讲解逻辑是这样的：
客户单的使用socket通信过程是先用socket()创建socket对象，然后用connect()连接服务端，然后输入内容用send()发送，recv()接收一个服务端反馈，最后close()关闭套接字
然后讲解服务端流程，先用socket()创建socket对象，然后用bind()绑定网络地址，然后用listen（）设置监听，然后accept()阻塞等待接收处理客户端连接，然后recv() send()和客户端配合收发，最后close关闭套接字
这是我的客户端代码：
from socket import *

clientSocket = socket()
clientSocket.connect(("127.0.0.1", 10012))
content = input('请输入发送的内容：')
clientSocket.send(content.encode())
res = clientSocket.recv(1024).decode()
print('接收到的消息：', res)
clientSocket.close()

这是我的服务端代码：
from socket import *
serverSocket = socket()
serverSocket.bind('127.0.0.1', 10012)
serverSocket.listen()

print('等待链接。。。')
cSocket, cAddr = serverSocket.accept()
req = cSocket.recv(1024).decode()
print('接收到客户端的消息：', req)
cSocket.send('你好，我收到你的消息了！'.encode())
cSocket.close()
serverSocket.close()
print('关闭')
请根据以上内容帮我使用中文，根据以上知识点出5道单选题，帮助6年级学生掌握这部分知识，其中既要包含
关于使用socket通信服务端和客户端的基本流程步骤，也要包含编程过程中涉及到的一些主要函数使用，不需要答案.

'''
a = 'a'
b = a.encode()
print(type(b))
