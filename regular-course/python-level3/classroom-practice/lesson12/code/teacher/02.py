'''
我想使用csv模块来对course.csv文件进行读写
以下是我的授课代码
self.data = [...]
一、将self.data写入到csv文件中
with open('course.csv', 'w', encoding='utf8', newline='') as f:
      # 创建writer对象
      writer = csv.writer(f)
      # 将self.data的数据写入到csv文件
      writer.writerows(self.data)

二、从csv文件中读取数据到self.data中，为防止文件不存在报错，在读取之前先对文件进行判断是否存在
# 判断文件是否存在
if os.path.exists('course.csv'):
    # 打开course.csv文件准备读取，设置编码格式为utf8
    with open('course.csv', 'r', encoding='utf8') as f:
        # 读取csv文件
        reader = csv.reader(f)
        # 将读取的课程信息转换为二维列表赋值给self.data
        self.data = list(reader)
请帮我使用中文，根据以上内容出5道单选题，帮助学员理解和消化使用csv模块读取course.csv文件不需要答案。
'''
