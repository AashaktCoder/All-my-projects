import pygame
from player import Player
from random import randint

pygame.init()

class Tiles:
    def __init__(self, win):
        self.win = win
        self.tl = []
        for i in range(1, 5):
            self.tl.append([randint(0, 420), 500-i*120, 100, 10])
    
    def Draw(self):
        for i in self.tl:
            pygame.draw.rect(self.win, (0, 255, 100), i)

    def Movement(self):
        for i in self.tl:
            i[1] += 1
            if self.tl[0][1] >= 450:
                self.tl.remove(self.tl[0])
                self.tl.append([randint(0, 400), 0, 100, 10])

    def Update(self):
        self.Movement()
        self.Draw()

class Window:
    def __init__(self):
        self.w = 500
        self.h = 500

        self.win = pygame.display.set_mode((self.w, self.h))

        self.run = True
        self.clock = pygame.time.Clock()
        self.fps = 60

        self.tiles = Tiles(self.win)
        self.player = Player(self.win, self.tiles.tl)

    def Update(self):
        while self.run:
            self.win.fill((255, 255, 255))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False
                    pygame.quit()
                    quit()
            
            self.player.Update()
            self.tiles.Update()
            pygame.draw.rect(self.win, (176, 108, 40), [0, 450, 500, 50])
            pygame.display.update()
            self.clock.tick(self.fps)

window = Window()
window.Update()            