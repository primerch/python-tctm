import datetime
import csv
import os
from PyQt5.Qt import *
import Style

app = QApplication([])
window = QMainWindow()
window.setWindowTitle("课程表")


class CourseWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.table = QTableWidget(13, 7, self)
        weeks = ['星期一', '星期二', '星期三', '星期四', '星期五', '星期六', '星期日']
        self.table.setHorizontalHeaderLabels(weeks)
        self.table.horizontalHeader().setStyleSheet('border: 1px solid gray')
        hours = ['08:00', '09:00', '10:00', '11:00', '12:00', '13:00', '14:00', '15:00', '16:00',
                 '17:00', '18:00', '19:00', '20:00', ]
        self.table.setVerticalHeaderLabels(hours)
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.data = [
            ['', '', '', '', '', '', ''],
            ['品德', '英语', '品德', '体育', '英语', '', ''],
            ['班队', '班队', '英语', '班队', '品德', '', ''],
            ['美术', '班队', '数学', '英语', '科学', '', ''],
            ['', '', '', '', '', '', ''],
            ['', '', '', '', '', '', ''],
            ['英语', '美术', '体育', '体育', '品德', '', ''],
            ['品德', '科学', '数学', '英语', '英语', '', ''],
            ['体育', '语文', '体育', '科学', '语文', '', ''],
            ['', '', '', '', '', '', ''],
            ['', '', '', '', '', '', ''],
            ['', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '']
        ]
        self.load()
        self.table.cellChanged.connect(self.modify)

        # 添加控件
        self.title = QLabel(self)
        self.limg = QLabel(self)
        self.rimg = QLabel(self)

    def modify(self, row, col):
        new = self.table.item(row, col).text()
        self.data[row][col] = new
        with open('course.csv', 'w', encoding='utf8', newline='') as f:
            writer = csv.writer(f)
            writer.writerows(self.data)

    def load(self):
        # 1.判断course.csv文件是否存在
        if os.path.exists('course.csv'):
            with open('course.csv', 'r', encoding='utf8') as f:
                reader = csv.reader(f)
                self.data = list(reader)

        for row in range(13):
            for col in range(7):
                data = self.data[row][col]
                item = QTableWidgetItem(data)
                self.table.setItem(row, col, item)
                item.setTextAlignment(Qt.AlignCenter)
                if col == datetime.datetime.today().weekday():
                    item.setBackground(QColor('skyblue'))


widget = CourseWidget()
window.setCentralWidget(widget)

# 调用封装好的样式代码 传入需要调整样式的内容
Style.init_ui(app, window, widget.table, widget.title, widget.limg, widget.rimg)
window.show()

app.exec_()
