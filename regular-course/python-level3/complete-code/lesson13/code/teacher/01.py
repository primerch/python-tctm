'''

这是我的授课思路：
问题：如何在填写作业后点击添加作业按钮将作业添加到表格中？
解决：通过按钮点击事件获取用户在文本框中的内容
问题：当天录入的作业时间和状态都是相同的，需要反复输入？
解决：为了不让用户反复输入当天作业的日期，程序需要自动获得当前作业的日期
      为了不让用户反复输入相同的作业状态，程序可以固定作业的起始状态
以下是我的授课代码：
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

app = QApplication([])
window = QMainWindow()
widget = HomeworkWidget()
window.setCentralWidget(widget)
window.setWindowTitle("记作业")
window.showMaximized()
app.exec_()

请帮我使用中文，根据以上内容出5道单选题，帮助学员理解如何通过在界面上输入的作业和内容，生成完整的作业数据

'''
