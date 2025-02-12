'''

我要给6年级的孩子讲解网络聊天小项目中客户端登录，服务端处理登录的过程，这部分我的讲解逻辑是这样的：
问题： 微信的服务器怎么知道每个人的用户名？又是如何把消息准确转发给每个人的呢
解答 ：阶段1. 客户端发送登录信息，服务端提取用户名。阶段2. 服务端保存所有登录的用户名和对应的连接。阶段3. 服务端收到消息，查找收件人，给其转发消息
讲解： 今天这部分先完成第一阶段，客户端发送登录信息，服务端提取用户名
步骤 ：1. 客户端发送登录消息；2. 服务端收到登录消息并解析用户名，然后返回登录结果信息；3. 客户端接收登录结果
讲解 ： 第1步客户端发送登录消息代码实现过程  ： 1. input请用户输入用户名；2. Message类创建登录消息对象；
3.  使用json.dumps转换为JSON格式数据；4. send发送给服务端
因为第2步客户端接收登录结果，也是客户端功能，所以先讲解这部分代码：1.res = self.socket.recv(1024).decode()接收服务端
回复 ； 2.使用json.loads转换JSON格式为字典。然后讲解服务端也就是步骤2 服务端收到登录消息并解析用户名，然后返回登录结果
信息。消息收发部分与客户端代码类似，主要是回复的消息结构中用code:200表示请求登录已经成功


这是我的客户端代码：

class Message:
    def __init__(self, cmd, content, sender, to=None):
        self.cmd = cmd
        self.content = content
        self.sender = sender
        self.to = to

class Client:
    def __init__(self, ip, port):
        self.socket = socket()
        self.socket.connect((ip, port))

    def run(self):
        content = input('请输入消息内容：')
        req = Message('login', content, '小派')
        self.sendMsg(req)
        res = self.recvMsg()
        print('接收到服务端的消息是：', res)
        code = res['code']
        msg = res['msg']
        print('状态码',code,'消息：', msg)
        self.socket.close()

    def sendMsg(self, msg):
        msg = json.dumps(msg.__dict__)
        self.socket.send(msg.encode())

    def recvMsg(self):
        msg = self.socket.recv(1024).decode()
        msg = json.loads(msg)
        return msg


client = Client('localhost', 10031)
client.run()

这是我的服务端代码：

# 预留的message类
class Message:
    def __init__(self, cmd, content, sender, to=None):
        self.cmd = cmd
        self.content = content
        self.sender = sender
        self.to = to


class Server:
    def __init__(self, ip, port):
        self.socket = socket.socket()
        self.socket.bind((ip, port))
        self.socket.listen()

    def run(self):
        while True:
            print('等待链接。。。')
            connSocket, cAddr = self.socket.accept()
            t = threading.Thread(target=self.handle, args=[connSocket])
            t.start()

    def handle(self, connSocket):
        while True:
            req = self.recvMsg(connSocket)
            print('接收到的消息：', req)
            if not req:
                break
            msg = Message(req['cmd'], '你好，我收到你的消息了！', '服务器')
            self.sendMsg(connSocket,200,msg)
        connSocket.close()

    def sendMsg(self,connSocket,code, msg):
        msg = json.dumps({'code':code,'msg':msg.__dict__})
        connSocket.send(msg.encode())

    def recvMsg(self,connSocket):
        msg = connSocket.recv(1024).decode()
        # 1. 判断收到的消息是否为空
        if not msg:
            return
        msg = json.loads(msg)
        return msg


if __name__ == '__main__':

    server = Server('localhost', 10031)
    server.run()

请根据以上内容帮我使用中文，根据以上知识点出5道单选题，主要考察：实现客户端发送聊天信息给服务端转发分为具体哪几个阶段实现，
客户端登录的实现步骤，服务端接收回复登录信息的步骤，重要的代码细节等知识，不需要答案.

'''
