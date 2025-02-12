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
        """
        
        我已经使用pyqt5编写了简单的聊天界面，并且导入了所有必要的模块，只需要你实现下面的功能：
        1. 创建一个标签，来显示正在聊天的好友昵称，存储到self.nameLb。
        设置它的宽高固定为550x60，左侧内边距padding-left为10px，文本内容为"好友昵称"。
        添加到网格布局self.layout的第0行，第1列，占据1行1列。
        2. 创建一个文本编辑框，用于输入消息，存储到self.msgTxt
        设置它的高度固定为145，只有顶部有1px的灰色边框，其他没有边框。
        添加到网格布局self.layout的第2行，第1列，占据1行1列。
        3. 创建一个按钮，用于发送消息，存储到self.sendBtn。
        添加到聊天界面self上的固定位置(685, 555)，设置文本内容为"发送",设置其父窗口为self
        只需要输出要求的代码
        
        """
        # 1. 使用上述提示词生成聊天界面右侧所需控件
        # 创建标签来显示正在聊天的好友昵称
        self.nameLb = QLabel("好友昵称", self)
        self.nameLb.setFixedSize(550, 60)
        self.nameLb.setStyleSheet("padding-left:10px;")
        self.layout.addWidget(self.nameLb, 0, 1, 1, 1)

        # 创建文本编辑框用于输入消息
        self.msgTxt = QTextEdit(self)
        self.msgTxt.setFixedHeight(145)
        self.msgTxt.setStyleSheet("border-top:1px solid gray; border-right:none; border-left:none; border-bottom:none;")
        self.layout.addWidget(self.msgTxt, 2, 1, 1, 1)

        # 创建按钮用于发送消息
        self.sendBtn = QPushButton("发送", self)
        self.sendBtn.move(685, 555)
