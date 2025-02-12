'''
我想在生成的计算器界面中点击按钮可以获取按钮文本
问题：在计算器界面如何点击按钮获取按钮文本
解决：为按钮绑定点击鼠标事件获取按钮文本
问题：用鼠标点来点去非常的麻烦
解决：绑定按下键盘事件，用按键盘代替点鼠标

这是我的授课代码：

# 定义点击鼠标事件处理函数
def btn_click():
    btn = window.sender()
    text = btn.text()
    print(text)

for r in range(len(btns)):
    row = btns[r]
    for c in range(len(row)):
        btn = QPushButton(btns[r][c])
        layout.addWidget(btn, r+1, c)
        # 关联事件处理函数
        btn.clicked.connect(btn_click)

# 定义按下键盘事件处理函数
def keypress(event):
    text = event.text()
    print(text)

# 关联事件处理函数
window.keyPressEvent = keypress

请帮我使用中文，根据以上内容出5道单选题，帮助学员理解和消化点击按钮事件和按下键盘事件概念，不需要答案。
'''
