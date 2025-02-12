# 1. 导入json模块
import json


class Message:

    def __init__(self, cmd, content, sender, to=None):
        self.cmd = cmd
        self.content = content
        self.sender = sender
        self.to = to


msg = Message('login', '小派', '小派')
print(msg.__dict__)
# 2. 将字典对象编码成JSON字符串，并输出查看
jstr = json.dumps(msg.__dict__)
print(jstr)
# 3. 将JSON字符串解析为字典对象，并输出查看
dic = json.loads(jstr)
print(dic)
