'''

帮我生成一个pyqt窗口，整个窗口的大小为1200*675，窗口标题为'已会单词'
为窗口创建布局，并在布局中添加一个0行2列的表格，然后将布局添加到窗口中
设置表格的表头为['单词'，'中文释义']
使用QHeaderView.Stretch拉伸表头让表格占满窗口
使用utf8编码方式打开data.csv,
如果数据第三列是已会，就读取前面的单词和释义，将单词和释义分别写入表格的单元格
为每行代码添加注释

'''
# 导入必要的库
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget, QHeaderView
from PyQt5.QtCore import Qt

import csv


# 创建主窗口类
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # 设置窗口大小
        self.resize(1200, 675)
        # 设置窗口标题
        self.setWindowTitle('已会单词')

        # 创建主窗口的布局
        self.main_widget = QWidget()
        self.setCentralWidget(self.main_widget)
        self.main_layout = QVBoxLayout()
        self.main_widget.setLayout(self.main_layout)

        # 创建一个0行2列的表格
        self.table_widget = QTableWidget(0, 2)
        # 设置表格的表头
        self.table_widget.setHorizontalHeaderLabels(['单词', '中文释义'])

        # 使用QHeaderView.Stretch拉伸表头让表格占满窗口
        self.table_widget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # 将表格添加到布局中
        self.main_layout.addWidget(self.table_widget)

        # 使用utf8编码方式打开data.csv
        with open('data.csv', 'r', encoding='utf-8') as f:
            csv_reader = csv.reader(f)
            for i, row in enumerate(csv_reader):
                # 如果数据第三列是已会，就读取前面的单词和释义
                if row[2] == '已会':
                    # 将单词和释义分别写入表格的单元格
                    self.table_widget.insertRow(i)
                    self.table_widget.setItem(i, 0, QTableWidgetItem(row[0]))
                    self.table_widget.setItem(i, 1, QTableWidgetItem(row[1]))


# 主函数
if __name__ == '__main__':
    # 创建应用程序和窗口
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    # 进入应用程序的主循环
    sys.exit(app.exec_())
