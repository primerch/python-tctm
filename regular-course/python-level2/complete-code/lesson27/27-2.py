# 编写一个列表推导式，将给定字符串列表中的字符串长度超过3个字符的字符串提取出来，生成一个新的字符串列表。
words = ['apple', 'dog', 'cherry', 'date', 'fig']
newWords = [word for word in words if len(word) > 3]
print(newWords)
