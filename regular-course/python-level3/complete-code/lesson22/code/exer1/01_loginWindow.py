"""

使用pyqt5制作一个童程健康微信登录界面，你需要完成以下功能：
1. 导入所有必要的模块，定义LoginWidnow类，继承自QWidget，
2. 设置窗口标题为童程健康微信，窗口大小为280*400，背景设置为白色，
   设置窗口图标为../images/icon.png
3. 定义setupUi方法，设置网格布局
4. 在网格布局中添加一个标签，只设置标签高固定为200，宽不设置大小，位置为0,0,1,2，
   在标签上设置微信图标(../images/wechat.png)，不要改变图标大小，并且水平居中
5. 添加一个标签，标签的文本为昵称，标签的字体大小为12px，标签的位置为1, 0, 1, 1
6. 添加一个单行文本输入框(senderLe)，设置高固定为30px,宽默认大小，默认显示：请输入昵称，
   字体大小为12px, 位置为1, 1, 1, 1
7. 添加一个标签(resultLb)，显示登录结果，只设置标签高固定为50，宽不设置大小,
   设置位置为2, 0, 1, 2，并且设置其在占据的格子中居中对齐。
8. 添加一个登录按钮，宽高为180, 40，设置位置为3, 0, 1, 2，并且设置其在占据的格子中居中对齐。
9. 当点击登录按钮时，获取文本框中的内容(sender)，如果内容为空，则在登录结果标签中显示用户名不能为空，
   停止执行后续代码，否则显示正在登录...。
10. 创建对象，显示界面
请输出要求的代码

"""
# 1. 使用上述提示词，生成登录界面
from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QGridLayout, QApplication
from PyQt5.QtGui import QPixmap, QIcon, QFont
from PyQt5.QtCore import Qt


class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('童程健康微信')
        self.setFixedSize(280, 400)
        self.setStyleSheet("background-color: white;")
        self.setWindowIcon(QIcon('../images/icon.png'))

        self.setupUi()

    def setupUi(self):
        grid = QGridLayout()
        self.setLayout(grid)

        label_img = QLabel(self)
        label_img.setFixedHeight(200)
        pixmap = QPixmap('../images/wechat.png')
        label_img.setPixmap(pixmap)
        label_img.setAlignment(Qt.AlignCenter)
        grid.addWidget(label_img, 0, 0, 1, 2)

        label_nickname = QLabel('昵称', self)
        label_nickname.setFont(QFont('Arial', 12))
        grid.addWidget(label_nickname, 1, 0, 1, 1)

        self.senderLe = QLineEdit(self)
        self.senderLe.setFixedHeight(30)
        self.senderLe.setFont(QFont('Arial', 12))
        self.senderLe.setPlaceholderText('请输入昵称')
        grid.addWidget(self.senderLe, 1, 1, 1, 1)

        self.resultLb = QLabel(self)
        self.resultLb.setFixedHeight(50)
        self.resultLb.setAlignment(Qt.AlignCenter)
        grid.addWidget(self.resultLb, 2, 0, 1, 2)

        login_button = QPushButton('登录', self)
        login_button.setFixedSize(180, 40)
        login_button.clicked.connect(self.login)
        grid.addWidget(login_button, 3, 0, 1, 2, Qt.AlignCenter)

    def login(self):
        sender = self.senderLe.text()
        if sender == '':
            self.resultLb.setText('用户名不能为空')
        else:
            self.resultLb.setText('正在登录...')


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    window = LoginWindow()
    window.show()
    sys.exit(app.exec_())
