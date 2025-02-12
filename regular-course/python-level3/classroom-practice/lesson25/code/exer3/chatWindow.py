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
        # 1. 定义msgLws属性，默认为空字典，保存每个好友对应的消息列表控件

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
                # 7.调用setMsgList方法

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
            # 6.调用setMsgList方法

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
        name = curItem.text()
        self.nameLb.setText(name)

    # 2.定义创建消息列表控件方法setMsgList和参数name

    # 3. 创建消息列表控件msgLw

    # 4. 设置msgLw控件只有顶部有1px的灰色边框，其他没有边框

    # 5. 将msgLw控件保存到好友消息列表字典中，并输出好友消息列表字典
