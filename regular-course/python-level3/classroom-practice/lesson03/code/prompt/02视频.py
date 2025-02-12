"""


我刚学习了Python中类和对象的基础知识，并在制作水果忍者游戏中创建了水果类和炸弹类：
```
class Fruit:
    def __init__(self, img, x, y):
        self.img = pygame.image.load(img)
        self.x = x
        self.y = y
        self.speedY = random.randint(30, 48)
        self.speedX = random.randint(-10, 10)
    def draw(self):
        screen.blit(self.img, (self.x, self.y))
    def move(self):
        self.y -= self.speedY
        self.speedY -= 2
        self.x -= self.speedX

class Bomb:
    def __init__(self, img, x, y):
        self.img = pygame.image.load(img)
        self.x = x
        self.y = y
        self.speedY = random.randint(30, 48)
        self.speedX = random.randint(-10, 10)
    def draw(self):
        screen.blit(self.img, (self.x, self.y))
    def move(self):
        self.y -= self.speedY
        self.speedY -= 2
        self.x -= self.speedX
```
发现他们中有大量重复的代码，有什么办法可以简化吗？



"""
