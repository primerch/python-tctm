from PyQt5.Qt import *

app = QApplication([])
window = QMainWindow()
window.setWindowTitle('计算器')
widget = QWidget()
window.setCentralWidget(widget)

# 1. 在widget中创建文本框

# 设置文本框只读

# 在widget中创建按钮并设置按钮文字为1


window.setFixedSize(400, 500)
window.show()
app.exec_()
