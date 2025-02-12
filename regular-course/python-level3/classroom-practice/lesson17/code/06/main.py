from PyQt5.Qt import *
from course import CourseWidget
from notes import NotesWidget


class MainApp:
    def __init__(self):
        app = QApplication([])
        self.window = QMainWindow()
        self.window.setWindowTitle("超级课程表")
        cusWidget = CourseWidget()
        self.window.setCentralWidget(cusWidget)
        self.showCourse()
        # 注释代码 先显示课程表不显示备忘录 通过菜单查看备忘录
        # self.showNotes()
        self.menubar = self.window.menuBar()
        cMenu = self.menubar.addMenu('课程表')
        nMenu = self.menubar.addMenu('备忘录')
        self.tMenu = self.menubar.addMenu('提醒')
        # 老师预留的 查看备忘录选项
        nAction = nMenu.addAction('查看备忘录')
        nAction.triggered.connect(self.showNotes)

        # 1. 为菜单添加可选项

        # 2. 为'查看课程表'绑定事件切换课程表界面

        self.window.showMaximized()
        app.exec_()

    def showCourse(self):
        cusWidget = CourseWidget()
        self.window.setCentralWidget(cusWidget)

    def showNotes(self):
        notesWidget = NotesWidget()
        self.window.setCentralWidget(notesWidget)


MainApp()
