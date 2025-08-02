import pygame
from time import sleep

pygame.init()

class Grid:
    def __init__(self, win, size):
        self.win = win
        self.size = size

    def draw(self):
        for i in range(self.win.get_height()//self.size):
            for j in range(self.win.get_width()//self.size):
                pygame.draw.rect(self.win, (255, 255, 255), [j*self.size, i*self.size, self.size, self.size], 1)     
    
    def Update(self):
        self.draw()

class Block:
    def __init__(self, win, size, bl, c, x, y, l):
        self.win = win
        self.size = size
        
        self.bl = bl
        self.c = c

        self.pos = [x, y]

        self.m = True

        self.l = l

    def Draw(self):
        for i in range(len(self.bl)):
            for j in range(len(self.bl[i])):
                if self.bl[i][j] == 1:
                    pygame.draw.rect(self.win, self.c, [self.pos[0]+(j*self.size), self.pos[1]+(i*self.size), self.size, self.size])

    def Fall(self):
        if self.m == True: self.pos[1] += self.size

    def Move(self, d):
        if self.m == True:
            self.pos[0] += self.size * d

    def Rotate(self):
        l = []
        if self.m:
            for j in range(len(self.bl[0])):
                row = []
                for i in range(len(self.bl)-1, -1, -1):
                    row.append(self.bl[i][j])
                l.append(row)
            self.bl = l
    
    def Collision(self):
        for i in range(len(self.bl)):
            for j in range(len(self.bl[i])):
                if self.pos[1]+(i*self.size) >= self.win.get_height():
                    self.pos[1] -= self.size
                    self.l.append(Block(self.win, self.size, [[0, 1, 0],[1, 1, 1]], (0, 255, 0), 0, 0, self.l))
                    self.m = False
                    return
    
    def Update(self):
        self.Fall()
        self.Collision()
        self.Draw()

class Window:
    def __init__(self, width, height, title, bgc, fps, size):
        self.width = width
        self.height = height
        self.title = title

        self.win = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption(self.title)
        self.run = True

        self.bgc = bgc

        self.clock = pygame.time.Clock()
        self.fps = fps

        self.size = size

        self.Grid = Grid(self.win, self.size)

        self.l = []

        self.l.append(Block(self.win, self.size, [[0, 1, 0],[1, 1, 1]], (0, 255, 0), 0, 0, self.l))

    def Loop(self):

        while self.run:
            self.win.fill(self.bgc)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        for b in self.l:
                            b.Rotate()
                    if event.key == pygame.K_d:
                        for b in self.l: b.Move(1)
                    if event.key == pygame.K_a:
                        for b in self.l: b.Move(-1)                

            for b in self.l:
                b.Update()
            self.Grid.Update()
            pygame.display.update()
            self.clock.tick(self.fps)
    
    def Update(self):
        self.Loop()

window = Window(300, 500, "Tetris", (0, 0, 0), 6, 20)
window.Update()