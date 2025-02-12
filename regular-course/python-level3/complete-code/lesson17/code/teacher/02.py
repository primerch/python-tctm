'''


我想在主窗口界面中添加菜单栏实现子窗口的切换
添加菜单：课程表、备忘录、提醒
菜单项：查看课程表、查看备忘录
问题：如何点击菜单项切换子窗口
解决：为菜单项绑定事件，关联显示子窗口方法
这是我的授课代码：
class MainApp:
    def __init__(self):
        ...
        self.menubar = self.window.menuBar()
        cMenu = self.menubar.addMenu('课程表')
        nMenu = self.menubar.addMenu('备忘录’)
请帮我使用中文，根据以上内容出5道单选题，帮助学员理解通过菜单栏切换子窗口不需要答案。


'''
