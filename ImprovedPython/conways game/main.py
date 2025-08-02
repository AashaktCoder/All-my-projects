import pygame
from time import sleep

pygame.init()

class Grid:
    def __init__(self, win, size):
        self.win = win
        self.size = size

    def draw(self, grid):
        for i in range(self.win.get_height()//self.size):
            for j in range(self.win.get_width()//self.size):
                if grid[i][j] == 1:
                    pygame.draw.rect(self.win, (255, 255, 255), [j*self.size, i*self.size, self.size, self.size])
                if grid[i][j] == 0:
                    pygame.draw.rect(self.win, (255, 255, 255), [j*self.size, i*self.size, self.size, self.size], 1)     

    def gridcheck(self, grid):
        newgrid = []
        for i in range(self.win.get_height()//self.size):
            newgrid.append([])
            for j in range(self.win.get_width()//self.size):
                newgrid[i].append(0)

        for i in range(1, len(grid)-1):
            for j in range(1, len(grid[i])-1):
                if grid[i][j] == 1: newgrid[i][j] = 1
                c = 0  
                if grid[i][j+1] == 1: c += 1 
                if grid[i][j-1] == 1: c += 1
                if grid[i+1][j] == 1: c += 1 
                if grid[i-1][j] == 1: c += 1
                if grid[i+1][j+1] == 1: c += 1 
                if grid[i-1][j-1] == 1: c += 1
                if grid[i+1][j-1] == 1: c += 1 
                if grid[i-1][j+1] == 1: c += 1

                if grid[i][j] == 0:
                    if c == 3: newgrid[i][j] = 1
                else:
                    if c == 2 or c == 3: newgrid[i][j] = 1
                    if c < 2 or c > 3: newgrid[i][j] = 0

        return newgrid  
    
    def Update(self, grid):
        self.draw(grid)

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
        self.gl = []
        for i in range(self.win.get_height()//self.size):
            self.gl.append([])
            for j in range(self.win.get_width()//self.size):
                self.gl[i].append(0)

        self.Grid = Grid(self.win, self.size)

        self.dt = 0.1

    def Loop(self):
        ap = False
        while self.run:
            self.win.fill(self.bgc)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p:
                        self.gl = self.Grid.gridcheck(self.gl)
                    if event.key == pygame.K_RIGHT:
                        self.dt += 0.05
                    if event.key == pygame.K_LEFT and self.dt > 0.05:
                        self.dt -= 0.05
            
            keys = pygame.key.get_pressed()
            if keys[pygame.K_a]: ap = True
            if ap:
                if keys[pygame.K_s]: ap = False
                self.gl = self.Grid.gridcheck(self.gl)
                sleep(self.dt)

            mouse = pygame.mouse.get_pos()
            if pygame.mouse.get_pressed()[0]:
                self.gl[mouse[1]//self.size][mouse[0]//self.size] = 1
            if pygame.mouse.get_pressed()[2]:
                self.gl[mouse[1]//self.size][mouse[0]//self.size] = 0

            self.Grid.Update(self.gl)
            pygame.display.update()
            self.clock.tick(self.fps)
    
    def Update(self):
        self.Loop()

window = Window(500, 500, "conways game", (0, 0, 0), 60, 10)
window.Update()