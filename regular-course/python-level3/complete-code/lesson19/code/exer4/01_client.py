from socket import *

clientSocket = socket()
clientSocket.connect(('l345.61it.cn', 10011))
# 1. 将发送的字符串转换为二进制字节串
clientSocket.send('童童，你好！我是小派。'.encode())
clientSocket.close()
