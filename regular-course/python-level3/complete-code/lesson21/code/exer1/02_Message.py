# 1.定义Message消息类和cmd,content,sender,to四个属性，其中to默认为None
class Message:
    def __init__(self, cmd, content, sender, to=None):
        self.cmd = cmd
        self.content = content
        self.sender = sender
        self.to = to


# 2. 创建登录消息对象msg1,聊天消息对象msg2
msg1 = Message('login', '小派', '小派')
msg2 = Message('chat', '出来踢球', '小派', '童童')
# 3. 输出msg1和msg2对象的__dict__属性
print(msg1.__dict__)
print(msg2.__dict__)
# 4. 先运行程序，然后解开下行注释，再运行程序查看结果
print(msg1.encode())
