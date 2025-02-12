"""
使用pygame库制作一个类似俄罗斯方块游戏，要求如下：

1. 创建一个400,600的游戏窗口，
2. 创建一个方块类，它有x,y坐标属性和color属性，draw方法，绘制一个宽高为20的矩形
3. 定义squareS列表，存储所有静止的方块类对象
4. 根据随机选择的颜色和选择0到380之间20倍数的坐标值，创建方块对象，存储到全局变量square中
5. 定义moveX函数，定义参数dx，遍历squareS，判断square的x坐标是否小于0或者大于400，如果是，返会False。
遍历squareS，判断其中的方块对象的x坐标是否等于square的x坐标加dx,并且y坐标是否等于square的y坐标，
如果是返回False。最后square的x坐标加等于dx
6. 定义moveY函数，声明全局变量square，判断square的y坐标是否等于580，
如果等于580，把square添加squareS中，并赋值为新的方块对象，返回False。
遍历squareS，判断其中的方块对象的x坐标是否等于square的x坐标并且y坐标减去square的y坐标是否等于20，
如果是把square添加squareS中，并赋值为新的方块对象返回False。最后square的y坐标加等于20
7. 在主循环中，设置游戏帧率为30，设置背景颜色为黑色，square对象调用draw，遍历squareS，调用draw方法
8. 当持续按下左键、右键时调用moveX方法，对应传入-20和20
9. 调用moveY函数

请只给出要求的完整代码

"""
# 1. 请使用上述提示词，编写一个俄罗斯方块游戏
import pygame
import random

pygame.init()

win_width = 400
win_height = 600
win = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption("Tetris Game")


class Square:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color

    def draw(self):
        pygame.draw.rect(win, self.color, (self.x, self.y, 20, 20))


squareS = []


def moveX(dx):
    global square
    if square.x + dx < 0 or square.x + dx > 380:
        return False
    for s in squareS:
        if s.x == square.x + dx and s.y == square.y:
            return False
    square.x += dx


def moveY():
    global square
    if square.y == 580:
        squareS.append(square)
        square = Square(random.randint(0, 19) * 20, 0,
                        (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
        return False
    for s in squareS:
        if s.x == square.x and s.y - square.y == 20:
            squareS.append(square)
            square = Square(random.randint(0, 19) * 20, 0,
                            (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
            return False
    square.y += 20


clock = pygame.time.Clock()

run = True
square = Square(random.randint(0, 19) * 20, 0, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
while run:
    clock.tick(10)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                moveX(-20)
            if event.key == pygame.K_RIGHT:
                moveX(20)

    win.fill((0, 0, 0))

    square.draw()
    for s in squareS:
        s.draw()

    if not moveY():
        moveX(0)

    pygame.display.update()

pygame.quit()
