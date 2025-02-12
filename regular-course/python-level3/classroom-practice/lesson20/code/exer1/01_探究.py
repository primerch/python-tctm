"""
第一段提示词：

```
from socket import *
clientSocket = socket()
clientSocket.connect(('l345.61it.cn', 10011))
clientSocket.send('童童，你好！我是小派。'.encode())
# 1. 接收服务器返回的消息
res = clientSocket.recv(1024).decode()
print('收到的消息：', res)
clientSocket.close()
```
这段代码如何使用Client类来封装，实现相同的功能？如何使用Client类运行客户端程序?

"""

"""
第二段提示词：

你能为我解释一下这段代码吗？特别是每个方法的作用？

"""

"""
第三段提示词：

如何使用这个类执行客户端功能？

"""

"""
提醒：
1. 如果GPT首次生成的回答你觉得不好理解，
    可以点击重新生成按钮，多试几次，GPT一定会给你满意的答复

"""
