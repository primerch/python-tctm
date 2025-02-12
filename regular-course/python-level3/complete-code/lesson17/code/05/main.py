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
        self.showNotes()
        # 1. 创建菜单栏
        self.menubar = self.window.menuBar()
        # 2. 为菜单栏添加菜单
        cMenu = self.menubar.addMenu("课程表")
        nMenu = self.menubar.addMenu("备忘录")
        self.tMenu = self.menubar.addMenu("提醒")
        self.window.showMaximized()
        app.exec_()

    def showCourse(self):
        cusWidget = CourseWidget()
        self.window.setCentralWidget(cusWidget)

    def showNotes(self):
        notesWidget = NotesWidget()
        self.window.setCentralWidget(notesWidget)


MainApp()
