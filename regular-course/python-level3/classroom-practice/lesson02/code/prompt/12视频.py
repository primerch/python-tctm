"""

这是我今天编写的代码：
```
class Fruit:
    def __init__(self, img, x, y):
        ...
        self.speedY = random.randint(30, 48)
        self.speedX = random.randint(-10, 10)

    def draw(self):
        screen.blit(self.img, (self.x, self.y))

    def move(self):
        self.y -= self.speedY
        self.speedY -= 2
        self.x -= self.speedX
fruitImgs = ['images/pineapple/full.png', 'images/orange/full.png',
             'images/pitaya/full.png', 'images/kiwi/full.png',
             'images/lemon/full.png', 'images/apple/full.png',
             'images/pomegranate/full.png', 'images/peach/full.png',
             'images/watermelon/full.png', 'images/banana/full.png',
             'images/coconut/full.png']

fruits = []
for i in range(10):
    fruit = Fruit(random.choice(fruitImgs), random.randint(100, 900), 600)
    fruits.append(fruit)


class Bomb:
    def __init__(self, img, x, y):
        ...
        self.speedY = random.randint(30, 48)
        self.speedX = random.randint(-10, 10)
    def draw(self):
        screen.blit(self.img, (self.x, self.y))
    def move(self):
        self.y -= self.speedY
        self.speedY -= 2
        self.x -= self.speedX

while True:
    ...
    for fruit in fruits:
        fruit.draw()
        fruit.move()
    bomb1.draw()
    bomb2.draw()
    bomb1.move()
    bomb2.move()

```
请详细总结今天学习的知识点


"""
