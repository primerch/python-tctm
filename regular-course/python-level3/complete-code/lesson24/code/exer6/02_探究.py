'''

我的程序运行报错，提示dict对象没有__dict__属性是什么原因，现在应该如何解决？
我之前发送Message对象都没问题。这是我发送消息的函数：
def sendMsg(self, msg):
    msg = json.dumps(msg.__dict__)
    self.socket.send(msg.encode())


'''
