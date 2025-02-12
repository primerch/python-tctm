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
        # self.showCourse()
        self.showNotes()
        self.window.showMaximized()
        app.exec_()

    def showCourse(self):
        cusWidget = CourseWidget()
        self.window.setCentralWidget(cusWidget)

    def showNotes(self):
        notesWidget = NotesWidget()
        self.window.setCentralWidget(notesWidget)


MainApp()
