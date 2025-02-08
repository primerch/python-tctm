# 课堂练习4
# 完善程序，实现按下a、s、d、f键分别出现春、夏、秋、冬四个季节的图片，并且各个图片之间可以多次任意切换
# 提示：可以设置'spring','summer','autumn'和'winter'四个状态来区分不同的场景
import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((1000, 700))
spring = pygame.image.load('spring.jpg')
summer = pygame.image.load('summer.png')
autumn = pygame.image.load('autumn.png')
winter = pygame.image.load('winter.png')
# 请在下方完善代码
