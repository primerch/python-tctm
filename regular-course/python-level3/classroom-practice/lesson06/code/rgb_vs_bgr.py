import cv2
import pygame

pygame.init()


class AICam:
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    height, width, _ = frame.shape
    screen = pygame.display.set_mode((width, height))

    @classmethod
    def recognize(cls):
        ret, frame = cls.cap.read()
        frame = cv2.flip(frame, 1)
        cv2.imshow('AICam', frame)
        cv2.waitKey(1)
        img = pygame.surfarray.make_surface(frame)
        img = pygame.transform.rotate(img, -90)
        img = pygame.transform.flip(img, True, False)
        AICam.screen.blit(img, (0, 0))


while True:
    AICam.recognize()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            AICam.cap.release()
            cv2.destroyAllWindows()
            exit()
    pygame.display.update()
    pygame.time.delay(80)
