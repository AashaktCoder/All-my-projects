import pygame
from math import cos, sin, pi, tan

pygame.init()

w = pygame.display.set_mode((750, 500))

run = True

angle = pi/5
u = 12

x = 0
y = 495
w.fill((255, 255, 255))
while run:

    if x < 750:
        x += u * cos(angle)

    pygame.draw.circle(w, (0, 0, 0), (x, y), 5)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
            quit()

    if y < 500:
        y = 500 - ((x * tan(angle)) - (0.2 * x**2) / (2 * (u * cos(angle))**2))

    pygame.display.update()
    pygame.time.Clock().tick(60)