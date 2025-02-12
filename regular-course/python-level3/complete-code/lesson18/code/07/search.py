import sys
import csv
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QTextEdit, QGridLayout
from PyQt5.QtGui import QFont


class SearchWords(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        grid = QGridLayout()
        self.setLayout(grid)

        self.input_line = QLineEdit(self)
        self.input_line.setFixedSize(600, 50)
        grid.addWidget(self.input_line, 0, 0)

        self.query_btn = QPushButton('查询', self)
        self.query_btn.setFixedSize(200, 50)
        self.query_btn.clicked.connect(self.query)  # 添加点击事件
        grid.addWidget(self.query_btn, 0, 1)

        self.result_area = QTextEdit(self)
        self.result_area.setFont(QFont("Arial", 20, QFont.Bold))  # 设置字体大小和加粗
        grid.addWidget(self.result_area, 1, 0, 1, 2)

        self.setWindowTitle('查询单词')
        self.setGeometry(300, 300, 1200, 675)

    def query(self):
        query_text = self.input_line.text()
        if not query_text:
            self.result_area.setText("请输入查询内容")
            return

        with open('data.csv', 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            for row in reader:
                if query_text in row:
                    if query_text == row[0]:  # 输入的是英文
                        self.result_area.setText(row[1])  # 显示中文翻译
                    else:  # 输入的是中文
                        self.result_area.setText(row[0])  # 显示英文单词
                    return

        self.result_area.setText("没有查询到结果")  # 没有找到匹配项


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = SearchWords()
    app.setFont(QFont('Arial', 16))
    ex.show()
    sys.exit(app.exec_())
'''

是我的代码，不需要解读代码，等待我的下一步指示

'''
