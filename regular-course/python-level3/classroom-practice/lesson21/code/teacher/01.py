'''

我要给6年级的孩子讲解JSON数据格式，这部分我的讲解逻辑是这样的：
问题： 聊天的项目客户端发送给服务端的内容不仅有聊天信息还有登录信息，如何组织这些信息的结构
解决 ：定义一个Message类，在类中添加to sender，content ,cmd 等属性，统一传输消息格式
问题： 但是类创建的对象不能通过网络发送怎么办
解决 ：使用JSON数据结构
问题： 什么是JSON结构
解决 ： 讲解JSON结构的特点，与字典格式类似，大括号包裹对象内容，对象中每个属性以名值对的方式写入大括号中，
每个属性间用逗号分隔，属性名用双信号，属性名值之间用冒号，属性值如果是字符串就加双引号，数字则不用引号，
是None则转换为null也无需引号。就像用单引号将"字典"引起来
JSON优点 ：易读性，每个属性值都有属性名描述，人和计算机都能看懂；通用性，本质上是字符串，跨不同编程语言、
不同操作系统通用
问题 ：如何把对象中属性的名字和值转换为JSON结构数据保存，能够通过网络发送
解决： 讲解 json 模块，对象不能直接转为JSON，所以，需要把对象先用__dict__转为字典，
再将字典用 json.dumps方法转换为JSON；json也不能直接转对象，只能使用json.loads 方法将json转为字典便于使用
这是我的客户端代码：
import json


class Message:

    def __init__(self, cmd, content, sender, to=None):
        # 消息对应的命令：登录，聊天，退出
        self.cmd = cmd
        # 消息对应的内容
        self.content = content
        # 用户账号
        self.sender = sender
        # 接收消息的好友
        self.to = to


msg = Message('login', '小派', '小派')
print(msg.__dict__)
jstr = json.dumps(msg.__dict__)
print(jstr)
dic = json.loads(jstr)
print(dic)

请根据以上内容帮我使用中文，根据以上知识点出5道单选题，主要考察JSON类型的格式、特点、用途,
json模块中dumps、loads函数使用，不需要答案.

'''
