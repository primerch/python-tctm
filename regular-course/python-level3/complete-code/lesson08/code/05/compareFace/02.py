"""

在此基础上，我想用pygame添加一个简单的界面，在界面中点击按钮拍摄照片,
然后使用Compare类中的方法比对照片中人脸与data.csv中的数据。
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

class Utils:
    @staticmethod
    def drawText(text, pos):
        font = pygame.font.Font('fonts/WRYH.TTF', 40)
        textImg = font.render(str(text), True, 'orange')
        screen.blit(textImg, pos)


while True:
    screen.blit(bg, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            AICam.cap.release()
            cv2.destroyAllWindows()
            sys.exit()


    pygame.display.update()
    pygame.time.delay(80)
请结合刚才的代码和这段代码，在此基础上为我实现5个功能：
1.AICam类中增加show函数，在while循环调用，在窗口界面的左侧实时显示摄像头拍摄画面；
2.画面右边是一个图片按钮位置是（600,30），图片为images下的button.png；
3.当点击图片按钮区域时，拍摄当前摄像头画面，并生成图片temp.jpg保存在face文件夹中。
4.使用Compare类比对拍摄的照片中人脸信息和在data.csv文件中的人脸信息，判断打卡人是谁。
5.如果比对成功则在（180,500）位置写文字，显示对应人名，比对不成功则显示：没有识别到人员信息。
注意：可以定义一个变量result初始为空字串,保存识别结果，这样让文字要一直显示直到下一次比对再更换
请为我生成完整程序代码，包括Compare部分。

"""

import pygame
import sys
import cv2
import numpy as np
from deepface import DeepFace
import csv

pygame.init()
screen = pygame.display.set_mode((1100, 600))
bg = pygame.image.load("images/bg.png")
button_img = pygame.image.load("images/button.png")


class AICam:
    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

    @staticmethod
    def show():
        ret, frame = AICam.cap.read()
        print(frame.shape)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame = np.rot90(frame)
        frame = pygame.surfarray.make_surface(frame)
        screen.blit(frame, (0, 0))


class Utils:
    @staticmethod
    def drawText(text, pos):
        font = pygame.font.Font('fonts/WRYH.TTF', 40)
        textImg = font.render(str(text), True, 'orange')
        screen.blit(textImg, pos)


class Compare:

    @staticmethod
    def recognize_face(image_path):
        try:
            result = DeepFace.represent(image_path, model_name='Facenet')
            face_array = np.array(result[0]['embedding'])
            return face_array
        except:
            return None

    @staticmethod
    def compare_face(image_path):
        face_array = Compare.recognize_face(image_path)

        if face_array is None:
            return '未检测到人脸'

        min_distance = 10
        recognized_person = "用户未识别"

        with open('data.csv', 'r') as file:
            csv_reader = csv.reader(file)
            for row in csv_reader:
                target_face = np.array(row[1:], dtype=np.float64)
                distance = np.linalg.norm(face_array - target_face)
                if distance < min_distance:
                    min_distance = distance
                    recognized_person = row[0]

        if min_distance <= 10:
            return recognized_person
        else:
            return '用户未识别'


result = ""

while True:
    screen.blit(bg, (0, 0))
    AICam.show()

    button_rect = button_img.get_rect(topleft=(600, 30))
    screen.blit(button_img, button_rect)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            AICam.cap.release()
            cv2.destroyAllWindows()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if button_rect.collidepoint(event.pos):
                ret, frame = AICam.cap.read()
                cv2.imwrite('face/temp.jpg', frame)
                result = Compare.compare_face('face/temp.jpg')

    if result:
        Utils.drawText(result, (180, 500))

    pygame.display.update()
    pygame.time.delay(80)
