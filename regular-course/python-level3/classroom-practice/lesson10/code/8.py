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


def calc(text):
    curr = ledit.text()
    # 1. 输入等号计算并显示结果

    # 2. 输入 c ，清空文本框

    # 3. 其他情况，拼接字符串
    new = curr + text

    ledit.setText(new)


def btn_click():
    btn = window.sender()
    text = btn.text()
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
    if key == Qt.Key_Enter or key == Qt.Key_Return:
        calc('=')
    elif text in '0123456789+-*/.c=':
        calc(text)


window.keyPressEvent = keypress
window.setFixedSize(400, 500)
window.show()
app.exec_()
