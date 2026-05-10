import pygame

pygame.init()

class Window:
    def __init__(self, w, h):  
        self.w = w
        self.h = h

        self.win = pygame.display.set_mode((self.w, self.h))

        self.run = True
        self.clock = pygame.time.Clock()
        self.fps = 60

    def Loop(self):
        while self.run:
            self.win.fill((0, 0, 0))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False
                    pygame.quit()
                    quit()

            pygame.display.update()
            self.clock.tick(self.fps)
    
    def Update(self): self.Loop()

window = Window(500, 500)
window.Update()