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

import pygame
import sys
import cv2
import numpy as np
import os
from PIL import Image

pygame.init()
screen = pygame.display.set_mode((1100, 600))
bg = pygame.image.load("images/bg.png")
play_button = pygame.image.load("images/play.png")


class AICam:
    cap = cv2.VideoCapture(0)

    @staticmethod
    def show():
        ret, frame = AICam.cap.read()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame = np.rot90(frame)
        frame = pygame.surfarray.make_surface(frame)
        screen.blit(frame, (0, 0))


# 创建face文件夹
if not os.path.exists("face"):
    os.makedirs("face")

# 导入Recognize类
import csv
import numpy as np
from deepface import DeepFace


class Recognize:
    @staticmethod
    def recognize_face(image_path):
        try:
            result = DeepFace.represent(image_path, model_name='Facenet')
            if result is not None:
                embedding_array = np.array(result[0]['embedding'])
                return embedding_array
            else:
                return None
        except:
            return None

    @staticmethod
    def store_face(name, image_path):
        face_array = Recognize.recognize_face(image_path)
        if face_array is not None:
            with open('data.csv', mode='a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([name] + face_array.tolist())
            print("人脸信息已成功保存至data.csv文件")
        else:
            print("未能识别到人脸，请重新尝试")


while True:
    screen.blit(bg, (0, 0))
    screen.blit(play_button, (800, 200))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            AICam.cap.release()
            cv2.destroyAllWindows()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            if 800 <= x <= 950 and 200 <= y <= 350:
                name = input("请输入名字：")
                ret, frame = AICam.cap.read()
                cv2.imwrite("face/temp.jpg", frame)
                Recognize.store_face(name, "face/temp.jpg")

    AICam.show()

    pygame.display.update()
    pygame.time.delay(80)
