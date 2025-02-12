from socket import *

# 1. 创建服务端socket对象
serverSocket = socket()
# 2. 绑定ip地址为exer2/02_ip.py中记录的ip，端口号为10011
serverSocket.bind(('172.25.6.40', 10011))
# 3. 让服务端socket拥有等待客户端连接的能力
serverSocket.listen()
# 4. 等待客户端连接请求
print('等待客户端连接...')
connSocket, addr = serverSocket.accept()
# 5. 接收客户端的请求消息，并输出
req = connSocket.recv(1024).decode()
print('接收到客户端的消息：', req)
# 6. 服务端给客户端发送消息
connSocket.send('我是服务端，我收到你的消息了！'.encode())
# 7. 关闭连接socket和服务器socket
connSocket.close()
serverSocket.close()
