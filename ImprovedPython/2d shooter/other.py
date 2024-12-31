import pygame
from random import randint

class Bullet:
    def __init__(self, win, player, s, v, bl):
        self.win = win

        self.player = player

        self.size = s
        self.color = (255, 0, 0)
        self.rect = [(self.player.rect[0])+self.size//2, (self.player.rect[1])+self.size//2, self.size, self.size]

        self.speed = 8

        self.velocity = [v[0], v[1]]

        self.bulletList = bl

    def Draw(self):
        pygame.draw.rect(self.win, self.color, self.rect)
    
    def Movement(self):
        self.rect[0] += self.velocity[0]
        self.rect[1] += self.velocity[1]

    def Collision(self):
        if not(0<self.rect[0]<(self.win.get_width()-self.size)) or not(0<self.rect[1]<(self.win.get_height()-self.size)):
            self.bulletList.remove(self)
    
    def Update(self):
        self.Movement()
        self.Collision()
        self.Draw()

class Enemy:
    def __init__(self, win, el, bl):
        self.win = win

        self.x = randint(0, 470)
        self.y = randint(0, 470)

        self.rect = [self.x, self.y, 30, 30]

        self.r = randint(1, 10)/10

        self.velocity = [(2*self.r), 2*(1-self.r**2)]
        self.direction = [(self.win.get_width()//2-self.x)//abs(self.win.get_width()//2-self.x), (self.win.get_height()//2-self.y)//abs(self.win.get_height()//2-self.y)]

        self.enemyList = el
        self.bulletList = bl
    
    def Draw(self):
        pygame.draw.rect(self.win, (0, 255, 0), self.rect)

    def Movement(self):
        self.rect[0] += self.velocity[0]*self.direction[0]
        self.rect[1] += self.velocity[1]*self.direction[1]
    
    def Collision(self):
        if self.rect[0] > 470 or self.rect[0] < 0:
            self.enemyList.remove(self)
        if self.rect[1] > 470 or self.rect[1] < 0:
            self.enemyList.remove(self)

        for j in self.bulletList:
            if pygame.Rect(self.rect).colliderect(j.rect):
                self.enemyList.remove(self)
                self.bulletList.remove(j)

    def Update(self):
        self.Movement()
        self.Collision()
        self.Draw()
