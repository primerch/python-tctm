'''

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
btns = [
    ['7', '8', '9', '+'],
    ['4', '5', '6', '-'],
    ['1', '2', '3', '*'],
    ['.', '0', '=', '/'],
    ['c'],
]
for r in range(len(btns)):
    row = btns[r]
    for c in range(len(row)):
        btn = QPushButton(btns[r][c])
        layout.addWidget(btn, r+1, c)
window.setCentralWidget(widget)
window.setFixedSize(400, 500)
window.show()
app.exec_()

以上是我的代码，请帮我梳理其中有关PyQt的知识点，以最精简的方式返回结果

'''

'''
追问：

我想知道我该如何使用这些知识点，比如我想创建一个窗口，应该用什么？这些知识点还能帮我做其它的什么功能？

'''
