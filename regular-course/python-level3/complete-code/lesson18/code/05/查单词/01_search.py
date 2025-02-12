'''

帮我生成一个pyqt窗口,设置窗口标题为'查单词'
窗口使用网格布局，0，0位置显示一个输入框，占1列；0，1位置显示一个查询按钮，占1列；1，0位置是用来显示查询结果的文本区域，占2列
整个窗口的大小为1200*675，输入框的宽度为600，高度为50，按钮的宽度为200，高度为50
为每行代码添加注释

'''
# 导入所需的库
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QTextEdit, QGridLayout
from PyQt5.QtCore import Qt


# 创建一个类，继承自QWidget
class WordQueryWindow(QWidget):
    def __init__(self):
        super().__init__()

        # 设置窗口标题
        self.setWindowTitle('查单词')
        # 设置窗口大小
        self.resize(1200, 675)

        # 使用网格布局
        layout = QGridLayout(self)

        # 创建输入框
        self.inputBox = QLineEdit(self)
        # 设置输入框大小
        self.inputBox.setFixedSize(600, 50)
        # 将输入框添加到布局，位置为0，0，占1列
        layout.addWidget(self.inputBox, 0, 0, 1, 1)

        # 创建查询按钮
        self.queryButton = QPushButton('查询', self)
        # 设置按钮大小
        self.queryButton.setFixedSize(200, 50)
        # 将按钮添加到布局，位置为0，1，占1列
        layout.addWidget(self.queryButton, 0, 1, 1, 1)

        # 创建用于显示查询结果的文本区域
        self.resultArea = QTextEdit(self)
        # 将文本区域添加到布局，位置为1，0，占2列
        layout.addWidget(self.resultArea, 1, 0, 1, 2)


# 创建应用实例
app = QApplication([])

# 创建窗口实例
window = WordQueryWindow()

# 显示窗口
window.show()

# 进入应用的主循环
app.exec_()
