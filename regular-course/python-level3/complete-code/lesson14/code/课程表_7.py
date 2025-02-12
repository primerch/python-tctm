import csv
import datetime
import os
from PyQt5.Qt import *
#  1. 导入自定义文件读写类
from utils_5 import CSVHandler


class CourseWidget(QWidget):
    def __init__(self):
        super().__init__()
        layout = QGridLayout()
        self.setLayout(layout)
        self.table = QTableWidget(13, 7)
        layout.addWidget(self.table)
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

    def modify(self, row, col):
        newTxt = self.table.item(row, col).text()
        self.data[row][col] = newTxt
        # 2. 使用自定义工具类中的save方法替换原始的文件写入操作
        CSVHandler.save('course.csv', self.data)

    def load(self):
        if os.path.exists('course.csv'):
            # 3. 使用自定义工具类中的load()方法替换原始的文件读取操作
            self.data = CSVHandler.load('course.csv')

        for r in range(len(self.data)):
            row = self.data[r]
            for c in range(len(row)):
                data = self.data[r][c]
                item = QTableWidgetItem(data)
                self.table.setItem(r, c, item)
                item.setTextAlignment(Qt.AlignCenter)
                if c == datetime.datetime.today().weekday():
                    item.setBackground(QColor('skyblue'))


app = QApplication([])
window = QMainWindow()
window.setWindowTitle("课程表")
widget = CourseWidget()
window.setCentralWidget(widget)
window.showMaximized()
app.exec_()
