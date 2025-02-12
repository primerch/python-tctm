'''

继续为刚才的窗口添加查询功能，当按钮点击时：
1. 检查输入框中是否有要查询的文字，如果没有文字，在下方文本区域显示 "请输入查询内容"
2. 如果输入的内容在data.csv中不存在，在下方文本区域显示 "没有查询到结果"
3. 如果输入的内容在data.csv中存在，如果输入的是中文，显示对应的英文单词，如果输入的是英文单词，显示对应的中文翻译
4. 设置所有文字大小20并加粗
要求使用csv模块操作，注意文件编码为utf8。
data.csv文件的格式是中英文对照，第一列是英文单词，第二列是中文翻译。
为每行代码添加注释

'''
# 导入所需的库
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QTextEdit, QGridLayout
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
import csv


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

        # 设置所有文字大小为20并加粗
        font = QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.inputBox.setFont(font)
        self.queryButton.setFont(font)
        self.resultArea.setFont(font)

        # 连接查询按钮的点击信号到查询函数
        self.queryButton.clicked.connect(self.query)

    def query(self):
        # 获取输入框中的文字
        text = self.inputBox.text()

        # 检查输入框中是否有要查询的文字
        if not text:
            # 如果没有文字，在下方文本区域显示 "请输入查询内容"
            self.resultArea.setText('请输入查询内容')
            return

        # 读取csv文件
        with open('data.csv', 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            for row in reader:
                # 如果输入的内容在data.csv中存在
                if text == row[0] or text == row[1]:
                    # 如果输入的是中文，显示对应的英文单词
                    if text == row[1]:
                        self.resultArea.setText(row[0])
                        return
                    # 如果输入的是英文单词，显示对应的中文翻译
                    elif text == row[0]:
                        self.resultArea.setText(row[1])
                        return

        # 如果输入的内容在data.csv中不存在，在下方文本区域显示 "没有查询到结果"
        self.resultArea.setText('没有查询到结果')


# 创建应用实例
app = QApplication([])

# 创建窗口实例
window = WordQueryWindow()

# 显示窗口
window.show()

# 进入应用的主循环
app.exec_()
