from PyQt5.Qt import *

app = QApplication([])
window = QMainWindow()
window.setWindowTitle("课程表")


# 1. 自定义widget实现课程表功能
class CourseWidget(QWidget):
    def __init__(self):
        super().__init__()
        # 修改PyQt设置，显示setStyleSheet设置的背景颜色
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setStyleSheet('background-color: lightblue')


# 2. 使用自定义的CourseWidget
widget = CourseWidget()
window.setCentralWidget(widget)

window.showMaximized()
app.exec_()
