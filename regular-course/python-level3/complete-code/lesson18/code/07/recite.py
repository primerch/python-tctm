import sys
import csv
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QPushButton, QHeaderView, \
    QVBoxLayout, QWidget
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor, QFont


class ReciteWords(QMainWindow):
    def __init__(self):
        super(ReciteWords, self).__init__()

        self.setWindowTitle("背单词")
        self.setGeometry(0, 0, 1200, 675)

        self.createTable()
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.tableWidget)
        self.setLayout(self.layout)

    def createTable(self):
        self.tableWidget = QTableWidget()

        # Set table dimensions
        self.tableWidget.setRowCount(15)
        self.tableWidget.setColumnCount(4)

        # Set table headers
        self.tableWidget.setHorizontalHeaderLabels(["单词", "释义", "显示释义", "标记已会"])

        # Set table header properties
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # Read data from CSV file
        self.data = []
        with open('data.csv', 'r', encoding='utf8', newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                if row[2] != '已会':
                    self.data.append(row)

        for i, row in enumerate(self.data):
            self.tableWidget.setItem(i, 0, QTableWidgetItem(row[0]))
            self.tableWidget.setItem(i, 1, QTableWidgetItem(''))
            show_button = QPushButton('显示释义')
            show_button.clicked.connect(lambda checked, row=row, i=i: self.show_meaning(row, i))
            self.tableWidget.setCellWidget(i, 2, show_button)
            mark_button = QPushButton('标记已会')
            mark_button.clicked.connect(lambda checked, row=row, i=i: self.mark_known(row, i))
            self.tableWidget.setCellWidget(i, 3, mark_button)

    def show_meaning(self, row, i):
        self.tableWidget.item(i, 1).setText(row[1])

    def mark_known(self, row, i):
        self.tableWidget.item(i, 0).setBackground(QColor('green'))
        self.tableWidget.item(i, 1).setBackground(QColor('green'))
        row[2] = '已会'
        with open('data.csv', 'w', encoding='utf8', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(self.data)

    def setLayout(self, layout):
        self.widget = QWidget()
        self.widget.setLayout(layout)
        self.setCentralWidget(self.widget)


def main():
    app = QApplication(sys.argv)
    mainWin = ReciteWords()
    app.setFont(QFont('Arial', 16))
    mainWin.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
'''

这是我的代码，不需要解读代码，等待我的下一步指示

'''
