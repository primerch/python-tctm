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


app = QApplication([])
window = QMainWindow()
window.setWindowTitle('查作业')
widget = SearchWidget()
window.setCentralWidget(widget)
window.showMaximized()
app.exec_()
