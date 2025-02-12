import threading
from PyQt5.Qt import *
from PyQt5.QtWebEngineWidgets import *
from client import Message
import os


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
        self.browser.page().featurePermissionRequested.connect(self.getPermission)
        self.browser.setUrl(QUrl(f"https://l345.61it.cn/python.html?room={self.sender}-{self.to}"))
        layout.addWidget(self.browser)

    def getPermission(self, url, feature):
        self.browser.page().setFeaturePermission(url, feature, QWebEnginePage.PermissionGrantedByUser)

    def closeEvent(self, event):
        if self.chatWindow.sender == self.sender:
            msg = Message('video', 'hangup', self.sender, self.to)
        else:
            msg = Message('video', 'hangup', self.to, self.sender)
        self.chatWindow.client.sendMsg(msg)
        self.chatWindow.videoFd = None
        self.browser.setUrl(QUrl('about:blank'))


class EmojiPicker(QWidget):
    def __init__(self, chatWindow):
        super().__init__()
        self.chatWindow = chatWindow
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.layout = QGridLayout(self)
        self.setUi()

    def setUi(self):
        row = col = 0
        for name in os.listdir('../images/emojis/'):
            btn = QPushButton()
            btn.setIcon(QIcon('../images/emojis/' + name))
            btn.setIconSize(QSize(30, 30))
            btn.setFixedSize(30, 30)
            btn.setToolTip(name)
            btn.clicked.connect(self.onEmojiClicked)
            self.layout.addWidget(btn, row, col)
            col += 1
            if col == 14:
                row += 1
                col = 0

    def onEmojiClicked(self):
        sender = self.sender()
        name = sender.toolTip()
        self.chatWindow.msgTxt.setText(name)
        self.chatWindow.btnSend()
        self.hide()


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
        self.emojiPicker.close()

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
                self.emoBtn.hide()
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
                if self.box:
                    if result == QMessageBox.AcceptRole:
                        self.videoWindow = VideoWindow(self, msg['sender'], msg['to'])
                        self.videoFd = msg['sender']
                    else:
                        msg = Message('video', 'hangup', self.sender, msg['sender'])
                        self.client.sendMsg(msg)
            elif content == 'busy':
                self.appendMsg('对方视频通话中', self.videoFd, Qt.AlignRight)
                self.videoFd = None
            elif content == 'hangup':
                if self.box:
                    self.box.close()
                    self.box = None
                self.appendMsg('对方已挂断', msg['sender'])
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
        self.msgTxt.setStyleSheet('border:none;border-top:1px solid gray;padding-top:30px')
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
        self.emoBtn = QPushButton(self)
        self.emoBtn.setFixedSize(25, 25)
        self.emoBtn.setIconSize(QSize(25, 25))
        self.emoBtn.setIcon(QIcon('../images/emoji.png'))
        self.emoBtn.setStyleSheet('border:none')
        self.emoBtn.move(265, 460)
        self.emoBtn.hide()
        self.emojiPicker = EmojiPicker(self)
        self.emoBtn.clicked.connect(self.showEmojiPicker)

    def showEmojiPicker(self):
        print("打开表情窗口")
        buttonPos = self.emoBtn.mapToGlobal(QPoint(0, 0))
        newX = buttonPos.x()
        newY = buttonPos.y() - 330
        self.emojiPicker.move(newX, newY)
        if self.emojiPicker.isVisible():
            self.emojiPicker.hide()
        else:
            self.emojiPicker.show()

    def videoChat(self):
        if self.videoFd != None:
            box = QMessageBox(self)
            box.setText("您正在视频聊天中...")
            box.exec_()
            return
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
        # 1. 判断content前三个字符是否为em_
        if content[:3] == 'em_':
            # 2. 如果是，则创建一个标签控件，保存到msgLb
            msgLb = QLabel()
            # 3. 加载../images/emojis/下content图片，存到pixmap，设置给msgLb
            pixmap = QPixmap('../images/emojis/' + content)
            msgLb.setPixmap(pixmap)
        # 4. 否则，才显示文本
        else:
            # 5. 给下面5行代码添加一个缩进
            msgLb = QLabel(content)
            textWidth = msgLb.fontMetrics().width(content)
            if textWidth > 440:
                msgLb.setFixedWidth(440)
                msgLb.setWordWrap(True)
        if align == Qt.AlignRight:
            msgLb.setStyleSheet('background-color:#95ec69;border-radius:5px;padding:10px 5px;')
        else:
            msgLb.setStyleSheet('background-color:#ffffff;border-radius:5px;padding:10px 5px;')
        layout.addWidget(msgLb)
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
        self.emoBtn.show()
        if name == self.sender:
            self.videoBtn.hide()

    def setMsgList(self, name):
        msgLw = QListWidget()
        msgLw.setStyleSheet('border:none;border-top:1px solid gray')
        msgLw.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.msgLws[name] = msgLw
        self.layout.addWidget(msgLw, 1, 1)
        msgLw.hide()
