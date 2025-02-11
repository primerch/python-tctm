'''
编写一个Python程序，向一个名为"message.txt"的文件写入"Hello, world!"，然后再读取这个文件的内容，并打印出来
'''

# 写方式打开文件写入内容
with open("message.txt", "w") as f:
    f.write("Hello, world!")

# 读方式打开文件读取内容
with open("message.txt", "r") as f:
    content = f.read()
    print(content)
