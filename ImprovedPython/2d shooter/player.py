import pygame
from other import Bullet

class Player:
    def __init__(self, win, w, h, color):
        self.win = win

        self.w = w
        self.h = h

        self.x = (self.win.get_height() - self.w) // 2
        self.y = (self.win.get_height() - self.h) // 2

        self.rect = [self.x, self.y, self.w, self.h]
        self.color = color

        self.speed = [3, 3]

        self.bulletList = []

    def Draw(self):
        pygame.draw.rect(self.win, self.color, self.rect)

        for i in self.bulletList:
            i.Update()

    def Movement(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_d] and self.rect[0] <= (self.win.get_width()-self.rect[2]): self.rect[0] += self.speed[0]
        elif keys[pygame.K_a] and self.rect[0] >= 0: self.rect[0] -= self.speed[0]
        if keys[pygame.K_s] and self.rect[1] <= (self.win.get_height()-self.rect[3]): self.rect[1] += self.speed[1]
        elif keys[pygame.K_w] and self.rect[1] >= 0: self.rect[1] -= self.speed[1]  

    def Shoot(self):
        if pygame.mouse.get_pressed()[0]:

            mouse = pygame.mouse.get_pos()
            velocity = [(mouse[0] - (self.rect[0] + self.w // 2)) / ((mouse[0] - (self.rect[0] + self.w // 2))**2 + (mouse[1] - (self.rect[1] + self.h // 2))**2)**0.5 * 10, 
            (mouse[1] - (self.rect[1] + self.h // 2)) / ((mouse[0] - (self.rect[0] + self.w // 2))**2 + (mouse[1] - (self.rect[1] + self.h // 2))**2)**0.5 * 10]

            bullet = Bullet(self.win, self, 10, velocity, self.bulletList)

            self.bulletList.append(bullet)

    def Update(self):
        self.Movement()
        self.Draw()      