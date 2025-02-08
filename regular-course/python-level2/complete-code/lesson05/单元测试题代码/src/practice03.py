# 练习3
# 编写代码，实现小派跳舞的效果
# 提示：
# （1）小派跳舞的5张图片保存在列表xiaopai中
# （2）通过索引来循环绘制小派跳舞的图片
# （3）在循环中绘制背景图片bg并将小派跳舞的图片绘制在（100，100）的位置
# （4）每次循环让index的值增加1，当index的值等于4的时候，就给index重新赋值为0
# （5）每一次绘制图片延时100毫秒pygame.time.delay()
# （6）更新屏幕显示pygame.display.update()
import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((700, 800))
bg = pygame.image.load("white.png")
xiaopai1 = pygame.image.load("1.png")
xiaopai2 = pygame.image.load("2.png")
xiaopai3 = pygame.image.load("3.png")
xiaopai4 = pygame.image.load("4.png")
xiaopai5 = pygame.image.load("5.png")
xiaopai = [xiaopai1, xiaopai2, xiaopai3, xiaopai4, xiaopai5]
index = 0
while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            sys.exit()
    # 在下方编写你的代码
