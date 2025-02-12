import threading
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
        self.msgLws = {}
        self.setUi()
        t = threading.Thread(target=self.getMsg, daemon=True)
        t.start()

    def getMsg(self):
        while True:
            res = self.client.recvMsg()
            print('聊天窗口收到消息：', res)
            msg = res['msg']
            if msg['cmd'] == 'login':
                avatar = msg['content']
                name = msg['sender']
                item = QListWidgetItem(QIcon('../images/avatar/' + avatar), name)
                self.fdList.insertItem(0, item)
                self.setMsgList(name)
            elif msg['cmd'] == 'quit':
                name = msg['content']
                item = self.fdList.findItems(name, Qt.MatchExactly)[0]
                index = self.fdList.row(item)
                self.fdList.takeItem(index)

    def setUi(self):
        self.fdList = QListWidget()
        self.layout.addWidget(self.fdList, 0, 0, 3, 1)
        self.fdList.setIconSize(QSize(40, 40))
        for name, avatar in self.avatars.items():
            item = QListWidgetItem(QIcon('../images/avatar/' + avatar), name)
            self.fdList.insertItem(0, item)
            self.setMsgList(name)
        self.nameLb = QLabel()
        self.nameLb.setFixedSize(550, 60)
        self.nameLb.setStyleSheet("padding-left:10px")
        self.layout.addWidget(self.nameLb, 0, 1, 1, 1)
        self.msgTxt = QTextEdit(self)
        self.msgTxt.setFixedHeight(145)
        self.msgTxt.setStyleSheet('border:none;border-top:1px solid gray;')
        self.layout.addWidget(self.msgTxt, 2, 1, 1, 1)
        self.sendBtn = QPushButton('发送', self)
        self.sendBtn.move(685, 555)
        self.msgTxt.hide()
        self.sendBtn.hide()
        self.fdList.itemClicked.connect(self.selectFriend)

    def selectFriend(self, curItem):
        self.msgTxt.show()
        self.sendBtn.show()
        # 1. 从nameLb中获取之前选中的好友名pre
        pre = self.nameLb.text()
        # 2. 如果pre不为空，就隐藏之前好友的消息列表控件
        if pre:
            self.msgLws[pre].hide()
        name = curItem.text()
        self.nameLb.setText(name)
        self.msgLws[name].show()

    def setMsgList(self, name):
        msgLw = QListWidget()
        msgLw.setStyleSheet('border:none;border-top:1px solid gray')
        self.msgLws[name] = msgLw
        self.layout.addWidget(msgLw, 1, 1)
        msgLw.hide()
        item = QListWidgetItem(name + "的消息列表")
        msgLw.insertItem(0, item)
