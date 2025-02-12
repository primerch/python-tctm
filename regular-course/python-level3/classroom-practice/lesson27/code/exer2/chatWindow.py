import sys
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
        # t = threading.Thread(target=self.getMsg, daemon=True)
        # t.start()

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
        self.sendBtn.clicked.connect(self.btnSend)

    def btnSend(self):
        content = self.msgTxt.toPlainText().strip()
        if content:
            to = self.nameLb.text()
            msg = Message('chat', content, self.sender, to)
            # self.client.sendMsg(msg)
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
        # 1. 获取msgLb的文字内容content的宽度textWidth

        # 2. 如果文字宽度超过440则设置msgLb固定宽度为440并自动换行

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

    def setMsgList(self, name):
        msgLw = QListWidget()
        msgLw.setStyleSheet('border:none;border-top:1px solid gray')
        # 3. 设置msgLw的垂直滚动模式为像素滚动

        self.msgLws[name] = msgLw
        self.layout.addWidget(msgLw, 1, 1)
        msgLw.hide()


if __name__ == '__main__':
    app = QApplication([])
    chatWindow = ChatWindow('小派', None, {'小派': '0.jpg'})
    chatWindow.show()
    chatWindow.appendMsg('童童，我使用AI小助手查了一下如何使用Python来实现视频通话', '小派', Qt.AlignLeft)
    chatWindow.appendMsg('首先，我们需要处理视频。视频其实就是一系列连续的图片，这些图片被称为帧。'
                         '我们可以使用一个名为opencv-python的库来处理这些帧。'
                         'opencv-python是一个非常强大的图像处理库，'
                         '它可以帮助我们从摄像头中捕获每一帧图片，并且提供了许多工具来处理这些图片。'
                         '比如，我们可以调整图片的大小，颜色等等，甚至可以对图片进行一些复杂的操作，'
                         '比如特征提取，物体检测等等。在我们的视频通话应用中，'
                         '我们主要会用到opencv-python捕获帧和压缩帧的功能，以便更快地通过网络发送。', '小派',
                         Qt.AlignLeft)
    chatWindow.appendMsg('接下来，我们需要处理音频。音频是我们在通话中说话的声音。'
                         '我们可以使用一个名为sounddevice的库来处理这些声音。'
                         'sounddevice是一个非常强大的音频处理库，它可以帮助我们从麦克风中捕获声音，'
                         '并且提供了许多工具来处理这些声音。比如，我们可以调整声音的音量，音调等等，'
                         '甚至可以对声音进行一些复杂的操作，比如噪声消除，回声消除等等。'
                         '在我们的视频通话应用中，我们主要会用到sounddevice捕获声音和压缩声音的功能，'
                         '以便更快地通过网络发送。', '小派', Qt.AlignLeft)
    chatWindow.appendMsg('然后，我们需要将处理过的视频和音频数据通过我们创建的socket服务器发送出去。'
                         '这个过程就像是我们把处理过的图片和声音放进信封，然后通过邮局发送出去。'
                         '接收方（也就是我们通话的另一方）就可以收到这些数据，然后解码，'
                         '就可以看到视频和听到声音了。', '小派', Qt.AlignLeft)
    chatWindow.appendMsg('童童，这确实很复杂，但我想我们可以做到。让我们开始试试吧！', '小派', Qt.AlignLeft)

    app.exec_()
