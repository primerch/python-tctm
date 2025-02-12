import threading
from PyQt5.Qt import *
from PyQt5.QtWebEngineWidgets import *
from client import Message


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
        self.show()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl("https://l345.61it.cn/python.html"))
        layout.addWidget(self.browser)

    def closeEvent(self, event):
        if self.chatWindow.sender == self.sender:
            msg = Message('video', 'hangup', self.sender, self.to)
        else:
            msg = Message('video', 'hangup', self.to, self.sender)
        self.chatWindow.client.sendMsg(msg)
        self.chatWindow.videoFd = None


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
        self.setWindowTitle(self.sender + '  的客户端')
        icon = QIcon('../images/icon.png')
        self.setWindowIcon(icon)
        self.setFixedSize(self.width, self.height)
        self.setStyleSheet("background-color:#f0f0f0;")
        self.layout = QGridLayout()
        self.setLayout(self.layout)
        self.layout.setSpacing(0)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.msgLws = {}
        self.videoFd = None
        self.videoWindow = None
        self.box = None
        self.setUi()
        t = threading.Thread(target=self.getMsg, daemon=True)
        t.start()

    def closeEvent(self, event):
        if self.videoFd:
            self.videoWindow.close()

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
            if name == self.nameLb.text():
                box = QMessageBox(self)
                box.setText(name + "退出了")
                box.exec_()
                self.msgLws[name].close()
                self.nameLb.setText('')
                self.msgTxt.hide()
                self.sendBtn.hide()
                self.videoBtn.hide()
        elif msg['cmd'] == 'chat':
            sender = msg['sender']
            print('接收到来自' + sender + '的聊天消息:' + msg['content'])
            self.appendMsg(msg['content'], sender)
        elif msg['cmd'] == 'video':
            content = msg['content']
            if content == 'free':
                self.videoWindow = VideoWindow(self, msg['sender'], msg['to'])
            elif content == 'call':
                self.box = QMessageBox(self)
                self.box.setText(msg['sender'] + "向你发起视频聊天")
                self.box.addButton("接听", QMessageBox.AcceptRole)
                self.box.addButton("挂断", QMessageBox.RejectRole)
                result = self.box.exec_()
                if result == QMessageBox.AcceptRole:
                    self.videoWindow = VideoWindow(self, msg['sender'], msg['to'])
                    self.videoFd = msg['sender']
                # 1. 否则，创建消息对象msg，传入video,hangup,self.sender和msg['sender'],并发送

            elif content == 'busy':
                self.appendMsg('对方视频通话中', self.videoFd, Qt.AlignRight)
                self.videoFd = None
            elif content == 'hangup':
                # 2. 调用appendMsg方法，在msg['sender']的消息列表左侧显示对方已挂断

                self.videoWindow = None
                self.videoFd = None

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
        self.sendBtn.clicked.connect(self.btnSend)
        self.videoBtn = QPushButton(self)
        self.videoBtn.setFixedSize(30, 24)
        self.videoBtn.setIconSize(QSize(30, 24))
        self.videoBtn.setIcon(QIcon('../images/video.png'))
        self.videoBtn.setStyleSheet('border:none')
        self.videoBtn.move(750, 460)
        self.videoBtn.hide()
        self.videoBtn.clicked.connect(self.videoChat)

    def videoChat(self):
        print("进入视频聊天...")
        self.videoFd = self.nameLb.text()
        msg = Message('video', 'call', self.sender, self.videoFd)
        self.client.sendMsg(msg)

    def btnSend(self):
        content = self.msgTxt.toPlainText().strip()
        if content:
            to = self.nameLb.text()
            msg = Message('chat', content, self.sender, to)
            self.client.sendMsg(msg)
            self.appendMsg(content, to, Qt.AlignRight)
        self.msgTxt.clear()

    def appendMsg(self, content, fd, align=Qt.AlignLeft):
        item = QListWidgetItem()
        lw = self.msgLws[fd]
        lw.addItem(item)
        widget = QWidget()
        widget.setStyleSheet('border:none;')
        layout = QHBoxLayout()
        layout.setAlignment(align)
        widget.setLayout(layout)
        msgLb = QLabel(content)
        if align == Qt.AlignRight:
            msgLb.setStyleSheet('background-color:#95ec69;border-radius:5px;padding:10px 5px;')
        else:
            msgLb.setStyleSheet('background-color:#ffffff;border-radius:5px;padding:10px 5px;')
        layout.addWidget(msgLb)

        textWidth = msgLb.fontMetrics().width(content)
        if textWidth > 440:
            msgLb.setFixedWidth(440)
            msgLb.setWordWrap(True)

        item.setSizeHint(widget.sizeHint())
        lw.setItemWidget(item, widget)
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
        painter.drawEllipse(30, 0, 10, 10)
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
        self.videoBtn.show()
        if name == self.sender:
            self.videoBtn.hide()

    def setMsgList(self, name):
        msgLw = QListWidget()
        msgLw.setStyleSheet('border:none;border-top:1px solid gray')
        msgLw.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.msgLws[name] = msgLw
        self.layout.addWidget(msgLw, 1, 1)
        msgLw.hide()
