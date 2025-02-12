'''

这是我的授课思路：
问题：创建的表格是0行4列的，现在没有行，新添加的作业放哪儿？
解决：按照标准的顺序，要先添加行，才添加单元格
问题: 今后表格中有多少行，不确定，每次添加新行的行号是多少
解决: 先知道当前表格已经有多少行，然后在末尾插入空行
问题: 因为将来向表格中插入一行数据的操作，使用非常频繁
解决: 封装为addRow()方法，便于反复调用
问题：每次添加的内容都是用户输入的不确定，怎么办？
解决：将要添加的内容定义为参数，当用户输入好内容后再调用函数传入数据

以下是我的代码：
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


请帮我使用中文，根据以上内容出5道单选题，帮助学员理解如何向表格中添加作业

'''
