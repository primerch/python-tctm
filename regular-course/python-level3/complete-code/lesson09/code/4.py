from PyQt5.Qt import *

app = QApplication([])
window = QMainWindow()
window.setWindowTitle('计算器')

# 1. 创建widget对象
widget = QWidget()
# 设置widget的背景颜色和要绘制的图片(将来如不需要，可省略)
widget.setStyleSheet(
    'background: gray url(images/kn.png)'
)
# 2. 将widget放入窗口中
window.setCentralWidget(widget)

window.setFixedSize(400, 500)
window.show()
app.exec_()
