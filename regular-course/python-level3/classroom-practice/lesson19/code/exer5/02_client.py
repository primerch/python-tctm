from socket import *

clientSocket = socket()
clientSocket.connect(('l345.61it.cn', 10011))
clientSocket.send('童童，你好！我是小派。'.encode())
# 1. 接收服务端返回的消息，并输出

clientSocket.close()
