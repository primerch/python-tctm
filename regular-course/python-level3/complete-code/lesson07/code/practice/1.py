"""
尝试使用python的pyqt5库创建一个成绩记录表。
你需要编写代码，满足如下要求：
1. 在成绩记录表上显示童程学院的学生成绩，成绩信息如下：
姓名 语文 数学 英语
小派 100  99   95
童童 100 100  100

请输出满足要求的代码
"""
# 请使用上述提示词，创建一个成绩记录表
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem


class ScoreTable(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("成绩记录表")
        self.setGeometry(100, 100, 400, 300)

        self.table_widget = QTableWidget(self)
        self.table_widget.setGeometry(10, 10, 380, 280)

        self.table_widget.setColumnCount(4)
        self.table_widget.setHorizontalHeaderLabels(['姓名', '语文', '数学', '英语'])

        self.load_data()

    def load_data(self):
        data = [
            ['小派', '100', '99', '95'],
            ['童童', '100', '100', '100']
        ]

        self.table_widget.setRowCount(len(data))

        for i, row in enumerate(data):
            for j, value in enumerate(row):
                item = QTableWidgetItem(value)
                self.table_widget.setItem(i, j, item)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    score_table = ScoreTable()
    score_table.show()
    sys.exit(app.exec_())
