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

        self.showCourse()
        self.menubar = self.window.menuBar()
        cMenu = self.menubar.addMenu('课程表')
        nMenu = self.menubar.addMenu('备忘录')
        self.tMenu = self.menubar.addMenu('提醒')
        cAction = cMenu.addAction('查看课程表')
        nAction = nMenu.addAction('查看备忘录')
        nAction.triggered.connect(self.showNotes)
        cAction.triggered.connect(self.showCourse)
        self.todayNotes()
        self.window.showMaximized()
        app.exec_()

    def todayNotes(self):
        courseData = CSVHandler.load('course.csv')
        weekday = datetime.datetime.today().weekday()
        weekdayData = [data[weekday] for data in courseData]
        # 1. 获取备忘录数据

        # 2. 筛选出当天的课程需要提醒的内容

        # 3. 在菜单栏中显示字符串格式的提醒内容

    def showCourse(self):
        cusWidget = CourseWidget()
        self.window.setCentralWidget(cusWidget)

    def showNotes(self):
        notesWidget = NotesWidget()
        self.window.setCentralWidget(notesWidget)


MainApp()
