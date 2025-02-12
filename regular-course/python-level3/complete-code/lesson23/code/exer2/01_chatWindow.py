"""

使用pyqt5生成一个聊天界面，要求如下：
1. 导入所有必要的模块，定义ChatWindow类，继承自QWidget
2. 它有三个属性：sender, client, avatars
3. 设置窗口的大小为800*600，标题为童程健康微信，
   图标为../images/icon.png，背景颜色为#f0f0f0，
4. 设置窗口布局为网格布局，设置布局间距和边距为0
5. 创建ChatWindow的对象，给三个参数传入None，并显示窗口
请给出符合要求的代码

"""
# 1. 请使用上述提示词，生成登录界面
from PyQt5.Qt import *


class ChatWindow(QWidget):
    def __init__(self, sender, client, avatars):
        super().__init__()
        self.sender = sender
        self.avatars = avatars
        self.client = client
        self.width = 800
        self.height = 600
        self.setWindowTitle("童程健康微信")
        icon = QIcon('../images/icon.png')
        self.setWindowIcon(icon)
        self.setFixedSize(self.width, self.height)
        self.setStyleSheet("background-color:#f0f0f0;")
        self.layout = QGridLayout()
        self.setLayout(self.layout)
        self.layout.setSpacing(0)
        self.layout.setContentsMargins(0, 0, 0, 0)


if __name__ == '__main__':
    app = QApplication([])
    chatWindow = ChatWindow(None, None, None)
    chatWindow.show()
    app.exec_()
