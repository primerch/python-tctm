'''

请帮我根据代码生成一个功能完全相同的备忘录程序
备忘录中只需要记录课程名和提醒内容两个字段，可以通过右键菜单删除备忘录，返回修改后的完整代码

'''
import os
from PyQt5.Qt import *
from utils import CSVHandler


class MemoWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QGridLayout()
        self.setLayout(self.layout)
        self.sub = QLabel("课程名")
        self.subEdit = QLineEdit()
        self.con = QLabel("提醒内容")
        self.conEdit = QLineEdit()
        self.addBtn = QPushButton("添加备忘录")
        self.layout.addWidget(self.sub, 0, 0)
        self.layout.addWidget(self.subEdit, 0, 1)
        self.layout.addWidget(self.con, 0, 2)
        self.layout.addWidget(self.conEdit, 0, 3)
        self.layout.addWidget(self.addBtn, 0, 4)
        self.table = QTableWidget(0, 2)
        self.table.setHorizontalHeaderLabels(['课程名', '提醒内容'])
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
        actDelete = QAction('删除备忘录')
        menu.addAction(actDelete)
        actDelete.triggered.connect(self.delete)
        menu.exec_(QCursor.pos())

    def delete(self):
        rowData = self.getCurrentRow()
        i = self.data.index(rowData)
        self.data.pop(i)
        CSVHandler.save('memos.csv', self.data)
        self.table.setRowCount(0)
        self.show()

    def getCurrentRow(self):
        rowIndex = self.table.currentRow()
        rowData = []
        for col in range(2):
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
        if os.path.exists('memos.csv'):
            self.data = CSVHandler.load('memos.csv')
        for memo in self.data:
            self.addRow(memo)

    def add(self):
        subject = self.subEdit.text()
        content = self.conEdit.text()
        if not subject or not content:
            return
        memo = [subject, content]
        self.data.append(memo)
        CSVHandler.save('memos.csv', self.data)
        self.addRow(memo)
        self.subEdit.clear()
        self.conEdit.clear()


app = QApplication([])
window = QMainWindow()
window.setWindowTitle('备忘录')
widget = MemoWidget()
window.setCentralWidget(widget)
window.showMaximized()
app.exec_()
