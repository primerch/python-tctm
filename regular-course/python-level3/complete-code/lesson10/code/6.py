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
    text = event.text()
    # 1.获取按键名
    key = event.key()
    if text in '0123456789+-*/.c=':
        ledit.setText(text)
    # 2.如果按下回车键，文本框显示等号
    elif key == Qt.Key_Enter or key == Qt.Key_Return:
        ledit.setText('=')


window.keyPressEvent = keypress

window.setFixedSize(400, 500)
window.show()
app.exec_()
