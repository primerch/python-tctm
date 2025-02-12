'''

这是我的授课思路：
为了让条件可控，我们采用下拉列表控件实现界面效果
下拉列表控件可以分成两部分
1.使用QComboBox()创建下拉列表框
2.使用addItems()方法批量添加选项
当用户变更下拉列表的选项时会触发currentIndexChanged事件
通过currentIndex()方法，可以获取当前选中的选项的索引值
这是我的代码
timeList = ['全部', '一周内', '两周内', '三周内', '四周内', '五周内', '六周内', '七周内', '八周内']
self.daysCmb = QComboBox()
self.daysCmb.addItems(timeList)
layout.addWidget(self.daysCmb, 0, 1)

请使用中文仿照以上内容出5道单选题，帮助学员理解如何在PyQt程序中使用下拉列表，不需要答案和解析

'''
