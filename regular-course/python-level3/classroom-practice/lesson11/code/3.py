from PyQt5.Qt import *

app = QApplication([])
window = QMainWindow()
window.setWindowTitle("课程表")


class CourseWidget(QWidget):
    def __init__(self):
        super().__init__()
        # 1. 创建并添加布局

        # 2. 创建13行7列的表格控件并使用


widget = CourseWidget()
window.setCentralWidget(widget)

window.showMaximized()
app.exec_()
