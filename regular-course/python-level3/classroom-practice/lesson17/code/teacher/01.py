'''


我有两个子窗口，分别是课程表子窗口，备忘录子窗口，我想把这两个子窗口添加到主窗口中
问题：子窗口代码分别保存在不同的文件里，该如何在别的程序中使用
解决：
1. 在主窗口中使用 from course import CourseWidget 导入子窗口
2. 创建子窗口对象添加到主窗口中
3. 在主窗口中加载时显示子窗口
问题：可是在启动时会同时运行两个窗口
解决：if __name__ == '__main__':

这是我的授课代码：
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
        self.window.showMaximized()
        app.exec_()

    def showCourse(self):
        cusWidget = CourseWidget()
        self.window.setCentralWidget(cusWidget)

    def showNotes(self):
        notesWidget = NotesWidget()
        self.window.setCentralWidget(notesWidget)

MainApp()

if __name__ == '__main__':


请帮我使用中文，根据以上内容出5道单选题，帮助学员理解和消化多窗口应用程序概念，不需要答案。


'''
