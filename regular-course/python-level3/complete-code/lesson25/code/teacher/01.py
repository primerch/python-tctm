'''
在聊天项目中已经已经使用pyqt创建好了聊天区域，现在要完成选择好友显示与好友的聊天消息，讲解步骤是这样的：
问题： 如何知道鼠标选择了好友列表中的哪位好友
解决：使用事件绑定函数，给好友列表控件添加点击事件。self.fdLw.itemClicked.connect(self.selectFriend)
问题：在哪设置事件绑定函数
解决： 因为要在聊天界面显示之后才有好友列表控件，所以可以放在setUi方法最后
问题：如何在selectFriend中知道选择了哪位好友
解决：需要先知道选择了哪个聊天好友，为事件处理函数添加curItem形参 自动获得选中的列表控件项
问题： 每个好友的聊天消息如何保存
解决： 给每个好友直接保存一个聊天消息列表控件，那每切换一个好友只需要控制消息列表控件显示隐藏就可以了
保存方式： 用每个好友姓名为键，对应的聊天列表控件为值   {姓名: 聊天列表控件 .......}
保存方法： 分3步实现  1. 创建字典，保存与每个好友的聊天消息的列表控件·；2. 定义函数，为每个好友创建聊天消息
列表控件，并设置样式；3. 将创建的消息列表控件添加到字典中
问题 ： 何时调用setMsgList函数为每个好友创建专属的聊天消息列表控件呢
解决 ： 因为：每个好友都需要有自己的消息列表控件，所以：在初始加载已登录好友和收到新好友登录时都需要使用
setMsgList为好友创建消息列表控件
问题：消息列表控件在控制台打印，但是不显示在界面上。在setMsgList()方法中创建消息列表控件后，应该把消息列表
控件放在布局中哪个位置?
解决：应该从1行1列格子开始，占一行一列self.layout.addWidget(self.msgLw, 1, 1)
问题： 什么时候显示好友的消息列表控件呢
解决： 因为：页面加载时，没有选择好友，不知道跟谁聊天，所以聊天区域和文本框，发送按钮一样暂时隐藏。都是应该
在选择好友后，确定跟谁聊天才显示
1.setMsgList中把每个消息放入布局之后，立刻隐藏 ；，2.在selectFriend方法中,让选中的好友，对应的消息列表控件
显示出来。然后添加一些测试消息
问题：当切换好友时有问题：第一次选童童能正常显示和他的聊天消息，但是选择小派后再选择童童，只有用户名变成童童，
聊天消息却还是和小派的，变不回来
解决：pyqt中规定，在同一个布局空间中，后添加的控件会放在先添加空间的上层，且同一个控件添加后所在的层就不会变。
切换好友时，如果第一次选择某一位好友，执行 addWidget，在窗口添加消息列表控件。因为所有消息列表控件放在窗口布
局中的相同的位置，所以show后添加的列表控件会在最上层，所以看到的就是新选择的好友的消息列表控件。但是当切换好友
后，第二次选择某一位好友。因为这位好友的消息列表控件已经添加过了，且所在的层不会变，被覆盖到下边所以看不到。
解决：每次选择新的好友时，都将现在正显示的好友消息列表控件隐藏掉，这样每次选择聊天好友后，消息列表显示区域就只
有一个消息列表控件，就是新选择的好友的消息列表控件。也就不会被覆盖住了
问题：如何知道选择新好友时，之前显示的好友消息列表控件是哪一个？
解决：nameLb中保存在现在正显示的好友的用户名，用用户名可以去消息列表字典中获取好友对应的，正在显示的消息列表控件
问题：运行程序发现，现在不但问题没解决，第一次选中一个好友程序就卡死，出错退出了
解决：因为点击第一个好友之前，根本内有前一个选中的好友，也就无法从文本框中获取前一个用户名，没有用户名就强行从
字典中读取，程序就会报错，增加一个if判断，只有current有值，不为空，才有必要从字典中读取列表控件，并隐藏

我的这部分的核心代码：
class ChatWindow(QWidget):
    def __init__(self, sender, client, avatars):
        .....
        # 定义消息列表字典
        self.msgLws = {}
        self.setUi()
        t = threading.Thread(target=self.getMsg, daemon=True)
        t.start()

    def getMsg(self):
        ...

    def setUi(self):
        self.fdList = QListWidget()
        self.layout.addWidget(self.fdList, 0, 0, 3, 1)
        self.fdList.setIconSize(QSize(40, 40))
        for name, avatar in self.avatars.items():
            item = QListWidgetItem(QIcon('../images/avatar/' + avatar), name)
            self.fdList.insertItem(0, item)
            self.setMsgList(name)
        ...
        # 绑定点击好友时对应的处理函数
        self.fdList.itemClicked.connect(self.selectFriend)

    # 定义选择好友后的处理函数
    def selectFriend(self,curItem):
        self.msgTxt.show()
        self.sendBtn.show()
        # 1. 获取之前选中的好友名
        pre = self.nameLb.text()
        # 2. 如果好友名存在，就隐藏之前好友的消息列表控件
        if pre:
            self.msgLws[pre].hide()
        name = curItem.text()
        self.nameLb.setText(name)
        # 获取新选择的好友对应的聊天列表控件，并显示出来
        self.msgLws[name].show()

    # 定义创建消息列表控件函数
    def setMsgList(self, name):
        msgLw = QListWidget()
        msgLw.setStyleSheet('border:none;border-top:1px solid gray')
        self.msgLws[name] = msgLw

        # 将聊天列表控件加入到布局中，先设置为隐藏
        self.layout.addWidget(msgLw, 1, 1)
        msgLw.hide()
        item = QListWidgetItem(name + "的消息列表")
        msgLw.insertItem(0, item)

请根据以上内容帮我使用中文，根据以上知识点出5道单选题，主要考察：列表控件点击事件使用方法，如何获取鼠标点击
的列表项内容，同一位置方多个列表控件的显示规则，同一位置方多个列表控件如何切换显示，为每个用户保存消息的方法
等，不需要答案.

'''
