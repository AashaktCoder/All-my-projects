import pygame
from math import sin

pygame.init()

w, h = 1000, 500
win = pygame.display.set_mode((w, h))
pygame.display.set_caption("Sin Wave Simulator")

clock = pygame.time.Clock()

x = 0
y = 212

direction = 1

amplitude = 100
waveLength = 10
speed = 0.1
xPos = x * waveLength
yPos = 212

LineList = []

while True:
    win.fill((255, 255, 255))
    pygame.draw.rect(win, (0, 155, 255), [xPos, y, 25, 25])
    
    LineList.append([xPos+12.5, y+12.5, 2, 2])
    for Line in LineList: pygame.draw.rect(win, (0,0,0), Line)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    x += (speed * direction)
    xPos = x * waveLength

    y = yPos + (amplitude * sin(x))

    if xPos >= w: direction = -1
    if xPos <= -12: direction = 1

    pygame.display.update()
    clock.tick(60)
