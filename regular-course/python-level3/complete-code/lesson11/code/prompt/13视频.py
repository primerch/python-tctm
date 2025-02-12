"""

这是我今天编写的代码：
```
import datetime
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
        header = self.table.horizontalHeader()
        header.setStyleSheet('border: 1px solid gray')
        header.setSectionResizeMode(QHeaderView.Stretch)

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

    def load(self):
        for r in range(len(self.data)):
            row = self.data[r]
            for c in range(len(row)):
                data = self.data[r][c]
                item = QTableWidgetItem(data)
                self.table.setItem(r, c, item)
                item.setTextAlignment(Qt.AlignCenter)
                if c == datetime.datetime.today().weekday():
                    item.setBackground(QColor('skyblue'))

widget = CourseWidget()
window.setCentralWidget(widget)
window.showMaximized()
app.exec_()


```
请根据代码详细总结今天学习的有关pyqt5和datetime的所有知识点


"""
