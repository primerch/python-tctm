import datetime
from PyQt5.Qt import *


class HomeworkWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.data = []
        self.layout = QGridLayout()
        self.setLayout(self.layout)

        self.sub = QLabel("科目")
        self.layout.addWidget(self.sub, 0, 0)

        self.subEdit = QLineEdit()
        self.layout.addWidget(self.subEdit, 0, 1)

        self.con = QLabel("内容")
        self.layout.addWidget(self.con, 0, 2)

        self.conEdit = QLineEdit()
        self.layout.addWidget(self.conEdit, 0, 3)

        self.addBtn = QPushButton("添加作业")
        self.layout.addWidget(self.addBtn, 0, 4)

        self.table = QTableWidget()
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(['日期', '科目', '内容', '状态'])
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.layout.addWidget(self.table, 1, 0, 1, 5)

        self.addBtn.clicked.connect(self.add)

    def add(self):
        subject = self.subEdit.text()
        content = self.conEdit.text()
        today = datetime.datetime.today().strftime('%Y-%m-%d')
        rowData = [today, subject, content, '未完成']
        self.addRow(rowData)
        # 1. 每次添加数据后清空输入框内容方便添加新数据
        self.subEdit.clear()
        self.conEdit.clear()

    def addRow(self, rowData):
        count = self.table.rowCount()
        self.table.insertRow(count)
        for col in range(len(rowData)):
            item = QTableWidgetItem(rowData[col])
            self.table.setItem(count, col, item)


app = QApplication([])
window = QMainWindow()
widget = HomeworkWidget()
window.setCentralWidget(widget)
window.setWindowTitle("记作业")
window.showMaximized()
app.exec_()
