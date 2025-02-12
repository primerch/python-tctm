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


def btn_click():
    btn = window.sender()
    text = btn.text()
    ledit.setText(text)


for r in range(len(btns)):
    row = btns[r]
    for c in range(len(row)):
        btn = QPushButton(btns[r][c])
        layout.addWidget(btn, r + 1, c)
        btn.clicked.connect(btn_click)


def keypress(event):
    print('别按了')
    # 1. 获取按键文本
    text = event.text()
    # 2. 限制用户只能输入以下文本
    if text in '0123456789+-*/.c=':
        ledit.setText(text)


window.keyPressEvent = keypress

window.setFixedSize(400, 500)
window.show()
app.exec_()
