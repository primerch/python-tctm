'''
我之前已经讲解完成了登录成功后切换到聊天窗口，现在讲解聊天窗口中显示好友列表，讲解步骤是这样的：
问题：客户端如何获取服务端保存的好友用户名和头像信息avatars字典
解决：通过服务端用JSON格式发送给客户端，然后客户端解析JSON格式数据提取字典
问题：点击登录后发现程序卡死
分析：消息打印发现，接收的消息内容很大，但是我只recv(1024),接收内容不够，但是不报错
      通过提问AI工具，建议我加try捕获错误信息，显示，发现是json解析报错
解决： 因为一次接收消息补全，不是JSON格式，所以使用json.loads函数无法解析，导致程序出错。
    可以将recv参数变大
问题 ：变为多大合适
解决 ：结合实际微信好友数量计算，变为1024*1000应该足够，解决了这个问题。
问题：好友信息有了，如何显示到聊天窗口
解决：使用QListWidget控件添加好友列表信息，显示头像和好友名字
问题：如何添加完成好友列表创建
解决： 1. 定义UI设置方法setUi（） 2. 添加元素到列表控件中，每个元素是一个好友
 3. 生成列表控件对象添加到窗口布局中的指定位置 4. init函数中调用UI设置 方法setUi（）
问题：如何在列表控件中添加好友信息
解决： 分3步：1.遍历avatars字典，得到每项的好友信息for username, avatar_path in avatars.items()
2. 将图片加载为图标对象icon = QIcon('../images/avatar/' + avatar)
3.为每个好友信息创建列表项，添加到列表控件中item = QListWidgetItem(icon，sender)  self.fdLw.insertItem(0, item)
至此完成了登录成功后显示出聊天窗口
问题： 图标大小不合适怎么办
解决：常见QSize对象规定大小，使用setIconSize设置图标大小
接下来就可以完成服务端发送好友列表信息：
在服务端的login方法中登录成功后，将avatars作为content内容，发送给客户端

这是我的客户端代码：
# 创建聊天窗口
def setUi(self):
        # 好友列表
        self.fdList= QListWidget()
        # 2. 设置列表所有项图标的大小，只需要设置一次即可，所以需要在方法外面书写
        self.fdLw.setIconSize(QSize(40, 40))
        self.layout.addWidget(self.fdLw, 1, 0, 2, 1)
        for account, avatar in self.users.items():
            item = QListWidgetItem(account)  # 先讲再封装
            self.fdLw.insertItem(0, item)
            # 1. 加载和设置图标
            icon = QIcon('../images/avatar/' + avatar)
            item.setIcon(icon)

这是我的服务端代码：
    def login(self, connSocket, req):
        ...
        # 1. 修改登录成功消息的内容为用户头像字典avatars
        msg = Message(req['cmd'], self.avatars, '服务器')
        self.sendMsg(connSocket, msg, 200)

请根据以上内容帮我使用中文，根据以上知识点出5道单选题，主要考察：如何解决接收消息过大的问题，
列表控件的使用，如何在列表控件中添加列表项，如何创建列表控件图标，如何设置图标大小等，不需要答案.

'''
