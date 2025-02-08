# 课堂练习一
# 编写代码，使用with open()语句读取text01.txt的文件，并将读取到的内容显示到控制台上
# 提示1：文件的写入操作：f.read()
# 提示2：想要显示读取到的文件中的内容，需要进行解码操作:在操作模式后添加代码：encoding= 'utf-8'
with open('text01.txt', 'r', encoding='utf-8') as f:
    content = f.read()
print(content)
