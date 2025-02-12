'''
我用Pyqt5库中的类创建了一个计算器应用程序窗口
问题：能不能直接把按钮显示在窗口中
解决：需要先在窗口中放置Widget，再在Widget中添加其他内容
问题：创建的按钮控件都堆在了左上角，如何摆放在固定行列位置
解决：使用布局来控制按钮控件在窗口的位置

这是我的授课代码：
from PyQt5.Qt import *

app = QApplication([])
window = QMainWindow()
window.setWindowTitle('计算器')
widget = QWidget()
window.setCentralWidget(widget)
btn = QPushButton("1")
layout = QGridLayout()
widget.setLayout(layout)
layout.addWidget(btn, 1, 0)

window.setFixedSize(400, 500)
window.show()
app.exec_()

请帮我使用中文，根据以上内容出5道单选题，帮助学员理解和消化Pyqt应用程序对象，窗口
及Widget，布局的概念，不需要答案。
'''
