# 课堂练习3
# 编写一个程序，获取到pictures文件夹中的所有的图片，并将它们逐个输出
import os

pictures = os.listdir('pictures/cute/')
for i in pictures:
    print(i)
