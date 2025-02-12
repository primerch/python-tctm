from PyQt5.Qt import *

app = QApplication([])
window = QMainWindow()
window.setWindowTitle('计算器')
widget = QWidget()

layout = QGridLayout()
widget.setLayout(layout)
ledit = QLineEdit()
ledit.setReadOnly(True)
layout.addWidget(ledit, 0, 0, 1, 4)

# 老师为你准备好了二维列表，其中按计算器按钮布局保存了按钮的文字
btns = [
    ['7', '8', '9', '+'],
    ['4', '5', '6', '-'],
    ['1', '2', '3', '*'],
    ['.', '0', '=', '/'],
    ['c'],
]
# 1. 根据二维列表的长度进行遍历
for r in range(len(btns)):
    # 获取当前行数据保存到变量row中
    row = btns[r]
    # 再根据当前行数据的长度进行遍历
    for c in range(len(row)):
        # 2. 每取出列表中一个文字，就创建一个按钮，把文字设置为按钮的文本
        btn = QPushButton(btns[r][c])
        # 3. 避开文本框，将按钮添加到布局中
        layout.addWidget(btn, r + 1, c)

window.setCentralWidget(widget)
window.setFixedSize(400, 500)
window.show()
app.exec_()
