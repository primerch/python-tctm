'''
预留代码用于拍照保存照片后执行这个代码进行测试
'''

import pygame
import sys
import cv2
import numpy as np
import csv
from deepface import DeepFace


class Compare:
    @staticmethod
    def recognize_face(image_path):
        try:
            # 使用DeepFace进行人脸识别
            result = DeepFace.represent(image_path, model_name='Facenet')
            face_array = np.array(result[0]['embedding'])
            return face_array
        except:
            return None

    @staticmethod
    def compare_face(image_path):
        # 使用Recognize中的recognize_face方法进行人脸识别
        face_array = Compare.recognize_face(image_path)

        if face_array is None:
            return '未检测到人脸'

        min_distance = 10
        best_match = '用户未识别'

        with open('data.csv', mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                person_name = row[0]
                face_data = np.array(row[1:], dtype=float)

                # 计算人脸特征之间的欧氏距离
                distance = np.linalg.norm(face_array - face_data)

                if distance < min_distance:
                    min_distance = distance
                    best_match = person_name

        return best_match


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
        if ret:
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


result = ""
while True:
    screen.blit(bg, (0, 0))
    AICam.show()

    button_rect = screen.blit(button_img, (600, 30))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            AICam.cap.release()
            cv2.destroyAllWindows()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if button_rect.collidepoint(event.pos):
                ret, frame = AICam.cap.read()
                if ret:
                    cv2.imwrite('face/temp.jpg', frame)
                    result = Compare.compare_face('face/temp.jpg')

    Utils.drawText(result, (180, 500))
    pygame.display.update()
    pygame.time.delay(80)
