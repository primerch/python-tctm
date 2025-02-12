'''
现在我的登录代码是这样的：
class loginWindow:

   def login(self):
       .....
       if code == 200:
            self.resultLable.setText('登录成功')
            # 1. 隐藏登录窗口
            lgWindow.hide()
            chatWindow = ChatWindow(sender, msg['content'], client)
            chatWindow.show()
        elif code == 401:
            self.resultLable.setText('该用户已登陆')
但是登录成功以后，聊天界面出现一下就马上消失了。
原因是什么，为我提供几种简单的解决方法，并说下每种方法的优劣？

'''
