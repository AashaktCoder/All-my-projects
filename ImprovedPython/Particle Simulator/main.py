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

        self.numl = [150, 100, 50, 10]

        self.arl = [[-1, 0, 0, 5],
                    [0, 10, 10, 10],
                    [0, -2, -10, 0],
                    [-10, -10, -10, -10]]
        
        self.pml = [1, 1, 1, 10]

        for i in range(self.numl[0]):
            self.pl.append(Particle(self.win, 0, 5, 5, randint(0, self.win.get_width()-5), randint(0, self.win.get_height()-5), self.pml[0], (255, 255, 255), self.pl, self.arl))

        for i in range(self.numl[1]):
            self.pl.append(Particle(self.win, 1, 5, 5, randint(0, self.win.get_width()-5), randint(0, self.win.get_height()-5), self.pml[1], (0, 255, 0), self.pl, self.arl))

        for i in range(self.numl[2]):
            self.pl.append(Particle(self.win, 2, 5, 5, randint(0, self.win.get_width()-5), randint(0, self.win.get_height()-5), self.pml[2], (0, 0, 255), self.pl, self.arl))

        for i in range(self.numl[3]):
            self.pl.append(Particle(self.win, 3, 5, 5, randint(0, self.win.get_width()-5), randint(0, self.win.get_height()-5), self.pml[3], (255, 0, 0), self.pl, self.arl))

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

window = Window(960, 540, "Simulator", (0, 0, 0), 60)
window.Update()