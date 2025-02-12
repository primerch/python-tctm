from PyQt5.Qt import *
from course import CourseWidget
# 1. 导入备忘录子窗口
from notes import NotesWidget


class MainApp:
    def __init__(self):
        app = QApplication([])
        self.window = QMainWindow()
        self.window.setWindowTitle("超级课程表")
        cusWidget = CourseWidget()
        self.window.setCentralWidget(cusWidget)
        self.showCourse()
        # 3. 调用方法显示子窗口
        self.showNotes()
        self.window.showMaximized()
        app.exec_()

    # 2. 定义方法添加子窗口对象
    def showNotes(self):
        notesWidget = NotesWidget()
        self.window.setCentralWidget(notesWidget)

    def showCourse(self):
        cusWidget = CourseWidget()
        self.window.setCentralWidget(cusWidget)


MainApp()
