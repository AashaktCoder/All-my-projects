import pygame
from particle import Particle
from random import randint

pygame.init()

class Window:
    def __init__(self, width, height, title, bgc, fps):

        self.width = width
        self.height = height
        self.title = title

        self.win = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption(self.title)

        self.run = True

        self.bgc = bgc

        self.clock = pygame.time.Clock()
        self.fps = fps

        self.pl = []

        self.numl = [100, 100, 20, 0]

        self.arl = [[-1, 0.5, 0.1, 0],
                    [0.5, 0.1, -0.5, 0],
                    [1, 0.5, 0, 0],
                    [0, 0, 0, 0]]
        
        self.pml = [1, 1, 1, 1]

        self.cl = [(255, 255, 255), (0, 255, 0), (0, 0, 255), (255, 0, 0)]

        for i in range(len(self.numl)):
            for j in range(self.numl[i]):
                self.pl.append(Particle(self.win, i, 5, 5, randint(0, self.win.get_width()-5), randint(0, self.win.get_height()-5), self.pml[i], self.cl[i], self.pl, self.arl))

    def Loop(self):

        while self.run:
            self.win.fill(self.bgc)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False
                    pygame.quit()
                    quit()

            for p in self.pl:
                p.Update()

            pygame.display.update()
            self.clock.tick(self.fps)
    
    def Update(self):
        self.Loop()

window = Window(500, 500, "Simulator", (0, 0, 0), 120)
window.Update()