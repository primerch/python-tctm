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
        self.table.setContextMenuPolicy(Qt.CustomContextMenu)
        self.table.customContextMenuRequested.connect(self.showMenu)
        self.table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)

    def showMenu(self, pos):
        item = self.table.itemAt(pos)
        if item is None:
            return

        menu = QMenu()
        actToggle = QAction('切换作业状态')
        menu.addAction(actToggle)
        actToggle.triggered.connect(self.toggle)
        menu.exec_(QCursor.pos())

    def toggle(self):
        rowData = self.getCurrentRow()
        i = self.data.index(rowData)
        self.data[i][3] = '已完成' if self.data[i][3] == '未完成' else '未完成'
        CSVHandler.save('data/homeworks.csv', self.data)
        self.table.setRowCount(0)
        self.refresh()

    def getCurrentRow(self):
        rowIndex = self.table.currentRow()
        rowData = []
        for col in range(4):
            rowData.append(self.table.item(rowIndex, col).text())
        return rowData

    def search(self, i):
        self.result = []
        if i == 0:
            self.result = self.data
            return
        today = datetime.datetime.today().date()
        start = today - datetime.timedelta(days=7 * i)

        for hw in self.data:
            date = datetime.datetime.strptime(hw[0], '%Y-%m-%d').date()
            if start < date and date <= today:
                self.result.append(hw)

    def refresh(self):
        if os.path.exists('data/homeworks.csv'):
            self.data = CSVHandler.load('data/homeworks.csv')

        i = self.daysCmb.currentIndex()
        self.search(i)

        self.table.setRowCount(0)
        for rowData in self.result:
            CSVHandler.addRow(self.table, rowData)


if __name__ == '__main__':
    app = QApplication([])
    window = QMainWindow()
    window.setWindowTitle('查作业')
    widget = SearchWidget()
    window.setCentralWidget(widget)
    window.showMaximized()
    app.exec_()
