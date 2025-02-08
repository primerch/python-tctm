# 练习2
# 编写代码，实现按下键盘上的任意键，将游戏开始界面（bg2.jpg）切换为正在进行游戏的界面(run.jpg)，并且实现点击关闭按钮时关闭窗口的功能。
# 提示：
# （1）设置变量state控制游戏状态
# （2）当state的值为begin时，就在（0，0）位置绘制bg2.jpg
# （3）获取用户事件列表pygame.event.get()并判断事件类型
# （4）当事件类型是退出QUIT时，就退出程序sys.exit()
# （5）当事件类型是键盘按下KEYDOWN时，就将state的值修改为run，并将run.jpg绘制在（0，0）的位置
# （6）更新显示：pygame.display.update()
import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((658, 507))
bg2 = pygame.image.load('bg2.jpg')
run = pygame.image.load('run.jpg')
# 请在下方完善代码
