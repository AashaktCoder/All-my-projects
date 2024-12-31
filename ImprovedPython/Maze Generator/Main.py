import pygame

pygame.init()

pygame.display.set_mode((500, 500))

class window:
    def __init__(self, w, h, title):
        self.w = w
        self.h = h
        self.title = title

        self.run = True
        self.clock = pygame.time.Clock()
        self.fps = 60

        self.win = pygame.display.set_mode((self.w, self.h))

        self.grid = Grid(self.w, self.h, 25, self.win)

    def makeWindow(self):
        self.win = pygame.display.set_mode((self.w, self.h))
        pygame.display.set_caption(self.title)

    def windowLoop(self):
        while self.run:

            self.win.fill((0, 0, 0))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False
                    pygame.quit()
                    quit()

            self.grid.update()
            pygame.display.update()
            self.clock.tick(self.fps)
    
    def runWindow(self):
        self.makeWindow()
        self.windowLoop()

class Grid:
    def __init__(self, w, h, s, win):
        self.w = w
        self.h = h

        self.s = s

        self.win = win
    
    def generate(self):
        for i in range(self.w//self.s):
            for j in range(self.h//self.s):
                    pygame.draw.line(self.win, (0, 255, 0), (j*self.s, i*self.s), (self.s*(j+1), self.s*(i)))
                    pygame.draw.line(self.win, (0, 255, 0), (i*self.s, j*self.s), (i*self.s, self.s*(j+1)))

        for i in range(self.h//self.s):pygame.draw.line(self.win, (0, 255, 0), (499, i*self.s), (499, (i+1)*self.s))
        for i in range(self.w//self.s):pygame.draw.line(self.win, (0, 255, 0), (i*self.s, 499), ((i+1)*self.s, 499))
    
    def update(self):
        self.generate()

win = window(500, 500, "Maze Generator")
win.runWindow()