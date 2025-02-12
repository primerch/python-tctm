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
        CSVHandler.getGenerateData()
        self.window.showMaximized()
        app.exec_()

    def todayNotes(self):
        weekday = datetime.datetime.today().weekday()
        courseData = CSVHandler.load('course.csv')
        weekdayData = [data[weekday] for data in courseData]
        notesData = CSVHandler.load('notes.csv')
        showList = [data[1] for data in notesData if data[0] in weekdayData]
        self.tMenu.setTitle('提醒:' + str(showList))

    def showCourse(self):
        cusWidget = CourseWidget()
        self.window.setCentralWidget(cusWidget)

    def showNotes(self):
        notesWidget = NotesWidget()
        self.window.setCentralWidget(notesWidget)


MainApp()
