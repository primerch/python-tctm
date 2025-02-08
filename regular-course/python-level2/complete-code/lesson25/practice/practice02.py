# 课堂练习二
# 编写代码，使用with open()语句创建一个名为poetry.txt的文件，并将古诗《小池》写入到文件中
# 提示1：文件的写入操作：f.write()
# 提示2：创建好的文件可以打开本地文件查看
poetry = '''
              《小池》
            泉眼无声惜细流，
            树阴照水爱晴柔。
            小荷才露尖尖角，
            早有蜻蜓立上头。
         '''
with open('poetry.txt', 'w') as f:
    f.write(poetry)
