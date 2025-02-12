'''
太棒了，接下来在刚才的代码中为HomeworkWidget添加以下属性：
1. sub，用来在header中添加一个文本"科目"，添加到网格布局第一行第一列
2. subEdit， 用来在header中添加一个输入框，添加到网格布局第一行第二列
3. con，用来在header中添加一个文本"内容"，添加到网格布局第一行第三列
4. conEdit， 用来在header中添加一个输入框，添加到网格布局第一行第四列
5. addBtn， 用来在header中添加一个添加作业的按钮，添加到网格布局第一行第五列
请按照要求以代码格式显示结果，不需要解释
'''

from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout, QLabel, QLineEdit, QPushButton


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


app = QApplication([])

window = QMainWindow()
widget = HomeworkWidget()
window.setCentralWidget(widget)
window.setWindowTitle("记作业")
window.showMaximized()
app.exec_()
