import pygame
import sys
import time

pygame.init()
screen = pygame.display.set_mode((1000, 700))
bg = pygame.image.load("bg.png")
car = pygame.image.load("car.png")
car1 = pygame.image.load("car1.png")
car2 = pygame.image.load("car2.png")
screen.blit(bg, (0, 0))
cars = [car, car1, car2]
index = 0
x = 100
y = 200
while True:
    screen.blit(bg, (0, 0))
    screen.blit(cars[index], (x, y))
    pygame.display.update()
    index = index + 1
    if index == 3:
        index = 0
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            sys.exit()
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_RIGHT:
                x = x + 10
            if e.key == pygame.K_LEFT:
                x = x - 10
            if e.key == pygame.K_UP:
                y = y - 10
            if e.key == pygame.K_DOWN:
                y = y + 10
