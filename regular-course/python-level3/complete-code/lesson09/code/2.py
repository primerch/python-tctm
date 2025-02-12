# 1. 导入PyQt5中提供的功能
from PyQt5.Qt import *

# 2. 创建应用程序
app = QApplication([])
# 创建主窗口
window = QMainWindow()
# 显示主窗口
window.show()
# 执行应用程序
app.exec_()
