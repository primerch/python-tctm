'''
在上一道题目生成的窗口中
创建一个按钮和一个文本框

'''
from PyQt5.QtWidgets import QWidget, QApplication, QLineEdit, QPushButton, QGridLayout


class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("我的窗口")
        self.setFixedSize(400, 500)
        # 创建布局对象

        # 创建一个文本框

        # 创建按钮

        # 将文本框和按钮添加到布局中

        # 将布局添加到widget中


app = QApplication([])
widget = MyApp()
widget.show()
app.exec_()
