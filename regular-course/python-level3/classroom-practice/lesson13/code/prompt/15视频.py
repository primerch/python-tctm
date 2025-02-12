'''

以下是我今天的代码
    def add(self):
        subject = self.subEdit.text()
        content = self.conEdit.text()
        # 如果没有输入科目和内容就不添加到表格
        if subject == '' or content == '':
            QMessageBox.warning(self, '规范输入', '请输入正确的科目和作业内容')
            return
        today = datetime.datetime.today().strftime('%Y-%m-%d')
        rowData = [today, subject, content, '未完成']
        self.addRow(rowData)
        self.subEdit.clear()
        self.conEdit.clear()

    def addRow(self, rowData):
        count = self.table.rowCount()
        self.table.insertRow(count)
        for col in range(len(rowData)):
            item = QTableWidgetItem(rowData[col])
            item.setTextAlignment(Qt.AlignCenter)
            self.table.setItem(count, col, item)
请帮我概括以上代码的功能，并提炼出其中的重要知识点

'''
