from PyQt5.Qt import *

app = QApplication([])
window = QMainWindow()
window.setWindowTitle("计算器")
widget = QWidget()
window.setCentralWidget(widget)
layout = QGridLayout()
widget.setLayout(layout)
ledit = QLineEdit()
ledit.setReadOnly(True)
layout.addWidget(ledit, 0, 0, 1, 4)

btns = [
    ['7', '8', '9', '+'],
    ['4', '5', '6', '-'],
    ['1', '2', '3', '*'],
    ['.', '0', '=', '/'],
    ['c'],
]


# 1. 定义事件处理函数
def btn_click():
    print('别点了，别点了')


for r in range(len(btns)):
    row = btns[r]
    for c in range(len(row)):
        btn = QPushButton(btns[r][c])
        layout.addWidget(btn, r + 1, c)
        # 2.为创建好的按钮绑定点击事件
        btn.clicked.connect(btn_click)

window.setFixedSize(400, 500)
window.show()
app.exec_()
