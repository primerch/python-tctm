import datetime
import os
from PyQt5.Qt import *
from utils import CSVHandler


class HomeworkWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QGridLayout()
        self.setLayout(self.layout)
        self.sub = QLabel("科目")
        self.subEdit = QLineEdit()
        self.con = QLabel("内容")
        self.conEdit = QLineEdit()
        self.addBtn = QPushButton("添加作业")
        self.layout.addWidget(self.sub, 0, 0)
        self.layout.addWidget(self.subEdit, 0, 1)
        self.layout.addWidget(self.con, 0, 2)
        self.layout.addWidget(self.conEdit, 0, 3)
        self.layout.addWidget(self.addBtn, 0, 4)
        self.table = QTableWidget(0, 4)
        self.table.setHorizontalHeaderLabels(['日期', '科目', '内容', '状态'])
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.layout.addWidget(self.table, 1, 0, 1, 5)
        self.addBtn.clicked.connect(self.add)
        self.data = []
        self.show()
        self.table.setContextMenuPolicy(Qt.CustomContextMenu)
        self.table.customContextMenuRequested.connect(self.showMenu)
        self.table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)

    def showMenu(self):
        menu = QMenu()
        actToggle = QAction('切换作业状态')
        actDelete = QAction('删除作业')
        menu.addAction(actToggle)
        menu.addAction(actDelete)
        actToggle.triggered.connect(self.toggle)
        menu.exec_(QCursor.pos())

    def toggle(self):
        rowData = self.getCurrentRow()
        i = self.data.index(rowData)
        self.data[i][3] = '已完成' if self.data[i][3] == '未完成' else '未完成'
        CSVHandler.save('homeworks.csv', self.data)
        # 1. 先清空表格中旧的数据
        self.table.setRowCount(0)
        # 2. 更新数据
        self.show()

    def getCurrentRow(self):
        rowIndex = self.table.currentRow()
        rowData = []
        for col in range(4):
            rowData.append(self.table.item(rowIndex, col).text())
        return rowData

    def addRow(self, rowData):
        count = self.table.rowCount()
        self.table.insertRow(count)
        for col in range(len(rowData)):
            item = QTableWidgetItem(rowData[col])
            item.setTextAlignment(Qt.AlignCenter)
            self.table.setItem(count, col, item)

    def show(self):
        if os.path.exists('homeworks.csv'):
            self.data = CSVHandler.load('homeworks.csv')
        today = datetime.datetime.today().strftime("%Y-%m-%d")
        for hw in self.data:
            if hw[0] == today:
                self.addRow(hw)

    def add(self):
        date_today = datetime.datetime.today().strftime("%Y-%m-%d")
        subject = self.subEdit.text()
        content = self.conEdit.text()
        if not subject or not content:
            return
        hw = [date_today, subject, content, '未完成']
        self.data.append(hw)
        CSVHandler.save('homeworks.csv', self.data)
        self.addRow(hw)
        self.subEdit.clear()
        self.conEdit.clear()


app = QApplication([])
window = QMainWindow()
window.setWindowTitle('记作业')
widget = HomeworkWidget()
window.setCentralWidget(widget)
window.showMaximized()
app.exec_()
