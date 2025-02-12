from PyQt5.Qt import *

app = QApplication([])
window = QMainWindow()
window.setWindowTitle('计算器')
widget = QWidget()
window.setCentralWidget(widget)

# 1. 在widget中创建文本框
ledit = QLineEdit(widget)
# 设置文本框只读
ledit.setReadOnly(True)
# 在widget中创建按钮并设置按钮文字为1
btn = QPushButton('1', widget)

window.setFixedSize(400, 500)
window.show()
app.exec_()
