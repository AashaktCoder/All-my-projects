import pygame
from math import pi

pygame.init()

win = pygame.display.set_mode((500, 500))

run = True
clock = pygame.time.Clock()
fps = 60

r = 20

x = 250
y = 100

vx = 200
vy = 0

while run:
    ac = 0.5 * (10 * pi*r**2)/(((250-x)**2 + (250-y)**2)**0.5)

    win.fill((0, 0, 0))
    sun = pygame.draw.circle(win, (255, 255, 0), [250, 250], r)

    p = pygame.draw.circle(win, (0, 150, 255), [x, y], 5)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
            quit()

    vx += ac * ((250 - x) / (((250 - x)**2 + (250 - y)**2)**0.5))
    vy += ac * ((250 - y) / (((250 - x)**2 + (250 - y)**2)**0.5))

    x += vx * 0.1
    y += vy * 0.1

    pygame.display.update()
    clock.tick(fps)