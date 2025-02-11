from socket import *
# 1. 创建客户端socket对象
clientSocket = socket()
# 2. 连接到ip地址为'l345.61it.cn'，端口号为10122的服务端
clientSocket.connect(('l345.61it.cn', 10122))
# 3. 向服务端发送消息："你好，我毕业了！"
clientSocket.send('你好，我毕业了！'.encode())
# 4. 接收服务端发送的消息，并输出
res = clientSocket.recv(1024).decode()
print('收到的消息：', res)
# 5. 关闭连接
clientSocket.close()

