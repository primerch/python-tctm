import csv
from PyQt5.Qt import *
from datetime import datetime, timedelta


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

    @staticmethod
    def addRow(table, rowData):
        count = table.rowCount()
        table.insertRow(count)
        for col in range(len(rowData)):
            item = QTableWidgetItem(rowData[col])
            item.setTextAlignment(Qt.AlignCenter)
            table.setItem(count, col, item)

    @staticmethod
    def getGenerateData():
        today = datetime.now()
        # 使用列表推导式生成日期字符串列表 日期范围是从60天前到今天为止
        date_list = [(today - timedelta(days=i)).strftime('%Y-%m-%d') for i in range(60)]
        date_list.reverse()
        # 科目为语文数学英语重复20次
        subject_list = ['语文', '数学', '英语'] * 20
        # 作业内容重复10次
        subject_content_list = ['背诵课文第二段', '做10道题', '听英语诗朗诵', '写作文', '做10道题', '预习单词'] * 10
        # 作业状态列表重复10次
        states_list = ['已完成', '已完成', '未完成', '未完成', '已完成', '已完成', '已完成', '未完成', '已完成'] * 10
        data = [[date_list[i], subject_list[i], subject_content_list[i], states_list[i]] for i in range(60)]
        CSVHandler.save('homeworks.csv', data)


# 1. 如果在当前模块运行py文件，才执行的测试代码
if __name__ == '__main__':
    print('测试读取数据功能的结果: ', CSVHandler.load('homeworks.csv'))
