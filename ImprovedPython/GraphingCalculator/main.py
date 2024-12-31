import pygame

pygame.init()

class Window:
    def __init__(self, w, h, title, bg):
        self.w = w
        self.h = h

        self.title = title

        self.win = pygame.display.set_mode((self.w, self.h))
        pygame.display.set_caption(self.title)

        self.runLoop = True
        self.fps = 60
        self.clock = pygame.time.Clock()

        self.bg = bg

    def mainLoop(self):
        while self.runLoop:
            self.win.fill(self.bg)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.runLoop = False
                    pygame.quit()
                    quit()

            pygame.display.update()
            self.clock.tick(self.fps)

    def update(self):
        self.mainLoop()

mainWindow = Window(500, 500, "Graphing Calculator By Aashakt", (255, 255, 255))
mainWindow.update()