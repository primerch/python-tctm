'''

继续添加功能，使用csv模块从data.csv中读取数据,注意编码方式为utf8
筛选csv中的数据，如果当前数据第三列是"不会"，就保存到临时列表中
读取临时列表中前两列数据，添加到表格的前两列，然后为表格每一行的后两列添加显示释义按钮和标记已会按钮
写入文件是要加newline=''参数选项
返回修改后的完整代码，为每行代码添加注释

'''
# 导入必要的库
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QTableWidget, QTableWidgetItem, \
    QHeaderView, QPushButton
import csv
import sys


# 创建一个QMainWindow子类
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # 设置窗口的大小和标题
        self.setWindowTitle('背单词')
        self.resize(1200, 675)

        # 创建一个中心部件对象
        widget = QWidget()

        # 创建一个布局
        layout = QVBoxLayout()

        # 创建一个15行4列的表格
        table = QTableWidget(15, 4)

        # 设置表头
        table.setHorizontalHeaderLabels(['单词', '中文释义', '显示释义', '标记已会'])

        # 使用QHeaderView.Stretch拉伸表头让表格占满窗口
        table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # 从csv文件中读取数据
        with open('data.csv', 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            temp_list = [row for row in reader if row[2] == "不会"]

        # 将数据添加到表格中
        for i, row in enumerate(temp_list):
            table.setItem(i, 0, QTableWidgetItem(row[0]))
            table.setItem(i, 1, QTableWidgetItem(row[1]))
            table.setCellWidget(i, 2, QPushButton('显示释义'))
            table.setCellWidget(i, 3, QPushButton('标记已会'))

        # 将表格添加到布局中
        layout.addWidget(table)

        # 将布局添加到中心部件对象
        widget.setLayout(layout)

        # 将widget设置为窗口的中心部件
        self.setCentralWidget(widget)


# 创建一个应用实例
app = QApplication(sys.argv)

# 创建一个窗口实例
window = MainWindow()

# 显示窗口
window.show()

# 进入应用的主循环
sys.exit(app.exec_())
