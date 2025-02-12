'''
请帮我使用pyqt5实现一个物品栏效果，要求如下：
1. 创建一个宽755，高1005的窗口，并设置窗口标题为物品栏
2. 在窗口中添加一个5行5列的表格，隐藏水平表头，隐藏垂直表头，隐藏分割线
3. 向表格中添加单元格，每个单元格内都有一个独立的widget，设置垂直布局，在上方用QLabel显示图片，下方用QLabel显示文字
4. 图片保存在images目录下，图片名为IMG (1).png ~ IMG (25).png共25张图
5. 图片下方文字字体大小16px，设置文字居中对齐，内容为1~100直接的随机数，双击当前单元格时文字数量-1
6. 设置表格中单元格水平拉抻，垂直拉抻均分表格
'''
import sys
import random
from PyQt5.QtWidgets import QApplication, QWidget, QTableWidget, QTableWidgetItem, QVBoxLayout, QLabel, QHeaderView
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtCore import Qt, QSize


class ItemWidget(QWidget):
    def __init__(self, img, text):
        super().__init__()
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.label_img = QLabel()
        self.label_img.setPixmap(QPixmap(img))
        self.layout.addWidget(self.label_img)

        self.label_text = QLabel()
        self.label_text.setFont(QFont('Arial', 16))
        self.label_text.setAlignment(Qt.AlignCenter)
        self.label_text.setText(str(text))
        self.layout.addWidget(self.label_text)

    def decrease(self):
        text = int(self.label_text.text())
        if text > 0:
            self.label_text.setText(str(text - 1))


class ItemTable(QTableWidget):
    def __init__(self):
        super().__init__()
        self.setRowCount(5)
        self.setColumnCount(5)
        self.setFixedSize(QSize(755, 1005))
        self.setShowGrid(False)
        self.horizontalHeader().setVisible(False)
        self.verticalHeader().setVisible(False)
        self.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)
        for i in range(5):
            for j in range(5):
                img = f'images/IMG ({i * 5 + j + 1}).png'
                text = random.randint(1, 100)
                item = ItemWidget(img, text)
                self.setCellWidget(i, j, item)

    def mouseDoubleClickEvent(self, event):
        item = self.cellWidget(self.currentRow(), self.currentColumn())
        if item is not None:
            item.decrease()


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('物品栏')
        self.layout = QVBoxLayout()
        self.layout.addWidget(ItemTable())
        self.setLayout(self.layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())
