import threading
from PyQt5.Qt import *
from client import Message


# 1. 创建视频聊天窗口类VideoWindow，继承自QWidget
class VideoWindow(QWidget):
    # 2. 定义__init__方法，chatWindow、sender、to属性并调用父类的__init__方法
    def __init__(self, chatWindow, sender, to):
        self.chatWindow = chatWindow
        self.sender = sender
        self.to = to
        # 3. 设置窗口标题为"video"，坐标位置为(0,0)，大小为(660,340)
        self.setWindowTitle("video")
        self.setGeometry(0, 0, 660, 340)
        # 4. 创建网格布局layout
        layout = QGridLayout()
        # 5. 设置窗口的布局为layout
        self.setLayout(layout)
        # 6. 显示窗口
        self.show()


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
        self.videoFd = None
        # 7. 定义videoWindow属性,默认为None
        self.videoWindow = None
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
        # 8. 判断msg是否为视频聊天消息，如果是，获取消息内容content
        elif msg['cmd'] == 'video':
            content = msg['content']
            # 9. 如果content等于free
            if content == 'free':
                # 10. 创建VideoWindow类的对象，存储到videoWindow属性中
                self.videoWindow = VideoWindow(self, msg['sender'], msg['to'])

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
