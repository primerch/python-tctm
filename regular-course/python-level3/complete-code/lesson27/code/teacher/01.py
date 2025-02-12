'''
在即时通信项目中在列表控件中显示聊天消息，现在要进行消息样式美化，讲解步骤是这样的：
问题：都需要加哪些效果样式效果
解决：1. 给消息增加背景颜色，并且背景颜色设置圆角；2. 消息之间设置间距
问题：每个item是一条消息，给每个消息控件项item设置样式，但是设置方式太少，不能满足要求？
解决：使用Widget代替item中原本的纯文本内容才能设置样式
问题 ：什么是Widget
解决： 就像乐高的底板，不但可以作为整个子窗口的底板，也可以作为窗口中局部区域的底板，就像一个大的乐高积木场景
中，整个场景要有一个大的底板。而场景中的每个建筑，也都会有自己专属的小底板。只要pyqt自带控件无法满足我们的样
式和功能需求时，我们都可以使用widget来定制个性化的控件
问题： 如何使用widget来自定义控件呢？
解决：1.直接用QWidget创建底板对象，然后加入到列表项item中widget = QWidget()
不过因为现实聊天消息都没有边框，所以我们的widget也直接设置无边框widget.setStyleSheet('border:none;')
2.每一条聊天消息widget中，只有一个label控件用于显示消息内容. 所以widget使用水平布局
2.1 专门控制一行中的控件位置和大小的布局；2.2自动根据内容适配大小，不用计算宽高；
2.3自带外间距，不用计算，甚至不用设置
2.4 只需要alignleft或alignright就可以设置左右对齐，不需要具体数值
3. 只需要一个label控件，但是label控件需要设置内容，样式，位置msgLb = QLabel(content)
背景色：呈现的颜色，属性background-color；圆角：设置圆弧半径，border-radius；内边距 ： label中文字与label边
界之间的距离，padding，两个值第一个是上下，第二个是左右。如果居左背景居做背景色为白色，如果居右背景色为绿色
4. widget不是加入主窗口了，而是只加到一个列表项item中lw.setItemWidget(item, widget)
问题：消息列表控件中不显示列表项
原因：默认item大小为0，放不下widget，设置item大小，自动适应widget大小item.setSizeHint(widget.sizeHint())
layout = QHBoxLayout()
widget.setLayout(layout)

我的这部分的核心代码：
def appendMsg(self, content, fd, align=Qt.AlignLeft):
        # 1.删除列表项内容content
        item = QListWidgetItem()
        lw = self.msgLws[fd]
        lw.addItem(item)

        # 2. 自定义widget
        widget = QWidget()
        widget.setStyleSheet('border:none;')
        # 3. 设置窗口为水平布局和对齐方式，添加到widget中
        layout = QHBoxLayout()
        layout.setAlignment(align)
        widget.setLayout(layout)
        # 4. 设置文本控件和样式，并布局中添加文本控件
        msgLb = QLabel(content)
        if align == Qt.AlignRight:
            msgLb.setStyleSheet('background-color:#95ec69;border-radius:5px;padding:10px 5px;')
        else:
            msgLb.setStyleSheet('background-color:#ffffff;border-radius:5px;padding:10px 5px;')
        layout.addWidget(msgLb)

        # 6. 设置item大小就是widget大小
        item.setSizeHint(widget.sizeHint())
        # 5. widget加到一个列表项item中
        lw.setItemWidget(item, widget)

        lw.scrollToBottom()
        fdItem = self.fdList.findItems(fd, Qt.MatchExactly)[0]
        row = self.fdList.row(fdItem)
        self.fdList.takeItem(row)
        self.fdList.insertItem(0, fdItem)
        if self.nameLb.text() != fd:
            self.drawIcon(fdItem)
        else:
            self.fdList.setCurrentItem(fdItem)

请根据以上内容帮我使用中文，根据以上知识点出5道单选题，主要考察：QWidget使用，水平布局用法和特点，
Qlabel设置样式方法，使用什么方式能给列表项设置自定义样式，如何在item中添加Widget等知识，不需要答案.

'''
