from PyQt5.Qt import *

app = QApplication([])
window = QMainWindow()
window.setWindowTitle('计算器')
widget = QWidget()
window.setCentralWidget(widget)
ledit = QLineEdit()
ledit.setReadOnly(True)
btn = QPushButton("1")

# 1. 创建布局，将布局添加到widget中
layout = QGridLayout()
widget.setLayout(layout)
# 2. 将文本框和按钮依次添加到布局中的指定位置
layout.addWidget(ledit, 0, 0, 1, 4)
layout.addWidget(btn, 1, 0)

window.setFixedSize(400, 500)
window.show()
app.exec_()
