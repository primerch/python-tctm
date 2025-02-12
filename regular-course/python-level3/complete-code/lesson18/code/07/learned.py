import sys
import csv

from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QHeaderView


class LearnedWords(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("显示已会单词")
        self.setGeometry(100, 100, 1200, 675)

        self.tableWidget = QTableWidget(self)
        self.tableWidget.setGeometry(0, 0, 1200, 675)
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setHorizontalHeaderLabels(["单词", "释义"])
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        with open('data.csv', 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            for row in reader:
                if len(row) >= 3 and row[2] == '已会':
                    word_item = QTableWidgetItem(row[0])
                    meaning_item = QTableWidgetItem(row[1])
                    self.tableWidget.insertRow(0)
                    self.tableWidget.setItem(0, 0, word_item)
                    self.tableWidget.setItem(0, 1, meaning_item)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mywindow = LearnedWords()
    app.setFont(QFont('Arial', 16))
    mywindow.show()
    sys.exit(app.exec_())
'''

是我的代码，不需要解读代码，等待我的下一步指示

'''
