'''
1. 同学们找到exer7中的01.py实验程序，运行01.py程序；
2. 在控制台输入老师指定的房间名，摁回车后，等待与老师进行视频通信；
3. 在建立视频通信后，关闭视频通信窗口，结束视频通信，但是不要关闭客户端主窗口；
4. 观察老师的屏幕中，老师的视频通信窗口是否还有你的摄像头画面。
'''
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
