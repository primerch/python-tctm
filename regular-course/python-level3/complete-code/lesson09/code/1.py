'''

请复制下方提示词，到AI小助手中粘贴并发送：
请使用pyqt5, 生成一个带'.'和'c'的计算器程序，按钮布局要和生活中计算器一致

你也可以尝试使用以下提示词或自己编写提示词：
请使用pyqt5, 生成一备忘录界面
请使用pyqt5, 生成一个数独游戏界面，没有数字的位置用''填充
'''
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, \
    QVBoxLayout, QGridLayout, QPushButton, QLineEdit


class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Calculator')
        self.init_ui()

    def init_ui(self):
        self.textbox = QLineEdit()
        self.textbox.setReadOnly(True)
        self.textbox.setAlignment(Qt.AlignRight)
        self.textbox.setMaxLength(15)
        self.textbox.setFixedHeight(40)
        self.textbox.setStyleSheet('font-size: 18px;')

        self.buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', 'c', '+',
            '='
        ]

        grid = QGridLayout()
        grid.setSpacing(5)

        positions = [(i, j) for i in range(5) for j in range(4)]

        for position, button in zip(positions, self.buttons):
            if button == '=':
                btn = QPushButton(button)
                btn.setStyleSheet('font-size: 18px;')
                btn.clicked.connect(self.calculate)
                grid.addWidget(btn, *position, 1, 2)
            elif button == 'c':
                btn = QPushButton(button)
                btn.setStyleSheet('font-size: 18px;')
                btn.clicked.connect(self.clear)
                grid.addWidget(btn, *position)
            else:
                btn = QPushButton(button)
                btn.setStyleSheet('font-size: 18px;')
                btn.clicked.connect(self.append_text)
                grid.addWidget(btn, *position)

        vbox = QVBoxLayout()
        vbox.addWidget(self.textbox)
        vbox.addLayout(grid)

        self.setLayout(vbox)

        self.show()

    def append_text(self):
        button = self.sender()
        self.textbox.setText(self.textbox.text() + button.text())

    def clear(self):
        self.textbox.clear()

    def calculate(self):
        try:
            expression = self.textbox.text()
            result = eval(expression)
            self.textbox.setText(str(result))
        except:
            self.textbox.setText('Error')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    calculator = Calculator()
    sys.exit(app.exec_())
