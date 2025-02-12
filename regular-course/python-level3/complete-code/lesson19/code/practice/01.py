# 1. 导入math模块
import math

# 2. 定义一个scores列表，存储学生成绩
scores = [80, 75, 90, 85, 95, 85, 90, 85, 95, 85]
# 3. 计算学生成绩的总分、平均分、最高分，并输出
result = sum(scores)
print("总分：", result)
result = result / len(scores)
print("平均分：", result)
result = max(scores)
print("最高分：", result)


# 4. 定义一个circle函数，和接收圆半径的参数r，计算圆形面积和周长
def circle(r):
    # 5.1 计算圆形面积
    area = math.pi * r * r
    # 5.2 计算圆形周长
    perimeter = 2 * math.pi * r
    # 5.3 输出圆形面积和周长
    print("圆形面积：", area)
    print("圆形周长：", perimeter)


# 5. 调用circle函数，计算半径为5的圆的面积和周长
circle(5)
