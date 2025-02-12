"""
使用pyqt5编写生成一周食谱的应用程序，要求如下：
1. 定义三个全局列表变量分别存储10种中餐主食、菜品和汤粥的真实中文名字
2. 创建食谱主窗口，添加网格布局，设置窗口大小为1200,500
3. 在网格布局中第1行第2列添加一个按钮控件，占据1行1列
4. 设置按钮高为50px，设置按钮文本为“生成一周食谱“，字体大小为20px
5. 在网格布局的第二行中添加一个3行7列的表格控件，占据1行3列
6. 设置表格控件的行表头项标签内容是星期一到星期日,并设置行表头项水平填充满
7. 设置列表头标签内容是早餐，午餐和晚餐，并设置列表头项垂直填充满
8. 设置表格中文本大小为18px，并且允许文本在单元格内换行
9. 当点击“生成一周食谱”按钮时，从主食列表、菜品列表和汤粥列表中随机挑选1个主食、2个菜品和1个汤粥，其中2个菜品不能相同
10. 把选择主食、菜品和汤粥进行换行后放置在每个单元格中

请输出要求的完整代码

"""
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont
import random

# 全局食品变量
main_food = ['米饭', '面条', '饺子', '包子', '馒头', '炒饭', '炒面', '糯米饭', '粥', '蒸饼']
dish = ['红烧排骨', '鱼香肉丝', '宫保鸡丁', '番茄牛腩', '酸辣白菜', '红烧桂鱼', '孜然肋排', '叉烧肉', '羊肉串',
        '串烧肠']
soup = ['老母鸡汤', '鲫鱼豆腐汤', '苦瓜猪肝汤', '冬瓜骨头汤', '西红柿鸡蛋汤', '牛腩萝卜汤', '菠菜豆腐汤', '归肉羹',
        '海鲜汤', '萝卜鸡蛋汤']


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("一周食谱")
        self.setGeometry(100, 100, 1200, 500)
        self.UI()

    def UI(self):
        layout = QGridLayout()
        generate_btn = QPushButton("生成一周食谱")
        generate_btn.setFixedHeight(50)
        generate_btn.setFont(QFont('Arial', 20))
        generate_btn.clicked.connect(self.generate)
        layout.addWidget(generate_btn, 0, 1)

        table = QTableWidget()
        table.setRowCount(3)
        table.setColumnCount(7)
        table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        table.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)
        table.setHorizontalHeaderLabels(['星期一', '星期二', '星期三', '星期四', '星期五', '星期六', '星期日'])
        table.setVerticalHeaderLabels(['早餐', '午餐', '晚餐'])
        table.setFont(QFont('Arial', 18))
        table.setWordWrap(True)

        layout.addWidget(table, 1, 0, 1, 3)
        self.setLayout(layout)

    def generate(self):
        for j in range(7):
            for i in range(3):
                main = random.choice(main_food)
                dish1, dish2 = random.sample(dish, 2)
                soup1 = random.choice(soup)
                recipe = f"{main}\n{dish1}\n{dish2}\n{soup1}"
                self.layout().itemAtPosition(1, 0).widget().setItem(i, j, QTableWidgetItem(recipe))


def main():
    App = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(App.exec_())


if __name__ == "__main__":
    main()
