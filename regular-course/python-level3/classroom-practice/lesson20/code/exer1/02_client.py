from socket import *

# 1. 使用面向对象编程的方式定义客户端类Client

clientSocket = socket()
clientSocket.connect(('l345.61it.cn', 10021))
clientSocket.send('童童，你好！我是小派。'.encode())
res = clientSocket.recv(1024).decode()
print('客户端收到的消息：', res)
clientSocket.close()

# 2. 创建客户端对象client，传入域名:l345.61it.cn和端口号：10021

# 3. 调用run()方法
