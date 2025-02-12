'''
在上一道题目生成的窗口中实现
点击按钮时，文本框中的文本变为 "嘿嘿嘿~派大星我们去抓水母吧~"
'''
from PyQt5.QtWidgets import QWidget, QApplication, QComboBox, QLabel, QLineEdit, QPushButton, QGridLayout


class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("我的窗口")
        self.setFixedSize(400, 500)
        layout = QGridLayout()
        self.text = QLineEdit()
        self.button = QPushButton('点击我')
        layout.addWidget(self.text)
        layout.addWidget(self.button)
        self.setLayout(layout)
        # 为按钮添加点击事件

    # 定义事件处理函数


app = QApplication([])
widget = MyApp()
widget.show()
app.exec_()
