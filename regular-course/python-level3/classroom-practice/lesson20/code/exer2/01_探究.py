"""
第一段提示词：

```
from socket import *
serverSocket = socket()
serverSocket.bind(('172.25.6.40', 10011))
serverSocket.listen()
print('等待客户端连接...')
connSocket, addr = serverSocket.accept()
req = connSocket.recv(1024).decode()
print('服务端收到的消息：', req)
connSocket.send('你好，我是服务端。我收到你的消息了！'.encode())
connSocket.close()
serverSocket.close()
```
这段代码如何使用Server类来封装，实现相同的功能？

"""

"""
第二段提示词：

你能为我解释一下这段代码么，特别是每个方法的作用？

"""

"""
第三段提示词：

如何使用这个类执行服务端功能？

"""

"""
提醒：
1. 如果GPT首次生成的回答你觉得不好理解，
    可以点击重新生成按钮，多试几次，GPT一定会给你满意的答复

"""
