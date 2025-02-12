import threading
from PyQt5.Qt import *


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

    def appendMsg(self, content, fd):
        item = QListWidgetItem(content)
        lw = self.msgLws[fd]
        lw.addItem(item)
        lw.scrollToBottom()
        # 2. 从好友列表fdList中精确找到当前聊天好友对应的列表项fdItem

        # 3. 调用drawIcon方法，在fdItem的图标上绘制红点

    """
    我已经导入所需的模块，请使用pyqt5在列表项的图标右上角上绘制一个红色小圆，要求如下：
    1. 定义一个drawIcon实例方法和其参数item，传入列表项
    2. 获取item的图标icon，并创建icon的一个40x40的位图像pixmap
    3. 创建一个画笔painter，用于在pixmap这个位图上进行绘图
    4. 设置painter不绘制边框
    5. 设置painter的画刷颜色为红色'red'
    6. 在25,0的位置开始绘制一个15x15的圆
    7. 绘制完成后，结束画笔，并将pixmap作为新的图标设置给item
    请只输出drawIcon方法的代码，不要输出导入模块的代码
    """

    # 1.使用上述提示词生成drawIcon方法的代码

    def selectFriend(self, curItem):
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
