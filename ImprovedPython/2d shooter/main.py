import pygame
from player import Player
from other import Enemy
from random import randint

pygame.init()

class Window:
    def __init__(self, w, h):
        self.w = w
        self.h = h
        self.win = pygame.display.set_mode((self.w, self.h))

        self.run = True
        self.clock = pygame.time.Clock()
        self.fps = 60

        self.player = Player(self.win, 30, 30, (0, 0, 255))

        self.enemyList = []

    def Loop(self):

        while self.run:

            self.win.fill((255, 255, 255))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False
                    pygame.quit()
                    quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        self.player.Shoot()

            for i in self.enemyList:
                i.Update()

            if 980 < randint(0, 1000) < 1000:
                enemy = Enemy(self.win, self.enemyList, self.player.bulletList)
                self.enemyList.append(enemy)

            self.player.Update()

            pygame.display.update()
            self.clock.tick(self.fps)
    
    def Update(self): self.Loop()

window = Window(500, 500)
window.Update()