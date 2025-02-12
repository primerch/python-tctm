'''
第一段提示词：

很多聊天程序为什么要限制用户在多个地点同时登录？请为我通俗的说一下。

'''

'''
第二段提示词：

这是我服务端保存用户登录信息的代码：
    def login(self, cSocket, req):
        account = req['account']
        Server.clients[account] = cSocket
        Server.users[account] = 'boy.png'

        msg = Message(req['cmd'], Server.users, '服务器')
        self.sendMsg(cSocket, msg, 200)
但是当一个用户登录后，在另外一台计算机还能登录，并提示登录成功，这是什么原因，应该如何解决？

'''
