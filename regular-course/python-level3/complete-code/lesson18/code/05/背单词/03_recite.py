'''

在向表格第二列添加内容时，先创建单元格，然后向单元格中添加空字符串
当用户点击当前行显示释义按钮时，才将当前行第二列的内容添加到表格中
当用户点击标记已会按钮时，将当前行前两列内容变为绿色，然后，使用uft8编码打开data.csv，设置newline=''，遍历所有读取到的数据，如果数据的第一列和第二列和被点击按钮当前行第一列第二列一致，且数据的第三列为'不会'时，将数据的第三列改为'已会'
最后设置前两列单元格中的内容不可编辑
为每行代码添加注释

'''

# 导入必要的库
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QTableWidget, QTableWidgetItem, \
    QHeaderView, QPushButton
from PyQt5.QtCore import Qt
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
        self.table = QTableWidget(15, 4)

        # 设置表头
        self.table.setHorizontalHeaderLabels(['单词', '中文释义', '显示释义', '标记已会'])

        # 使用QHeaderView.Stretch拉伸表头让表格占满窗口
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # 从csv文件中读取数据
        with open('data.csv', 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            self.temp_list = [row for row in reader if row[2] == "不会"]

        # 将数据添加到表格中
        for i, row in enumerate(self.temp_list):
            self.table.setItem(i, 0, QTableWidgetItem(row[0]))
            self.table.setItem(i, 1, QTableWidgetItem(''))  # 先添加空字符串
            btn_show = QPushButton('显示释义')
            btn_show.clicked.connect(lambda _, x=i: self.show_meaning(x))  # 绑定点击事件，传入当前行号
            self.table.setCellWidget(i, 2, btn_show)
            btn_mark = QPushButton('标记已会')
            btn_mark.clicked.connect(lambda _, x=i: self.mark_known(x))  # 绑定点击事件，传入当前行号
            self.table.setCellWidget(i, 3, btn_mark)

        # 将表格添加到布局中
        layout.addWidget(self.table)

        # 将布局添加到中心部件对象
        widget.setLayout(layout)

        # 将widget设置为窗口的中心部件
        self.setCentralWidget(widget)

    def show_meaning(self, row):
        # 显示中文释义
        self.table.item(row, 1).setText(self.temp_list[row][1])

    def mark_known(self, row):
        # 标记为已知
        self.table.item(row, 0).setBackground(Qt.green)  # 设置背景色为绿色
        self.table.item(row, 1).setBackground(Qt.green)  # 设置背景色为绿色
        self.table.item(row, 0).setFlags(Qt.ItemIsEnabled)  # 设置为不可编辑
        self.table.item(row, 1).setFlags(Qt.ItemIsEnabled)  # 设置为不可编辑
        # 更新csv文件
        with open('data.csv', 'r', encoding='utf-8') as f:
            data = list(csv.reader(f))
        with open('data.csv', 'w', encoding='utf-8', newline='') as f:
            writer = csv.writer(f)
            for row_data in data:
                if row_data[0] == self.temp_list[row][0] and row_data[1] == self.temp_list[row][1] and row_data[
                    2] == '不会':
                    row_data[2] = '已会'
                writer.writerow(row_data)


# 创建一个应用实例
app = QApplication(sys.argv)

# 创建一个窗口实例
window = MainWindow()

# 显示窗口
window.show()

# 进入应用的主循环
sys.exit(app.exec_())
