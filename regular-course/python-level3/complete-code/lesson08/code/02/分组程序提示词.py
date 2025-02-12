'''

我要用python完成一个抽签小程序，功能如下：
1.运行程序需要先在控制台输入一个数字n
2.用pygame做界面，界面大小为1100 * 600，界面背景是images/bg.png, 界面中随机位置有n个苹果图片images/apple.png，注意苹果图片不要超出界面范围
3.当点击任意一个苹果图片后，在这个位置立即显示1-n中任意一个数字且数字会一直显示。注意所有苹果产生的数字不重复。我的字体文件是fonts/WRYH.TTF，要求文字大小事40，颜色为白色
请为我生成完整代码

'''

'''

如果结果不理想可追问 ： 

数字为什么闪一下就消失了，我需要数字一直显示

'''

import pygame
import random

# Initialize pygame
pygame.init()

# Set up display
screen = pygame.display.set_mode((1100, 600))
pygame.display.set_caption("抽签小程序")

# Load images
background = pygame.image.load("images/bg.png")
apple_img = pygame.image.load("images/apple.png")

# Load font
font = pygame.font.Font("fonts/WRYH.TTF", 40)


# Function to display number on apple
def display_number(x, y, number):
    text = font.render(str(number), True, (255, 255, 255))
    screen.blit(text, (x, y))


# Main function
def draw_apples(n):
    numbers = random.sample(range(1, n + 1), n)
    apples = []
    display_numbers = [False] * n
    for _ in range(n):
        x = random.randint(0, 1100 - apple_img.get_width())
        y = random.randint(0, 600 - apple_img.get_height())
        apples.append((x, y))

    running = True
    while running:
        screen.blit(background, (0, 0))

        for i in range(n):
            screen.blit(apple_img, apples[i])
            if display_numbers[i]:
                display_number(apples[i][0] + 20, apples[i][1] + 20, numbers[i])

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                for i in range(n):
                    if apples[i][0] <= mouse_pos[0] <= apples[i][0] + apple_img.get_width() and apples[i][1] <= \
                            mouse_pos[1] <= apples[i][1] + apple_img.get_height():
                        display_numbers[i] = True

        pygame.display.update()

    pygame.quit()


# Get user input for number of apples
n = int(input("请输入苹果的数量："))
draw_apples(n)
