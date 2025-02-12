'''
我现在要讲解对象访问属性这个知识点。这是我的授课思路：
问题:  使用blit绘制图片，需要用到保存在属性中的值，怎么取出属性值呢
解决：用.访问对象中每个属性，属性的本质就像保存对象中的变量。除了使用时，前边必须加"对象名."，其余用法与普通变量一致
我们可以读取每个水果对象的属性，放入pygame,blit方法中绘制
问题 ：但是blit需要传入load方法加载的图片，但是现在img属性值是图片路径.修改每个对象的img属性值为load方法加载后的图片,
造成大量重复修改，易错

解决： 修改类中的初始化方法中定义的img属性值.
讲解： 对象访问属性的方法，并类比学会访问苹果对象属性，同理访问香蕉和橙子属性值

这是我的代码：
class Fruit:
    def __init__(self, img, x, y):
        # 1.修改img属性值为load方法加载的图片
        self.img = pygame.image.load(img)
        ...
while True:
# 2.访问对象属性，绘制水果图片
    screen.blit(apple.img, (apple.x, apple.y))
    screen.blit(banana.img, (banana.x, banana.y))
    screen.blit(orange.img, (orange.x, orange.y))


请帮我使用中文，根据以上知识点出5道单选题，题目尽量通俗，帮助5年级学生理解什么是对象属性，__init__函数中定义属性，
对象属性的作用，使用属性的好处，对象访问属性的语法，如何定义对象属性等，不需要答案.
'''
