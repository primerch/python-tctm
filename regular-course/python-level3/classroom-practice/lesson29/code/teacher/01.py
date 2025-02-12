'''
在给学生讲解即时通信项目的视频聊天功能中，当对方请求视频聊天时需要接收方有提示框进行选择，我的讲解思路是：
问题：现在视频聊天请求方一请求，接收方自动弹出视频聊天窗口不合理
解决：参考现实中的微信，可以在收到视频聊天请求时，出现一个消息提示框，让视频接受者选择是否接通视频聊天
问题：如何添加消息提示框，在哪添加？
解决：因为：只有收到对方视频聊天请求时才需要出现是否接受的消息提示框，所以：应该在收到视频消息，并且content=call
时出现是否接收的消息提示框。步骤： 1. 创建message box控件self.box = QMessageBox(self)
2.添加控件标题提示谁像你发起了视频聊天self.box.setText(msg['sender'] + "向你发起视频聊天")
3.设置box两个按钮，一个是接听按钮，一个是挂断按钮，并返回按钮的实例对象
self.box.addButton("接听") self.box.addButton("挂断")
4.弹出box弹窗self.box.exec_()
问题 ：程序怎么知道用户是选择了接收还是挂断
解决： 1.在添加按钮时，用第二个参数指定点击按钮要返回的结果，而且QMessageBox已有备选项
self.box.addButton("接听", QMessageBox.AcceptRole)  self.box.addButton("挂断", QMessageBox.RejectRole)
2.exec_()不仅是等待用户点击，还能返回用户点击不同按钮返回的不同结果。所以我们要用变量result接住exec_()方法的
返回值QMessageBox.AcceptRole或QMessageBox.RejectRole 表示接受或者拒绝视频聊天，然后通过if判断，完成各自的操作

主要代码是：
class ChatWindow(QWidget):
    def __init__(self, sender, client, avatars):
        # 1. 设置box属性 保存提示框
        self.box = None

   def handle(self, msg):
       ...
          elif content == 'call':
                # 2. 添加提示框，等待用户选择
                self.box = QMessageBox(self)
                self.box.setText(msg['sender'] + "向你发起视频聊天")
                self.box.addButton("接听", QMessageBox.AcceptRole)
                self.box.addButton("挂断", QMessageBox.RejectRole)
                result = self.box.exec_()
                # 3.如果用户接听，才创建视频窗口
                if result == QMessageBox.AcceptRole:
                    self.videoWindow = VideoWindow(self, msg['sender'], msg['to'])
                    self.videoFd = msg['sender']

然后还要讲解如何获取摄像头和麦克风权限，讲解思路是
问题： 现在已经打开视频窗口了，但是两个方块都是黑的，怎么样才能看到画面进行视频聊天呢
原因：因为摄像头和麦克风设计个人隐私，所以需要更严格的安全防范，在程序中需要用程序获得计算机的摄像头和麦克风权限，
才能进行视频聊天启
问题：如何在程序中获取获取摄像头麦克风权限？
讲解：不是所有的网页都需要获取摄像头麦克风权限。比如普通新闻网页，购物网页等只需要看的网页都不需要。
只有当QWebEngineView控件要加载的网页需要用到摄像头麦克风时才会自动申请权限
步骤： 1. 需要提前定义处理函数，在函数中获取网页加载时申请的权限；2.将申请权限的函数绑在专门的事件上

我的这部分的核心代码：
class VideoWindow(QWidget):
    def __init__(self, sender, to):
        super().__init__()
        ...
        self.browser = QWebEngineView()
        # 2 获取视频音频权限
        self.browser.page().featurePermissionRequested.connect(self.getPermission)
        self.browser.setUrl(QUrl(f"https://tcim.61it.cn/python.html"))
        layout.addWidget(self.browser)

    # 1 获取视频音频权限
    def getPermission(self, url, feature):
        self.browser.page().setFeaturePermission(url, feature, QWebEnginePage.PermissionGrantedByUser)

请根据以上内容帮我使用中文，根据以上知识点出5道单选题，主要考察：创建提示框的步骤，如何窗口带有2个按钮的提示框，
如何知道用户点击了提示框的接受按钮还是挂断，为什么视频聊天需要获取权限才能进行，如何获取摄像头麦克风权限，等知识，
不需要答案.

'''
