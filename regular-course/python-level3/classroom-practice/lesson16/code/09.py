import os
import datetime

from PyQt5.Qt import *
from utils import CSVHandler


class SearchWidget(QWidget):
    def __init__(self):
        super().__init__()
        layout = QGridLayout()
        label = QLabel('时间段')
        layout.addWidget(label, 0, 0)
        label.setAlignment(Qt.AlignRight)

        timeList = ['全部', '一周内', '两周内', '三周内', '四周内', '五周内', '六周内', '七周内', '八周内']
        self.daysCmb = QComboBox()
        self.daysCmb.addItems(timeList)
        layout.addWidget(self.daysCmb, 0, 1)

        self.table = QTableWidget(0, 4)
        self.table.setHorizontalHeaderLabels(['日期', '科目', '内容', '状态'])
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        layout.addWidget(self.table, 1, 0, 1, 2)
        self.setLayout(layout)
        self.data = []
        self.refresh()
        self.daysCmb.currentIndexChanged.connect(self.refresh)

    def refresh(self):
        if os.path.exists('homeworks.csv'):
            self.data = CSVHandler.load('homeworks.csv')

        i = self.daysCmb.currentIndex()
        self.search(i)

        self.table.setRowCount(0)
        for rowData in self.result:
            CSVHandler.addRow(self.table, rowData)

    def search(self, i):
        # 1. 如果选择下拉列表第一个选项 也就是全部选项

        # 此时筛选的数据为全部数据

        # 不需要再计算时间段

        today = datetime.datetime.today().date()
        start = today - datetime.timedelta(days=7 * i - 1)
        self.result = []
        for hw in self.data:
            date = datetime.datetime.strptime(hw[0], '%Y-%m-%d').date()
            if start <= date and date <= today:
                self.result.append(hw)


app = QApplication([])
window = QMainWindow()
window.setWindowTitle('查作业')
widget = SearchWidget()
window.setCentralWidget(widget)
window.showMaximized()
app.exec_()
