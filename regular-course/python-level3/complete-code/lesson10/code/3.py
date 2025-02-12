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
# 4. 为文本框设置文本右对齐
ledit.setAlignment(Qt.AlignRight)
btns = [
    ['7', '8', '9', '+'],
    ['4', '5', '6', '-'],
    ['1', '2', '3', '*'],
    ['.', '0', '=', '/'],
    ['c'],
]


def btn_click():
    # 1.获取当前被点击的按钮
    btn = window.sender()
    # 2.获取该按钮的文本
    text = btn.text()
    # 3.将文本显示在文本框
    ledit.setText(text)


for r in range(len(btns)):
    row = btns[r]
    for c in range(len(row)):
        btn = QPushButton(btns[r][c])
        layout.addWidget(btn, r + 1, c)
        btn.clicked.connect(btn_click)

window.setFixedSize(400, 500)
window.show()
app.exec_()
