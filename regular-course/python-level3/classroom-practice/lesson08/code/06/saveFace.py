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
