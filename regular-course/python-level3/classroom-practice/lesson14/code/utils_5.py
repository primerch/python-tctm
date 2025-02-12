import csv


# 1. 将预留好的save()方法和load()方法封装成工具类的静态方法
def save():
    with open('homeworks.csv', 'w', newline='', encoding='utf8') as f:
        writer = csv.writer(f)
        writer.writerows(self.data)


def load():
    with open('homeworks.csv', 'r', encoding='utf8') as f:
        reader = csv.reader(f)
        self.data = list(reader)

# 2. 将读写功能修改为静态方法后，取消注释执行测试代码

# 测试save方法，运行后能看到生成新的csv文件--《test.csv》
# 测试load方法, 测试文件写入功能.csv存在 运行后能看到打印结果 [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
# 测试load方法, 测试文件写入功能.csv不存在 报错FileNotFoundError，所以要先确保文件存在才能读取数据


# data = [[1,2,3],[4,5,6],[7,8,9] ]
# CSVHandler.save('test.csv', data)
# print(CSVHandler.load('test.csv'))

# 测试完成后， 删除 或 重新注释测试代码
