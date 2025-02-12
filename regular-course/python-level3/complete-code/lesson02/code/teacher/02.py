'''

这是我的授课思路：
在生活中投篮时篮球上升时会越来越慢然后自动下落并且速度越来越快，而程序中水果只会向上移动，并且速度不变，那怎么在程序中让水果也实现先向上减速，再向下加速
解决: 先向上减速，直到速度减到0，停止上移，speedY继续减小就变成负数,self.y-=self.speedY变为向下移动
问题：现实中，物体上抛，多少都会有水平偏移
解决: 分析水平方向也应该有一个速度，类比垂直方向运动，得出需要定义一个speedX属性来保存水平方向速度
问题：水果有向左和向右移动
解决：水平向右速度为正，水平向左速度为负，并且速度值也不同，所以需要使用随机的数值

这是我的授课代码：
class Fruit:
    def __init__(self, img, x, y):
        self.img = pygame.image.load(img)
        self.x = x
        self.y = y
        self.speedY = random.randint(30, 48)
        # 1. 定义speedX属性
        self.speedX = random.randint(-10, 10)

    def move(self):
        self.y -= self.speedY
        self.speedY -= 2
        # 2. 实现水平方向运动
        self.x -= self.speedX
请帮我使用中文，根据以上知识点出5道单选题，帮助学生理解如何实现水果上抛运动，不需要答案

'''
