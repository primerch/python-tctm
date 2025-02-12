import csv
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

    def addRow(self, rowData):
        count = self.table.rowCount()
        self.table.insertRow(count)
        for col in range(len(rowData)):
            item = QTableWidgetItem(rowData[col])
            item.setTextAlignment(Qt.AlignCenter)
            self.table.setItem(count, col, item)

    def add(self):
        subject = self.subEdit.text()
        content = self.conEdit.text()
        if not subject or not content:
            QMessageBox.warning(self, '规范输入', '请输入正确的作业科目和内容')
            return
        today = datetime.datetime.today().strftime('%Y-%m-%d')
        rowData = [today, subject, content, '未完成']
        # 1. 将界面数据保存到程序中的二维列表中

        # 2. 将程序中的二维列表整体保存到文件中

        self.addRow(rowData)
        self.subEdit.clear()
        self.conEdit.clear()

    # 老师提前预留好的save方法
    def save(self):
        with open('homeworks.csv', 'w', encoding='utf8', newline='') as f:
            writer = csv.writer(f)
            writer.writerows(self.data)


app = QApplication([])
window = QMainWindow()
widget = HomeworkWidget()
window.setCentralWidget(widget)
window.setWindowTitle("记作业")
window.showMaximized()
app.exec_()
