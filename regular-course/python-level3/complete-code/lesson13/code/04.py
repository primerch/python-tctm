'''
在刚才的代码中继续为HomeworkWidget添加属性，要求如下：
1. 添加table属性，实现一个0行4列的表格部件
2. 设置水平方向表头为'日期', '科目', '内容', '状态'
3. 设置表格水平表头的拉伸模式为"Stretch"，使其尽可能填满表格的宽度
4. 将表格添加到layout布局中，在第二行显示，整个表格占网格布局中的1行5列
请按照要求以代码格式显示结果，不需要解释
'''
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout, QLabel, QLineEdit, QPushButton, \
    QTableWidget, QTableWidgetItem, QHeaderView


class HomeworkWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QGridLayout()
        self.setLayout(self.layout)
        self.data = []

        self.sub = QLabel('科目')
        self.layout.addWidget(self.sub, 0, 0)
        self.subEdit = QLineEdit()
        self.layout.addWidget(self.subEdit, 0, 1)
        self.con = QLabel('内容')
        self.layout.addWidget(self.con, 0, 2)
        self.conEdit = QLineEdit()
        self.layout.addWidget(self.conEdit, 0, 3)
        self.addBtn = QPushButton('添加作业')
        self.layout.addWidget(self.addBtn, 0, 4)

        self.table = QTableWidget(0, 4)
        self.table.setHorizontalHeaderLabels(['日期', '科目', '内容', '状态'])
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.layout.addWidget(self.table, 1, 0, 1, 5)


app = QApplication([])

window = QMainWindow()
widget = HomeworkWidget()
window.setCentralWidget(widget)
window.setWindowTitle("记作业")
window.showMaximized()
app.exec_()
