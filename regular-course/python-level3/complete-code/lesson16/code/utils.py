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


# 1. 如果在当前模块运行py文件，才执行的测试代码
if __name__ == '__main__':
    print('测试读取数据功能的结果: ', CSVHandler.load('homeworks.csv'))
