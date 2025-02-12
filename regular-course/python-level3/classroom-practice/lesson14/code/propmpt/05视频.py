'''

def load(self):
    with open('homeworks.csv', 'r', encoding='utf8') as f:
        reader = csv.reader(f)
        self.data = list(reader)

为什么这段代码运行后会报错
FileNotFoundError: [Errno 2] No such file or directory: 'homeworks.csv'
请帮我分析问题出现的原因

'''
