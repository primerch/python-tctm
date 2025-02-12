from PyQt5.Qt import *

app = QApplication([])
window = QMainWindow()
window.setWindowTitle("课程表")


class CourseWidget(QWidget):
    def __init__(self):
        super().__init__()
        layout = QGridLayout()
        self.setLayout(layout)
        self.table = QTableWidget(13, 7)
        layout.addWidget(self.table)
        weeks = ['星期一', '星期二', '星期三', '星期四', '星期五', '星期六', '星期日']
        hours = ['08:00', '09:00', '10:00', '11:00', '12:00', '13:00', '14:00', '15:00', '16:00',
                 '17:00', '18:00', '19:00', '20:00', ]
        self.table.setHorizontalHeaderLabels(weeks)
        self.table.setVerticalHeaderLabels(hours)
        # 1. 获取水平表头

        # 2. 设置水平表头边框，然后拉抻水平表头


widget = CourseWidget()
window.setCentralWidget(widget)

window.showMaximized()
app.exec_()
