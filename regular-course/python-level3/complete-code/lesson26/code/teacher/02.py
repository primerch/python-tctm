'''
在即时通信项目中要实现私聊过程，现在完成发送聊天消息给好友，讲解步骤是这样的：
分析私聊过程客户端服务端工作：
问题：如何获取文本框中的内容
解决：我们之前在登录时因为只需要输入用户名，使用的文本输入框是QLineEdit。但是聊天内容可能比较多，
一行不够，所以我们再这里使用的是多行文本输入框：QTextEdit。读取内容是，QLineEdit使用 text（）方法，
QTextEdit使用toPlainText()。所以：content = self.msgTxt.toPlainText()
问题： 消息发给谁？
解决：接下来，发件人就是self.sender，要发给谁，收件人to就是label标签里正在聊天的好友人，调
用sendMsg方法把消息对象发送出去
问题 ： 发送完消息，文本框内容还在
解决： 加上文本框.clear()方法，每次发送消息都能自动清空文本框了
问题： 如何防止发送空消息
解决：对内容字符串增加一个strip()方法，先去掉内容两侧的空格。然后发送消息前增加if判断content不能为空
问题： 发送的消息也需要显示到列表控件?
解决： 同样调用appendMsg添加
问题：所有消息都在左侧，分不出哪些是收的，哪些是发送的
解决：增加对齐方式，收到的消息默认左对齐，发送的消息传入Qt.AlignRight右对齐
问题： 正在聊天的好友退出了，但是聊天界面还在，还能给好友发消息，导致程序报错
解决： 先判断退出的好友，是不是正在和我聊天的好友（如果不是好友在列表中消失，自然不能聊天了）
如果是现有一个弹窗提示
box = QMessageBox(self)
box.setText(name + "退出了")
box.exec_()
然后删除好友的聊天列表控件用close方法。好友名标签不隐藏只清空。隐藏文本框和按钮

我的这部分的核心代码：
def handle(self, msg):
        if msg['cmd'] == 'login':
            ...
        elif msg['cmd'] == 'quit':
            name = msg['content']
            item = self.fdList.findItems(name, Qt.MatchExactly)[0]
            index = self.fdList.row(item)
            self.fdList.takeItem(index)
            #1 如果是正聊天好友关闭聊天列表
            if name == self.nameLb.text():
                # 2.提示好友退出
                box = QMessageBox(self)
                box.setText(name + "退出了")
                box.exec_()
                # 3.关闭消息窗口
                self.msgLws[name].close()
                # 4.隐藏姓名输入框和按钮
                self.nameLb.setText('')
                self.msgTxt.hide()
                self.sendBtn.hide()

def btnSend(self):
        content = self.msgTxt.toPlainText().strip()
        if content:
            to = self.nameLb.text()
            msg = Message('chat', content, self.sender, to)
            self.client.sendMsg(msg)
            # 3.将发送消息添加到列表控件中
            self.appendMsg(content, to, Qt.AlignRight)
        self.msgTxt.clear()


    # 1. 增加对齐方式参数，默认为左对齐
    def appendMsg(self, content, fd, align = Qt.AlignLeft):
        item = QListWidgetItem(content)
        # 2. 设置对齐方式
        item.setTextAlignment(align)
        lw = self.msgLws[fd]
        lw.addItem(item)
        lw.scrollToBottom()
        fdItem = self.fdList.findItems(fd, Qt.MatchExactly)[0]
        self.fdList.insertItem(0, fdItem)
        # 2. 如果消息不是正在聊天的好友发来的，才显示红点
        if self.nameLb.text() != fd:
            self.drawIcon(fdItem)

请根据以上内容帮我使用中文，根据以上知识点出5道单选题，主要考察：如何获取多行文本框中的内容，
如何将发送消息添加到列表控件中和接收消息左右区分，好友退出如何设置弹窗，好友退出需要做哪些操作，
关闭销毁列表控件的方法等知识，不需要答案.

'''
