import os

from PyQt5.Qt import *
from utils import CSVHandler


class SearchWidget(QWidget):
    def __init__(self):
        super().__init__()
        layout = QGridLayout()
        label = QLabel('时间段')
        layout.addWidget(label, 0, 0)
        self.daysCmb = QLineEdit()
        layout.addWidget(self.daysCmb, 0, 1)
        self.btn = QPushButton('查询作业')
        layout.addWidget(self.btn, 0, 2)
        self.table = QTableWidget(0, 4)
        self.table.setHorizontalHeaderLabels(['日期', '科目', '内容', '状态'])
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        layout.addWidget(self.table, 1, 0, 1, 4)
        self.setLayout(layout)
        # 老师提前定义好的data属性  保存程序中的作业数据
        self.data = []
        # 1. 调用加载数据的方法

    # 老师提前定义好的加载数据的方法，从csv文件中将数据读取到程序中
    def refresh(self):
        if os.path.exists('homeworks.csv'):
            self.data = CSVHandler.load('homeworks.csv')
        # 清空表格
        self.table.setRowCount(0)
        # 遍历二维列表，根据作业数据向表格中添加行和单元格
        for rowData in self.data:
            CSVHandler.addRow(self.table, rowData)


app = QApplication([])
window = QMainWindow()
window.setWindowTitle('查作业')
widget = SearchWidget()
window.setCentralWidget(widget)
window.showMaximized()
app.exec_()
