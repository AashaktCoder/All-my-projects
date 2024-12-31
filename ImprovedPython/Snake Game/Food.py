import pygame
from random import choice

class Food:
    def __init__(self, win, w, h, color):
        self.win = win
        
        self.w = w
        self.h = h
        self.XposList = []
        self.YposList = []
        for i in range(self.win.get_width()):
            if i%self.w == 0: self.XposList.append(i)
        for j in range(self.win.get_height()):
            if j%self.h == 0: self.YposList.append(j)

        self.x = choice(self.XposList)
        self.y = choice(self.YposList)

        self.rect = [self.x, self.y, self.w, self.h]

        self.color = color
    
    def Draw(self):
        pygame.draw.rect(self.win, self.color, self.rect)
    
    def Collision(self, SnakeList, direction):
        for cell in SnakeList:
            if pygame.Rect(self.rect).colliderect(cell):
                self.rect[0] = choice(self.XposList)
                self.rect[1] = choice(self.YposList)
                SnakeList.append([(SnakeList[len(SnakeList)-1][0]+(self.w*direction[0])), (SnakeList[len(SnakeList)-1][1]+(self.h*direction[1])), self.w, self.h])

    def Update(self, SnakeList, direction):
        self.Collision(SnakeList, direction)
        self.Draw()