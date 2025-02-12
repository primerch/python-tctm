'''
请使用PyQt库编写一个简单的应用程序窗口
要求为该程序设置标题为“我的窗口”，
宽度为400，高度为500
'''
from PyQt5.QtWidgets import QWidget, QApplication, QComboBox, QLabel, QLineEdit, QPushButton, QGridLayout


# 自定义类MyApp继承QWidget类
class MyApp(QWidget):
    # 在初始化方法中设置窗口的标题为“我的窗口”设置大小为宽400,高500
    def __init__(self):
        super().__init__()
        self.setWindowTitle("我的窗口")
        self.setFixedSize(400, 500)


# 创建应用程序对象
app = QApplication([])
# 创建MyApp对象
widget = MyApp()
# 显示窗口
widget.show()
# 启动应用程序窗口
app.exec_()
