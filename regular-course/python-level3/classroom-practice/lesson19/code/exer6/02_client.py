from socket import *

clientSocket = socket()
# 1. 修改下方IP地址为exer2/02_ip.py中记录的ip，端口号为10011。
clientSocket.connect(('请改为本机IP地址', 10011))
clientSocket.send('童童，你好！我是小派。'.encode())
res = clientSocket.recv(1024).decode()
print('收到消息：', res)
clientSocket.close()

'''
调试步骤：
1. 修改第4行IP地址为本机IP地址，并运行02_client.py
2. 如果看到控制台中02_client.py中出现服务端返回的消息，说明成功
3. 在控制台中切换到02_server.py运行界面，看到客户端发来的消息说明成功
'''
