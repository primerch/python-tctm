from PyQt5.Qt import *
from client import Client, Message
# 导入定义好的ChatWindow类
from chatWindow import ChatWindow


class LoginWindow(QWidget):
    def __init__(self, ):
        super().__init__()
        self.client = Client('l345.61it.cn', 10051)
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
        self.wechatLb = QLabel()
        self.pixmap = QPixmap('../images/wechat.png')
        self.wechatLb.setPixmap(self.pixmap)
        self.wechatLb.setFixedHeight(200)
        self.wechatLb.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.wechatLb, 0, 0, 1, 2)
        self.senderLb = QLabel('昵称')
        self.senderLb.setStyleSheet('font-size:12px')
        layout.addWidget(self.senderLb, 1, 0, 1, 1)
        self.senderLe = QLineEdit('小派')
        self.senderLe.setFixedHeight(30)
        self.senderLe.setPlaceholderText('请填写昵称')
        self.senderLe.setStyleSheet('font-size:12px')
        layout.addWidget(self.senderLe, 1, 1, 1, 1)
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
            self.resultLb.setText('账号不能为空')
            return
        self.resultLb.setText('正在登录...')
        msg = Message('login', '0.jpg', sender)
        self.client.sendMsg(msg)
        res = self.client.recvMsg()
        code = res['code']
        msg = res['msg']
        print('状态码', code, '消息：', msg)
        if code == 200:
            self.resultLb.setText('登录成功')
            # 1. 隐藏登录窗口

            # 2. 创建聊天界面对象，传入发送人，客户端对象，头像字典，并显示

        elif code == 401:
            self.resultLb.setText('该用户已登陆')


if __name__ == '__main__':
    app = QApplication([])
    lgWindow = LoginWindow()
    lgWindow.show()
    app.exec_()
