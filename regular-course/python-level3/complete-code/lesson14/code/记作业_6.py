import csv
import datetime
import os
from PyQt5.Qt import *
# 1. 导入自定义工具类
from utils_5 import CSVHandler


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
        self.show()

    def addRow(self, rowData):
        count = self.table.rowCount()
        self.table.insertRow(count)
        for col in range(len(rowData)):
            item = QTableWidgetItem(rowData[col])
            item.setTextAlignment(Qt.AlignCenter)
            self.table.setItem(count, col, item)

    def save(self):
        with open('homeworks.csv', 'w', encoding='utf8', newline='') as f:
            writer = csv.writer(f)
            writer.writerows(self.data)

    def add(self):
        subject = self.subEdit.text()
        content = self.conEdit.text()
        if not subject or not content:
            QMessageBox.warning(self, '规范输入', '请输入正确的作业科目和内容')
            return
        today = datetime.datetime.today().strftime('%Y-%m-%d')
        rowData = [today, subject, content, '未完成']
        self.data.append(rowData)
        # 2. 使用自定义工具类中的save方法替换原有的self.save()
        #    传入文件名(小心不要写错)和二维列表
        # self.save()
        CSVHandler.save('homeworks.csv', self.data)

        self.addRow(rowData)
        self.subEdit.clear()
        self.conEdit.clear()

    def show(self):
        if os.path.exists('homeworks.csv'):
            # 3. 使用自定义工具类中的load方法替换原有的self.load()
            #    传入文件名，保证和save方法中传入的文件名一致
            # self.load()
            self.data = CSVHandler.load('homeworks.csv')
        today = datetime.datetime.today().strftime("%Y-%m-%d")
        for rowData in self.data:
            if rowData[0] == today:
                self.addRow(rowData)

    def load(self):
        with open('homeworks.csv', 'r', encoding='utf8') as f:
            reader = csv.reader(f)
            return list(reader)


app = QApplication([])
window = HomeworkWidget()
window.setWindowTitle("记作业")
window.showMaximized()
app.exec_()
