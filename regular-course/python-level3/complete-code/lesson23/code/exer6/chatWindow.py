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
        # 4.调用setUi
        self.setUi()

    # 1. 定义setUi方法
    def setUi(self):
        # 2. 定义列表控件fdList属性,放到网格布局的第1行，第1列，占据3行1列
        self.fdList = QListWidget()
        self.layout.addWidget(self.fdList, 0, 0, 3, 1)
        # 3. 设置列表所有项图标的大小为40*40
        self.fdList.setIconSize(QSize(40, 40))
        # 4. 遍历avatars字典,获取名称和头像,依次添加到一个列表项,并添加到列表中
        for name, avatar in self.avatars.items():
            item = QListWidgetItem(QIcon('../images/avatar/' + avatar), name)
            self.fdList.insertItem(0, item)


if __name__ == '__main__':
    app = QApplication([])
    avatars = {'程程': 'boy.png', '美美': 'girl.png'}
    chatWindow = ChatWindow('小派', None, avatars)
    chatWindow.show()
    app.exec_()
