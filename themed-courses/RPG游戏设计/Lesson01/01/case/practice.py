# 创建父类与子类
class Animal:
    def __init__(self, kind, age):
        self.kind = kind
        self.age = age

    def eat(self):
        print('觅食')

Animal1= Animal('小羊',8)

class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed

    def bark(self):
        print('汪汪汪')

# 创建实例对象
dog1 = Dog("旺财", 3, "腊肠")

# 调用父类方法
dog1.eat()

# 调用子类方法
dog1.bark()
