'''
接下来在聊天项目中给学生讲解从好友列表实时删除退出用户，讲解步骤是这样的：
现在当一位好友退出后，在其他人的好友列表中还显示该好友在线
应该和新的好友登录相反，如果有好友退出时，也应该马上从其他人的好友列表中消失
分为2步：1. 用户断开连接，服务端删除用户信息后，将退出用户信息群发给其他客户端；
2. 其他客户端收到用户退出消息，并将好友从列表中删除
问题：客户端窗口如何知道好友退出
解答：我们已经实现了循环接收服务员发送的一切消息，以及判断消息类型，执行对应操作，所以在getMsg中增加分支当收到信息cmd
类型是退出时表示服务端发送的是有用户退出的信息。解析还有退出时其他客户端从服务端收到的消息：cmd : quit 表示这是服务端发
送的用户退出的信息；那么在聊天界面如何从好友列表删除用户信息？分为3步：
1. 列表控件中查找出要删除的好友列表项item = self.fdLw.findItems(name，Qt.MatchExactly)[0]
2. 获取列表项在列表控件中的索引号index = self.fdLw.row(item)
3. 从列表控件中删除对应所有号的列表项self.fdLw.takeItem(index)
接下来讲解服务端操：
有用户退出和新用户登录不同，新用户登录会向服务端发送登录信息，服务端转发即可，但是用户退出不会向服务端发任何消息，
所以服务端群发需要自己创建消息对象。发送纤细就是上面分析过的cmd : quit ，content: name，sender : ‘服务器’ ，to : None
用户退出消息应该群发给出了自己之外的所有其他用户，所以在原quit方法中，在connSockets和avatars字典中删除用户信息之后，
再遍历连接socket字典，发送消息给所有其他客户端，就不会发送给自己了

我的客户端核心代码是：
def getMsg(self):
    ...
    if msg['cmd'] == 'login':
            ...

    # 2. 判断消息命令是否为退出，如果删除好友
    elif msg['cmd'] == 'quit':
         name = msg['content']
         item = self.fdLw.findItems(name)[0]
         index = self.fdLw.row(item)
        self.fdLw.takeItem(index)


服务端核心代码是：
def quit(self, connSocket):
   ...

    msg = Message('quit', name, '服务器')
    for skt in Server.clients.values():
       self.sendMsg(skt, msg, 200)

请根据以上内容帮我使用中文，根据以上知识点出5道单选题，主要考察：有用户退出后服务端客户端应该做的操作，
如何从好友列表控件中删除一项的具体步骤和函数使用，服务端发送的有用户退出的消息包含的数据几项，
findItems的MatchExactly参数，字典的values函数功能等，不需要答案.

'''
