import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((1000, 700))
bg = pygame.image.load("bg.png")
car = pygame.image.load("car.png")
screen.blit(bg, (0, 0))
screen.blit(car, (100, 200))
pygame.display.update()
while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            sys.exit()
