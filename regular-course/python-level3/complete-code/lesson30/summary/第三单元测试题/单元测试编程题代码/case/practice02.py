from socket import *
# 1. 创建服务端socket对象
serverSocket = socket()
# 2. 绑定ip地址0.0.0.0和端口号10122
serverSocket.bind(('0.0.0.0', 10122))
# 3. 让socket处于监听状态
serverSocket.listen()
# 4. 等待客户端的连接
connSocket, addr = serverSocket.accept()
# 5. 接收客户端的消息，并输出
req = connSocket.recv(1024).decode()
print('接收到客户端的消息：', req)
# 6. 给客户端发送消息：'我是服务端，我收到你的消息了！'
connSocket.send('我是服务端，我收到你的消息了！'.encode())
# 7. 关闭连接socket和服务端socket
connSocket.close()
serverSocket.close()