'''

帮我生成一个pyqt窗口，整个窗口的大小为1200*675，窗口表头为'背单词'
创建一个中心部件对象widget
向widget中添加布局，然后在布局中添加一个15行4列的表格
设置表头为['单词','中文释义', '显示释义', '标记已会']
使用QHeaderView.Stretch拉伸表头让表格占满窗口
将widget设置为窗口的中心部件
为每行代码添加注释

'''
# 导入必要的库
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QTableWidget, QTableWidgetItem, QHeaderView
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
