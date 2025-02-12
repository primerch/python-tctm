'''
在即时通信项目中实现私聊过程，现在要完成接收好友聊天消息，讲解步骤是这样的：
分析私聊过程客户端服务端工作：
客户端发消息时： 在文本框输入内容，点击发送按钮发送给服务端
服务端转发消息： 服务端收到客户端发送的聊天信息，找到要转发的客户端，将消息转发过去
客户端收消息时： 随时准备接收服务端发送过来的消息，并显示在消息列表中
问题：在哪里随时接收好友消息
解决：子线程收消息，发信号给主程序，主程序执行handle，在handle中执行各种操作
和收到登录或退出消息一样
问题： 我们怎么知道服务端给我们转发来的是聊天消息？还是登录消息或退出消息？
解决：分析消息内容的组成，收到消息，解析后msg字典结构
收到消息，解析后msg字典结构  {cmd:chat,content:内容，sender：发送者，to: 接受者}
cmd是cmd表示是聊天消息，content是聊天内容，sender是发来消息的好友名
问题 ： 聊天内容现在在控制台打印，应该显示在聊天列表中，但是每个好友都有消息列表控件，那本次收到的消息应该添加到
哪个好友的聊天消息列表中呢
解决： 消息是哪个好友发来的，就应该添加到哪个好友的消息列表控件中
问题： 如何查找好有对应的消息列表控件
解决：从消息控件字典中，用当前这条消息发送者好友名找到他对应的消息列表控件
问题： 如何把消息内容添加到消息列表控件中?
解决： 参考现实中的微信，最新的消息都是在底下，所以消息添加到消息列表最后
问题：将来发送的消息和收到的消息都要显示显示在消息列表，所以向消息列表中添加消息的操作可能反复使用
所以：为了方便将来复用，创建函数appendMsg, 专门用来向消息列表添加消息。当收到好友消息时要调用，放在
if msg['cmd'] == 'chat' 分支中
因为：消息超出屏幕出现右侧滚动条了，每次看最新的消息还要把滚动条拖动到下边，好麻烦
解决：增加一行代码，让每次添加消息后滚动条自动滚动到最底下
问题： 收到消息没有提醒
解决： 收到消息给好友增加小红点，并移动到好友列表最前面
步骤： 定义专门的drawIcon()方法，首先获得当前好友列表项中的QIcon图标，但是图标不能直接绘制修改，而要转换成
pixmap类型的像素位图才能绘制，画纸已经有了，就是原头像位图pixmap，接下来我们创建画笔QPainter，也要选择画笔颜色，
另外，我们不需要线条，只需要填充颜色，所以，把笔设置为无线条模式，然后，从指定左上角位置(30,0)开始，绘制椭圆，半径
为10；大家别忘了，用完画笔要收起来！最后，我们只要把绘制修改后的pixmap位图，重新创建为Qicon()图标，并设置给列表项
3.  每当收到新好友发来聊天消息时，都查找好友列表项，并调用drawIcon()方法，为头像图标添加小圆点
问题： 现在收到一个好友的消息这个好友就一直有小红点提示，就算看了还有提示
解决：查看消息后红点消失
步骤： 1. 获取当前选中项的好友名，2.好友登录时将好友头像添加到字典avatars保存只要用当前选中的好友名去字典中查找，
就知道这个好友之前用的哪个头像图片了3. 重新创建QIcon()，设置给当前选中的列表项就行了！

我的这部分的核心代码：
def handle(self, msg):
    if msg['cmd'] == 'login':
        avatar = msg['content']
        name = msg['sender']
        item = QListWidgetItem(QIcon('../images/avatar/' + avatar), name)
        self.fdList.insertItem(0, item)
        self.setMsgList(name)
        # 1. 将后登录好友的头像保存起来
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

def appendMsg(self, content, fd):
    item = QListWidgetItem(content)
    lw = self.msgLws[fd]
    lw.addItem(item)
    lw.scrollToBottom()
    fdItem = self.fdList.findItems(fd, Qt.MatchExactly)[0]
    # 3. 将当前好友取出移到最前面
    row = self.fdList.row(fdItem)
    self.fdList.takeItem(row)
    self.fdList.insertItem(0, fdItem)
    # 2. 如果消息不是正在聊天的好友发来的，才显示红点
    if self.nameLb.text() != fd:
        self.drawIcon(fdItem)
    else:
        # 4. 如果是正在聊天的好友，设置为选中状态
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

请根据以上内容帮我使用中文，根据以上知识点出5道单选题，主要考察：私聊过程中客户端服务端分别作什么，
列表项如何添加到列表控件最后，滚轮如何自动到底部，pyqt绘制红点主要步骤，如何取出列表项icon图标等，不需要答案.

'''
