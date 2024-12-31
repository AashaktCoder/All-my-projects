import pygame
from time import sleep

pygame.init()

class Snake:
    def __init__(self, win, x, y, w, h, color):
        self.win = win

        self.x = x
        self.y = y
        self.w = w
        self.h = h

        self.SnakeList = [[self.x, self.y, self.w, self.h]]

        self.color = color

        self.direction = [0, 0]

    def Draw(self):
        for cell in self.SnakeList:
            pygame.draw.rect(self.win, self.color, cell)
    
    def Movement(self):
        keys = pygame.key.get_pressed()

        if (keys[pygame.K_d] and self.direction[0] == 0):
            self.direction[1] = 0
            self.direction[0] = 1
        elif (keys[pygame.K_a] and self.direction[0] == 0):
            self.direction[1] = 0
            self.direction[0] = -1
            
        if (keys[pygame.K_w] and self.direction[1] == 0):
            self.direction[0] = 0
            self.direction[1] = -1
        elif (keys[pygame.K_s] and self.direction[1] == 0):
            self.direction[0] = 0
            self.direction[1] = 1

        self.SnakeList.append([(self.SnakeList[len(self.SnakeList)-1][0]+(self.w*self.direction[0])), (self.SnakeList[len(self.SnakeList)-1][1]+(self.h*self.direction[1])), self.w, self.h])
        self.SnakeList.pop(0)
        sleep(0.1)

    def Update(self):
        self.Movement()
        self.Draw()