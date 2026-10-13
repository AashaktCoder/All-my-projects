import pygame

pygame.init()

class Window:
    def __init__(self, w, h):
        self.w = w
        self.h = h

        self.win = pygame.display.set_mode((self.w, self.h))
        self.run = True
        self.fps = 60

        self.templist = []
        self.boxlist = []

        for i in range(self.w//self.h):
            self.templist.append(0)
            self.boxlist.append([i * self.h, 0, self.h, self.h])

        self.tempchange = 10

    def Loop(self):
        while self.run:
            mouse = pygame.mouse.get_pos()

            self.win.fill((0, 0, 0))

            for i in self.boxlist:
                if self.templist[i[0]//self.h] > 0:
                    pygame.draw.rect(self.win, (self.templist[i[0]//self.h], 0, 0), i)
                if self.templist[i[0]//self.h] < 0:
                    pygame.draw.rect(self.win, (0, 0, abs(self.templist[i[0]//self.h])), i)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False
                    pygame.quit()
                    quit()
                
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1 and self.templist[mouse[0]//self.h] + self.tempchange < 255:
                        self.templist[mouse[0]//self.h] += self.tempchange
                    if event.button == 3 and self.templist[mouse[0]//self.h] - self.tempchange > -255:
                        self.templist[mouse[0]//self.h] -= self.tempchange

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_w: self.tempchange += 5
                    if event.key == pygame.K_s: self.tempchange -= 5

            pygame.display.update()
            pygame.time.Clock().tick(self.fps)
    
    def Update(self):
        self.Loop()

window = Window(500, 25)
window.Update()