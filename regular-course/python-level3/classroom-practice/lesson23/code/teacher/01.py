'''
我在给6年级的孩子一个聊天程序。之前已经讲解完成了socket通信和登录的基本功能，在此基础上继续讲解，
讲解步骤是这样的：
问题：用户登录成功后如果退出再重启，就不能用原来用户名登录了，提示该用户已登录
原因：初步分析是因为用户客户端关闭，但是服务端字典里，没有及时删除用户的信息，导致同一个用户名不能再次登
录。客户端退出需要一个善后工作
解决：编写一个quit方法 ： 1.关闭客户端连接socket 2.删除avatars中保存的头像信息和connSockets中保存的客
户端socket信息。当服务端收到客户端退出消息，调用quit
问题： 登录成功后应该进入聊天界面，接下来要完成聊天界面，如何完成？
分析： 聊天界面应该包含 好友列表、显示聊天内容区域、文本输入区域、发送按钮
解决： 使用pyqt创建聊天界面，这里可以使用AI工具生成
问题 ：有了聊天窗口类 ChatWindow就可以先创建窗口对象，然后通过show 显示聊天窗口，但是这个类需要什么额外
属性？
解决 ：因为聊天时需要告知服务端自己是谁，所以需要自己的用户名sender；因为需要与服务端发送聊天消息，所以
也需要客户端对象client，
因为需要显示好友列表所以需要好友用户名和头像字典avatars

问题：现在聊天界面有了如何在登录成功后切换到聊天界面呢
解决：分为3步： 1.隐藏登录界面lgWindow.hide()  2.创建聊天界面对象  3.显示聊天界面chatWindow.show()
问题： 但是界面出现一下就消失了原因是什么
解决： 因为创建的聊天界面对象是login方法中的局部变量，使用global 声明为全局变量即可
至此完成了登录成功后显示出聊天窗口

这是我的客户端代码：
# 创建聊天窗口
class ChatWindow(QWidget):
    def __init__(self, sender, client, avatars):
       ...

# 登录窗口
class LoginWindow(QWidget):
    def __init__(self,):
        ...

    def setup_ui(self):
        ...

    def login(self):
        sender = self.senderLe.text()
        if not sender:
            self.resultLb.setText('账号不能为空')
            return
        self.resultLb.setText('正在登录...')
        msg = Message('login', "0.jpg", sender)
        self.client.sendMsg(msg)
        res = self.client.recvMsg()
        code = res['code']
        msg = res['msg']
        print('状态码', code, '消息：', msg)
        if code == 200:
            self.resultLb.setText('登录成功')
            lgWindow.hide()
            # 1. 声明chatWindow为全局变量
            global chatWindow
            chatWindow = ChatWindow(sender, self.client, msg['content'])
            chatWindow.show()
        elif code == 401:
            self.resultLb.setText('该用户已登陆')

请根据以上内容帮我使用中文，根据以上知识点出5道单选题，主要考察：客户端退出服务端需要哪些处理，
聊天窗口包含内容，聊天窗口类属性，登录成功如何切换到聊天窗口，如何让聊天窗口一直显示等知识，不需要答案.

'''
