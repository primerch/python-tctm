from PyQt5.Qt import *

app = QApplication([])
window = QMainWindow()
window.setWindowTitle("课程表")

# 1. 自定义widget实现课程表功能

# 修改PyQt设置，显示setStyleSheet设置的背景颜色


# 2. 使用自定义的CourseWidget


window.showMaximized()
app.exec_()
