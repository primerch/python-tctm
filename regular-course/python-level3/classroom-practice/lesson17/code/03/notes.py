import os
from PyQt5.Qt import *
from utils import CSVHandler


class NotesWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("备忘录")
        self.layout = QGridLayout()
        self.setLayout(self.layout)
        self.sub = QLabel("课程名称")
        self.subEdit = QLineEdit()
        self.con = QLabel("备忘录内容")
        self.conEdit = QLineEdit()
        self.addBtn = QPushButton("添加备忘录")
        self.layout.addWidget(self.sub, 0, 0)
        self.layout.addWidget(self.subEdit, 0, 1)
        self.layout.addWidget(self.con, 0, 2)
        self.layout.addWidget(self.conEdit, 0, 3)
        self.layout.addWidget(self.addBtn, 0, 4)
        self.table = QTableWidget(0, 2)
        self.table.setHorizontalHeaderLabels(['课程名称', '备忘录内容'])
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
        CSVHandler.save('notes.csv', self.data)
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
        for col in range(2):
            item = QTableWidgetItem(rowData[col])
            item.setTextAlignment(Qt.AlignCenter)
            self.table.setItem(count, col, item)

    def show(self):
        if os.path.exists('notes.csv'):
            self.data = CSVHandler.load('notes.csv')
        for hw in self.data:
            self.addRow(hw)

    def add(self):
        subject = self.subEdit.text()
        content = self.conEdit.text()
        if not subject or not content:
            return
        rm = [subject, content]
        self.data.append(rm)
        CSVHandler.save('notes.csv', self.data)
        self.addRow(rm)
        self.subEdit.clear()
        self.conEdit.clear()


app = QApplication([])
window = QMainWindow()
widget = NotesWidget()
window.setWindowTitle('备忘录')
window.setCentralWidget(widget)
window.showMaximized()
app.exec_()
