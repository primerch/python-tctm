'''

这是我的授课思路：
问题：点击选项没反应？
解决：每当点击菜单中的切换选项时，会触发triggered事件，然后绑定事件处理函数实现功能
问题：如何切换当前作业的状态？
1. 获得表格中被选中的作业
2. 查找作业修改状态
3. 保存到csv文件
4. 读取csv文件显示到界面
删除作业和修改作业的过程类似，只需要替换列表操作即可
下面是我的代码：
    def showMenu(self):
        menu = QMenu()
        actToggle = QAction('切换作业状态')
        actDelete = QAction('删除作业')
        menu.addAction(actToggle)
        menu.addAction(actDelete)
        actToggle.triggered.connect(self.toggle)
        actDelete.triggered.connect(self.delete)
        menu.exec_(QCursor.pos())

    def delete(self):
        rowData = self.getCurrentRow()
        i = self.data.index(rowData)
        self.data.pop(i)
        CSVHandler.save('homeworks.csv', self.data)
        self.table.setRowCount(0)
        self.show()

    def toggle(self):
        rowData = self.getCurrentRow()
        i = self.data.index(rowData)
        self.data[i][3] = '已完成' if self.data[i][3] == '未完成' else '未完成'
        CSVHandler.save('homeworks.csv', self.data)
        self.table.setRowCount(0)
        self.show()

    def getCurrentRow(self):
        rowIndex = self.table.currentRow()
        rowData = []
        for col in range(4):
            rowData.append(self.table.item(rowIndex, col).text())
        return rowData
请使用中文根据以上内容，提炼知识点后出5道单选题，
帮助学员理解在作业表功能中使用右键菜单完成修改删除操作的流程，
不需要答案和解析。

'''
