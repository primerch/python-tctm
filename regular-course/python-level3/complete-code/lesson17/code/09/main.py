import datetime

from PyQt5.Qt import *
from course import CourseWidget
from homework import HomeworkWidget
from notes import NotesWidget
from search import SearchWidget
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
        hMenu = self.menubar.addMenu('作业表')
        nMenu = self.menubar.addMenu('备忘录')
        self.tMenu = self.menubar.addMenu('提醒')
        cAction = cMenu.addAction('查看课程表')
        hAction = hMenu.addAction('记作业')
        sAction = hMenu.addAction('查作业')
        nAction = nMenu.addAction('查看备忘录')
        nAction.triggered.connect(self.showNotes)
        cAction.triggered.connect(self.showCourse)
        hAction.triggered.connect(self.showHomeWork)
        sAction.triggered.connect(self.showSearch)
        self.todayNotes()
        CSVHandler.getGenerateData()
        app.setFont(QFont('Arial', 16))
        self.window.setFixedSize(1200, 675)
        self.window.show()
        # self.window.showMaximized()
        app.exec_()

    def showHomeWork(self):
        hwWidget = HomeworkWidget()
        self.window.setCentralWidget(hwWidget)

    def showSearch(self):
        searchWidget = SearchWidget()
        self.window.setCentralWidget(searchWidget)

    def todayNotes(self):
        courseData = CSVHandler.load('data/course.csv')
        weekday = datetime.datetime.today().weekday()
        weekdayData = [data[weekday] for data in courseData]
        notesData = CSVHandler.load('data/notes.csv')
        showList = [data[1] for data in notesData if data[0] in weekdayData]
        self.tMenu.setTitle('提醒:' + str(showList))

    def showCourse(self):
        cusWidget = CourseWidget()
        self.window.setCentralWidget(cusWidget)

    def showNotes(self):
        notesWidget = NotesWidget()
        self.window.setCentralWidget(notesWidget)


MainApp()
