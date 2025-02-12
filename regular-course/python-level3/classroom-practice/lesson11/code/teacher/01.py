'''
我想自定义一个CourseWidget类来显示课程信息添加到主窗口中
问题：自定义的类不具备添加到主窗口的功能
解决：使用自定义的类继承自QWidget类
问题：如何显示课程信息
解决：通过QTableWidget(13,7)来创建13行7列的表格添加到布局中来显示课程信息
问题：创建的表格看不出是课程表
解决：为表格添加水平表头和垂直表头

以下是我的授课代码
class CourseWidget(QWidget):
    def __init__(self):
        super().__init__()
        layout = QGridLayout()
        self.setLayout(layout)
        self.table = QTableWidget(13, 7)
        layout.addWidget(self.table)
        # 1. 设置水平表头
        weeks = ['星期一', '星期二', '星期三', '星期四', '星期五', '星期六', '星期日']
        self.table.setHorizontalHeaderLabels(weeks)
        # 2. 设置垂直表头
        hours = ['08:00', '09:00', '10:00', '11:00', '12:00', '13:00', '14:00', '15:00', '16:00',
                 '17:00', '18:00', '19:00', '20:00', ]
        self.table.setVerticalHeaderLabels(hours)

widget = CourseWidget()
window.setCentralWidget(widget)



请帮我使用中文，根据以上内容出5道单选题，帮助学员理解和消化自定义Widget类和表格控件概念，不需要答案。
'''
