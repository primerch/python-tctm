'''
我在给6年级的孩子讲解网络聊天程序中客户端使用图形界面登录，在此之前已经讲完了不使用图形界面，
客户端发送登录消息给服务端，收到服务端回复，显示在终端，并已经用代码实现。
在此基础上这部分我的讲解步骤是这样的：
问题： 在命令行操作不方便，平时软件操作都需要图形界面
解答 ：使用pyqt搭建登录界面，界面包含软件名称和图标，输入用户名的文本框和登录按钮。用户在文本框输入用户名，
点击登录按钮时程序发送用户名给服务端进行验证，并接收登录结果。这部分代码我使用AI工具用pyqt生成，
然后总结了使用PyQt创建Weight主窗口分为几步,要实现以上登录界面需要哪些控件？还有其他的功能。
问题：之前已经实现了在终端命令行发送登录消息，换成界面怎么发送登录消息，代码是否需要重写
解答 ： 不需要，只需要导入之前写好的客户端发送接收函数和消息类就行，整体分2步 1.点击登录按钮时获取到输入
的用户名；2. 结合之前的客户端程序将用户名发送给服务端，得到服务端反馈。
具体实现过程：1.导入client模块下的Client类和Message类；2. 创建连接；3.login方法中发送登录信息，
接收登录结果：3.1创建Message类型对象，3.2使用sendMsg和recvMsg收发消息，与之前一样；
3.3 分情况显示接收结果

这是我的客户端代码：

class LoginWindow(QWidget):
    def __init__(self,):
        super().__init__()
        # 2. 定义client属性
        self.client = Client('l345.61it.cn', 10041)
        self.setWindowTitle("同学微信")
        self.width = 280
        self.height = 400
        self.setFixedSize(self.width, self.height)
        self.setStyleSheet("background-color:white")
        self.setup_ui()

    def setup_ui(self):
        layout = QGridLayout()
        self.setLayout(layout)
        # 添加微信图标
        self.wechatLb = QLabel()
        self.pixmap = QPixmap('../images/wechat.png')
        self.wechatLb.setPixmap(self.pixmap)
        self.wechatLb.setFixedHeight(200)
        self.wechatLb.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.wechatLb, 0, 0, 1, 2)

        # 账号标签
        self.senderLb = QLabel('昵称')
        self.senderLb.setStyleSheet('font-size:12px')
        layout.addWidget(self.senderLb, 1, 0, 1, 1)
        # 账号输入框
        self.senderLe = QLineEdit('小派')
        self.senderLe.setFixedHeight(30)
        self.senderLe.setPlaceholderText('请填写昵称')
        self.senderLe.setStyleSheet('font-size:12px')
        layout.addWidget(self.senderLe, 1, 1, 1, 1)
        # 登录结果显示Label
        self.resultLb = QLabel()
        self.resultLb.resize(230, 50)
        layout.addWidget(self.resultLb, 2, 0, 1, 2, alignment=Qt.AlignCenter)

        self.loginBtn = QPushButton('登录')
        self.loginBtn.setFixedSize(180, 40)
        layout.addWidget(self.loginBtn, 3, 0, 1, 2, alignment=Qt.AlignCenter)
        self.loginBtn.clicked.connect(self.login)

    def login(self):
        sender = self.senderLe.text()
        if not sender:
            self.resultLb.setText('用户名不能为空')
            return
        self.resultLb.setText('正在登录...')
        # 3. 创建登录消息对象, 发送消息并接收服务器响应
        msg = Message('login', "0.jpg", sender)
        self.client.sendMsg(msg)
        res = self.client.recvMsg()
        # 4. 获取服务器响应码和响应消息，并输出查看
        code = res['code']
        msg = res['msg']
        print('状态码', code, '消息：', msg)
        # 5. 判断服务器响应状态码，显示对应提示信息
        if code == 200:
            self.resultLb.setText('登录成功')
        elif code == 401:
            self.resultLb.setText('该用户已登陆')

请根据以上内容帮我使用中文，根据以上知识点出5道单选题，主要考察：客户端发送登录消息给服务端并接受回复的步骤，
客户端界面结合Client类和Message类的实现客户端功能的步骤，搭建登录界面窗口的步骤，使用登录界面登录的步骤等，
注意着重考察登录过程实现步骤，无需考察代码细节和函数使用，不需要答案.

'''
