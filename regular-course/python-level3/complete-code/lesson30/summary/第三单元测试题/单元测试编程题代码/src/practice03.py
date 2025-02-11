from PyQt5.Qt import *


class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        # 1. 创建一个网格布局

        # 2. 设置为当前窗口的布局

        # 3. 创建一个列表控件

        # 4. 创建两个列表项控件，文本分别是'小派'和'童童'

        # 5. 将两个列表项控件添加到列表控件中

        # 6. 将列表控件添加到网格布局中


if __name__ == '__main__':
    app = QApplication([])
    widget = MyWidget()
    widget.show()
    app.exec_()
