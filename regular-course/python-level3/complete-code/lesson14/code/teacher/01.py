'''

这是我的授课思路：
问题：添加的作业关闭后就消失了。
解决办法：定义函数保存作业数据到csv文件
问题：添加的作业，保存到csv文件了，可是重启程序，又没了。
解决方法：启动程序时，从csv文件读取数据显示到界面。
问题：第一次运行程序时没有添加作业，作业csv文件不存在会报错
解决方法：只要从csv文件读取，都要先判断文件是否存在
问题：日积月累，csv文件中会包含很多作业，而我们今天新增的作业始终排在众多作业最后一行，很难看到
解决方法：加过滤，从csv文件中读取今天的作业
下面是我的部分代码：
        #如果文件存在才加载csv中的数据
        if os.path.exists('homeworks.csv'):
            self.data = self.load()
        #只显示今天的作业
        today = datetime.datetime.today().strftime('%Y-%m-%d')
        for rowData in self.data:
            if rowData[0] == today:
                self.addRow(rowData)
        #读取作业数据
        with open('homeworks.csv', 'r', encoding='utf8') as f:
            reader = csv.reader(f)
            return list(reader)
        #保存作业数据
        with open('homeworks.csv', 'w', encoding='utf8', newline='') as f:
            writer = csv.writer(f)
            writer.writerows(self.data)
        #生成作业数据保存并显示
        rowData = [today, subject, content, '未完成']
        self.data.append(rowData)
        self.save()
        self.addRow(rowData)
请使用中文，根据以上内容出5道单选题，帮助学员理解消化其中的代码和知识点，不需要答案和解析。


'''
