from PyQt5.Qt import *
from PyQt5.QtWebEngineWidgets import *


class VideoWindow(QWidget):
    def __init__(self, chatWindow, sender, to):
        super().__init__()
        self.chatWindow = chatWindow
        self.sender = sender
        self.to = to
        self.setWindowTitle(self.chatWindow.sender)
        self.setGeometry(0, 0, 660, 340)
        layout = QGridLayout()
        self.setLayout(layout)
        self.browser = QWebEngineView()
        self.browser.page().featurePermissionRequested.connect(self.getPermission)
        self.browser.setUrl(QUrl(f"https://l345.61it.cn/python.html?room={room}"))
        layout.addWidget(self.browser)
        self.show()

    def getPermission(self, url, feature):
        self.browser.page().setFeaturePermission(url, feature, QWebEnginePage.PermissionGrantedByUser)

    def closeEvent(self, event):
        # 1. 设置浏览器显示空白页面

        pass


class ChatWindow(QWidget):

    def __init__(self, sender, client, avatars):
        super().__init__()
        self.sender = sender
        self.avatars = avatars
        self.client = client
        self.width = 800
        self.height = 600
        self.setWindowTitle(self.sender + '  的客户端')
        self.setFixedSize(self.width, self.height)
        self.videoWindow = VideoWindow(self, self.sender, self.sender)


if __name__ == '__main__':
    room = input('请输入房间名：')
    app = QApplication([])
    chatWindow = ChatWindow('测试', None, None)
    chatWindow.show()
    app.exec_()
