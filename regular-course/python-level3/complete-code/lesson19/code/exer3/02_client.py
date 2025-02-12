# 1. 导入socket模块中的所有函数、类、变量
from socket import *

# 2. 创建一个客户端socket对象，存到变量clientSocket
clientSocket = socket()
# 3. 连接域名为l345.61it.cn，端口为10011的服务端
clientSocket.connect(('l345.61it.cn', 10011))
# 4. 向服务端发送消息：童童，你好！我是小派。
clientSocket.send('童童，你好！我是小派。')
# 5. 关闭客户端socket对象
clientSocket.close()
