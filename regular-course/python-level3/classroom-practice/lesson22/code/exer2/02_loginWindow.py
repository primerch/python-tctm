from PyQt5.Qt import *


# 1. 从client.py导入Client类和Message类


class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        # 2. 创建连接至('l345.61it.cn',10041)的Client对象，存为client属性

        self.setWindowTitle("童程健康微信")
        icon = QIcon('../images/icon.png')
        self.setWindowIcon(icon)
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
        # 登录按钮
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
        # 3. 创建登录消息对象, 消息内容为0.jpg

        # 4. client对象调用sendeMsg发送登录消息

        # 5. client对象调用recvMsg接收响应字典，赋值给res

        # 6. 获取状态码和消息，赋值给code和msg，并输出

        # 7. 如果code为200，显示登录成功，如果为401，显示该用户已登录


if __name__ == '__main__':
    app = QApplication([])
    lgWindow = LoginWindow()
    lgWindow.show()
    app.exec_()
