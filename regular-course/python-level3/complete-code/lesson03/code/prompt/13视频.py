"""

这是我今天编写的代码：
```
class FlyObject:
    def __init__(self, img, x, y):
        self.img = pygame.image.load(img)
        w, h = self.img.get_size()
        self.centerX = x + w / 2
        self.centerY = y + h / 2
        self.speedY = random.randint(30, 48)
        self.speedX = random.randint(-10, 10)
        self.angle = 0
    def draw(self):
        if self.speedX < 0:
            self.angle -= 5
        else:
            self.angle += 5
        self.newImg = pygame.transform.rotate(self.img, self.angle)
        self.rect = self.newImg.get_rect(center=(self.centerX, self.centerY))
        screen.blit(self.newImg, self.rect)
    def move(self):
        self.centerY -= self.speedY
        self.speedY -= 2
        self.centerX -= self.speedX
class Fruit(FlyObject):
    pass
class Bomb(FlyObject):
    pass
class Knife:
    ...
    def move(self):
        mouseX,mouseY = pygame.mouse.get_pos()
        self.x = mouseX - 60
        self.y = mouseY - 60
knife = Knife("images/knife.png", 550, 300)
while True:
    ...
    knife.draw()
    knife.move()

```
请详细总结今天学习的知识点


"""
