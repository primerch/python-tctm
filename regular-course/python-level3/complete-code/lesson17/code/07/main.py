import datetime

from PyQt5.Qt import *
from course import CourseWidget
from notes import NotesWidget
from utils import CSVHandler


class MainApp:
    def __init__(self):
        app = QApplication([])
        self.window = QMainWindow()
        self.window.setWindowTitle("超级课程表")
        cusWidget = CourseWidget()
        self.window.setCentralWidget(cusWidget)
        self.window.showMaximized()
        self.showCourse()
        self.menubar = self.window.menuBar()
        cMenu = self.menubar.addMenu('课程表')
        nMenu = self.menubar.addMenu('备忘录')
        self.tMenu = self.menubar.addMenu('提醒')
        nAction = nMenu.addAction('查看备忘录')
        nAction.triggered.connect(self.showNotes)
        cAction = cMenu.addAction('查看课程表')
        cAction.triggered.connect(self.showCourse)
        # 老师预留好的 调用获取今日提醒的方法
        self.todayNotes()
        app.exec_()

    def todayNotes(self):
        # 1. 获取课程表数据
        courseData = CSVHandler.load('course.csv')
        # 2. 先获取今天是星期几
        weekday = datetime.datetime.today().weekday()
        # 3. 根据星期获取课程表中的课程
        weekdayData = [data[weekday] for data in courseData]
        print(weekdayData)

    def showCourse(self):
        cusWidget = CourseWidget()
        self.window.setCentralWidget(cusWidget)

    def showNotes(self):
        notesWidget = NotesWidget()
        self.window.setCentralWidget(notesWidget)


MainApp()
