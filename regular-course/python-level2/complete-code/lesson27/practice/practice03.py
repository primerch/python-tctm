# 课堂练习三
# 编写一个列表推导式，从字典grades中推导出一个列表，列表中包含所有及格（分数大于等于60）的学生姓名。
grades = {"小派": 80, "字符串精灵": 59, "游戏精灵": 55, "童童": 90, "字典精灵": 65}
names = [name for name, grade in grades.items() if grade > 60]
print(names)
