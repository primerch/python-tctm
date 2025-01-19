# 课堂练习3
# 编写程序，实现一个单词反转游戏。
# 要求：
# 1.使用切片的相关知识实现一个用于接收反转后的单词的函数reverse_words(word)
# 2.使用 with open 和 pickle.dump 将原始的单词保存到文件中，文件名为word.pkl。
# 3.使用 try/except 进行检查，若存在保存的单词文件，则使用 with open 和 pickle.load 加载原始单词；
#   若出现 FileNotFoundError 错误，则提示用户输入一个单词。
# 4.在程序结束时，使用 with open 和 pickle.dump 将新生成的单词保存到文件中，覆盖原来的单词。
#
# 提示：
# 1. [::-1] 表示对序列进行逆向遍历
# 2. 'rb'：以二进制格式打开一个文件用于只读；'wb'：以二进制格式打开一个文件只用于写入
# 在下方编写你的代码
import pickle
def reverse_words(word):
    words = word[0:]
    reversed_words = words[::-1]
    words=reversed_words
    return words

# 检查是否存在保存的单词文件，并加载原始单词
try:
    with open('word.pkl', 'rb') as f:
        word = pickle.load(f)
except FileNotFoundError:
    word = input("请输入一个单词：")

# 输出原始单词供测试
print("原始单词:", word)

# 反转单词并输出反转后的单词
reversed_word = reverse_words(word)
print("反转后的单词:", reversed_word)

# 保存新生成的单词
with open('word.pkl', 'wb') as f:
    pickle.dump(reversed_word, f)


