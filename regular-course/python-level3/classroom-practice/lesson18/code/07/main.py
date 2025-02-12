import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMenu, QMenuBar, QAction
from PyQt5.QtGui import QFont
from learned import LearnedWords
from recite import ReciteWords
from search import SearchWords


class SuperWordApp(QMainWindow):
    def __init__(self):
        super().__init__()
        # 设置窗口的标题
        self.setWindowTitle("超级背单词")
        # 设置窗口的大小
        self.setFixedSize(1200, 675)
        # 设置应用的字体
        self.setFont(QFont("Arial", 16))

        # 创建ReciteWords对象并设置为窗口的中心部件
        self.setCentralWidget(ReciteWords())

        # 创建菜单栏
        menu_bar = self.menuBar()
        # 添加'切换窗口'菜单
        switch_window_menu = QMenu('切换窗口', self)
        menu_bar.addMenu(switch_window_menu)

        # 创建菜单项
        recite_action = QAction('背单词', self)
        search_action = QAction('查单词', self)
        learned_action = QAction('已会单词', self)

        # 将菜单项添加到'切换窗口'菜单
        switch_window_menu.addAction(recite_action)
        switch_window_menu.addAction(search_action)
        switch_window_menu.addAction(learned_action)

        # 连接菜单项的triggered信号到对应的槽函数
        recite_action.triggered.connect(self.show_recite_words)
        search_action.triggered.connect(self.show_search_words)
        learned_action.triggered.connect(self.show_learned_words)

    def show_recite_words(self):
        # 创建ReciteWords对象并设置为窗口的中心部件
        self.setCentralWidget(ReciteWords())

    def show_search_words(self):
        # 创建SearchWords对象并设置为窗口的中心部件
        self.setCentralWidget(SearchWords())

    def show_learned_words(self):
        # 创建LearnedWords对象并设置为窗口的中心部件
        self.setCentralWidget(LearnedWords())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SuperWordApp()
    window.show()
    sys.exit(app.exec_())
'''

是我的代码，不需要解读代码，等待我的下一步指示

'''
