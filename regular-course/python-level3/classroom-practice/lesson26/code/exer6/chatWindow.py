import threading
from PyQt5.Qt import *
from client import Message


class ChatWindow(QWidget):
    signal = pyqtSignal(dict)

    def __init__(self, sender, client, avatars):
        super().__init__()
        self.signal.connect(self.handle)
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
            self.signal.emit(msg)

    def handle(self, msg):
        if msg['cmd'] == 'login':
            avatar = msg['content']
            name = msg['sender']
            item = QListWidgetItem(QIcon('../images/avatar/' + avatar), name)
            self.fdList.insertItem(0, item)
            self.setMsgList(name)
            self.avatars[name] = avatar
        elif msg['cmd'] == 'quit':
            name = msg['content']
            item = self.fdList.findItems(name, Qt.MatchExactly)[0]
            index = self.fdList.row(item)
            self.fdList.takeItem(index)
        elif msg['cmd'] == 'chat':
            sender = msg['sender']
            print('接收到来自' + sender + '的聊天消息:' + msg['content'])
            self.appendMsg(msg['content'], sender)

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
        # 5. 绑定发送按钮点击事件处理函数btnSend

    # 1. 定义点击发送按钮的事件处理函数btnSend

    # 2. 从文本输入框获取消息内容content，和获取正在聊天的好友名to

    # 3. 定义聊天消息对象msg，传入'chat',content,self.sender和to

    # 4. 在控制台上输出msg的__dict__属性

    def appendMsg(self, content, fd):
        item = QListWidgetItem(content)
        lw = self.msgLws[fd]
        lw.addItem(item)
        lw.scrollToBottom()
        fdItem = self.fdList.findItems(fd, Qt.MatchExactly)[0]
        row = self.fdList.row(fdItem)
        self.fdList.takeItem(row)
        self.fdList.insertItem(0, fdItem)
        if self.nameLb.text() != fd:
            self.drawIcon(fdItem)
        else:
            self.fdList.setCurrentItem(fdItem)

    def drawIcon(self, item):
        icon = item.icon()
        pixmap = icon.pixmap(40, 40)
        painter = QPainter(pixmap)
        painter.setBrush(QBrush(QColor("red")))
        painter.setPen(Qt.NoPen)
        painter.drawEllipse(25, 0, 15, 15)
        painter.end()
        item.setIcon(QIcon(pixmap))

    def selectFriend(self, curItem):
        avatar = self.avatars[curItem.text()]
        curItem.setIcon(QIcon('../images/avatar/' + avatar))
        self.msgTxt.show()
        self.sendBtn.show()
        pre = self.nameLb.text()
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
