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
    avatars = {'程程': 'boy.png', '美美': 'girl.png'}
    chatWindow = ChatWindow('小派', None, avatars)
    chatWindow.show()
    app.exec_()
