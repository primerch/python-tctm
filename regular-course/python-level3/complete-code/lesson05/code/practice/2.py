"""

下面定义了交通工具类Vehicle，和它的两个子类：飞机类Plane和电动汽车类ElectricCar：
class Vehicle:
    def __init__(self, speed):
        self.speed = speed
    def run(self):
        print('正在行驶的速度是' + self.speed)
# 飞机类
class Plane(Vehicle):
    pass
# 电动汽车类
class ElectricCar(Vehicle):
    pass
请编写代码，完成以下要求：
1. 请给飞机类添加其独有的属性altitude，存储其飞行高度
2. 请给电动汽车类添加其独有的属性electricity, 存储其电量
注意：altitude和electricity属性值都是创建对象时传入的

"""


# 交通工具类
class Vehicle:
    def __init__(self, speed):
        self.speed = speed

    def run(self):
        print('正在行驶的速度是' + self.speed)


# 飞机类
class Plane(Vehicle):
    # 1. 给飞机类添加其独有的属性altitude，存储其飞行高度
    def __init__(self, speed, altitude):
        super().__init__(speed)
        self.altitude = altitude


# 电动汽车类
class ElectricCar(Vehicle):
    # 2. 给电动汽车类添加其独有的属性electricity, 存储其电量
    def __init__(self, speed, electricity):
        super().__init__(speed)
        self.electricity = electricity
