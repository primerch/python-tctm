"""

这是我今天编写的代码：
```
class Juice:
    def __init__(self, img):
        self.img = pygame.image.load(img)
        self.centerX = None
        self.centerY = None
    def draw(self):
        rect = self.img.get_rect(center=(self.centerX, self.centerY))
        screen.blit(self.img, rect)
class Fruit(FlyObject):
    def __init__(self, img, x, y):
        super().__init__(img, x, y)
        self.juice = Juice(img.replace('full.png', 'juice.png'))
    def bang(self):
        super().bang()
        self.juice.centerX = self.centerX
        self.juice.centerY = self.centerY
    def draw(self):
        if self.isCut:
            self.juice.draw()
        super().draw()
class Game:
    bg = pygame.image.load("images/bg.png")
    fruitImgs = ['images/pineapple/full.png', 'images/orange/full.png',
                ...
                ]
    fruits = []
    bomb = Bomb('images/bomb/full.png', random.randint(100, 900), 600)
    knife = Knife('images/knife.png', 550, 300)
for i in range(10):
    fruit = Fruit(random.choice(Game.fruitImgs), random.randint(100, 900), 600)
    Game.fruits.append(fruit)

```
请根据代码详细总结今天学习的所有有关类和对象的知识点


"""
