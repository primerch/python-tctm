from PyQt5.Qt import *

app = QApplication([])
window = QMainWindow()

# 设置窗口标题
window.setWindowTitle('计算器')
# 设置窗口固定大小
window.setFixedSize(400, 500)

window.show()
app.exec_()
