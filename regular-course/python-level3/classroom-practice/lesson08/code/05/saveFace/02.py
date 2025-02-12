'''

在此基础上，我想用pygame添加一个简单的界面，在界面中点击按钮拍摄照片然后使用Recognize类中的方法保存人脸数据。
下面是我之前学过的代码：
import pygame
import sys
import cv2
import numpy as np

pygame.init()
screen = pygame.display.set_mode((1100, 600))
bg = pygame.image.load("images/bg.png")

class AICam:
    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)


while True:
    screen.blit(bg, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # 点击了退出按钮
            pygame.quit()
            AICam.cap.release()
            cv2.destroyAllWindows()
            sys.exit()


    pygame.display.update()
    pygame.time.delay(80)
请结合刚才的代码和这段代码，在此基础上为我实现4个功能：
1.AICam类中增加show函数，在while循环调用，在窗口界面的左侧实时显示摄像头拍摄画面；
2.画面右边是一个图片按钮，图片为images下的play.png；
3.当点击图片按钮时，在控制台输入名字，并拍摄摄像头画面生成图片叫temp.jpg保存在face文件夹中。
4.使用Recognize类将temp.jpg中人脸信息存储到data.csv中
请为我生成完整程序代码，包括Recognize部分。

'''
