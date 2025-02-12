'''

以下是我的授课思路：
问题：课程表界面和记作业界面都需要持久保存表格中修改的新数据，代码重复
解决方案：定义专门的类包含从csv文件读写数据的方法，然后分别在两个功能中直接调用
问题：这个类中的方法应该不需要创建对象，也不会用到类变量所以，更适合定义为静态方法
解决方案：在类中定义静态方法
问题：这两个方法同时被课程表和记作业功能使用，但是两个功能读写的csv文件不同，返回的数据也不同
解决方案：在静态方法中传入两个形参变量
问题：别的py文件也想用怎么办？
解决方案：提前把class预留在第三个py文件里，
然后在需要用到这个类的.py文件开头用import引入工具类后，调用类中的方法
下面是我的代码：
import csv
class CSVHandler:
    @staticmethod
    def save(fname, data):
        with open(fname, 'w', newline='', encoding='utf8') as f:
            writer = csv.writer(f)
            writer.writerows(data)

    @staticmethod
    def load(fname):
        with open(fname, 'r', encoding='utf8') as f:
            reader = csv.reader(f)
            return list(reader)

其它文件中的代码：
from utils_5 import CSVHandler
CSVHandler.save('homeworks.csv', self.data)
self.data = CSVHandler.load('homeworks.csv')

请使用中文，参考以上内容（不要简单的复述），出5道单选题，帮助学员理解消化里面的知识点

不需要答案和解析。

'''
