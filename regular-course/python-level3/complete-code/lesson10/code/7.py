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
ledit.setAlignment(Qt.AlignRight)
layout.addWidget(ledit, 0, 0, 1, 4)
btns = [
    ['7', '8', '9', '+'],
    ['4', '5', '6', '-'],
    ['1', '2', '3', '*'],
    ['.', '0', '=', '/'],
    ['c'],
]


# 1.定义计算函数
def calc(text):
    # 用变量保存当前文本
    curr = ledit.text()
    # 拼接新文本到变量
    new = curr + text
    # 显示文本到文本框
    ledit.setText(new)


def btn_click():
    btn = window.sender()
    text = btn.text()
    # 2.将ledit.setText()方法替换为calc()方法，参数不变
    calc(text)


for r in range(len(btns)):
    row = btns[r]
    for c in range(len(row)):
        btn = QPushButton(btns[r][c])
        layout.addWidget(btn, r + 1, c)
        btn.clicked.connect(btn_click)


def keypress(event):
    key = event.key()
    text = event.text()
    # 3. 将ledit.setText()方法替换为calc()方法，参数不变
    if text in '0123456789+-*/.c=':
        calc(text)
    # 4. 将ledit.setText()方法替换为calc()方法，参数不变
    elif key == Qt.Key_Enter or key == Qt.Key_Return:
        calc('=')


window.keyPressEvent = keypress
window.setFixedSize(400, 500)
window.show()
app.exec_()
