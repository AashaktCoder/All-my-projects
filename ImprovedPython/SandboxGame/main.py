import pygame

pygame.init()

class Window:
    def __init__(self, height, width, colour, title, tilesize, gridcolour):
        self.width = width
        self.height = height
        
        self.win = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption(title)

        self.colour = colour

        self.run = True
        self.fps = 20
        self.clock = pygame.time.Clock()

        self.tilesize = tilesize
        self.gridcolour = gridcolour

        self.brushsize = 1
        self.brushcolour = (140, 140, 140)

        self.grid = []
        for i in range(self.height//self.tilesize[1]):
            self.grid.append([])
            for j in range(self.width//self.tilesize[0]):
                self.grid[i].append(0)

        self.elementlist = [(0, 0, 0), (235, 218, 73), (0, 0, 255)]

    def DrawGrid(self):
        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                pygame.draw.rect(self.win, self.gridcolour, [j*self.tilesize[0],i*self.tilesize[1], self.tilesize[0],self.tilesize[1]], 1)

    def DrawBrush(self, mouse):
        for i in range(-(self.brushsize//2), self.brushsize//2 + 1):
            for j in range(-(self.brushsize//2), self.brushsize//2 + 1):

                if ((i)**2 + (j)**2)**0.5 <= self.brushsize/2:
                    pygame.draw.rect(self.win, self.brushcolour, [self.tilesize[0] * ((mouse[0]//self.tilesize[0]) + j), self.tilesize[1] * ((mouse[1]//self.tilesize[1]) + i), self.tilesize[0], self.tilesize[1]])
    
    def DrawElement(self):
        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                    pygame.draw.rect(self.win, self.elementlist[self.grid[i][j]], [j*self.tilesize[0],i*self.tilesize[1], self.tilesize[0],self.tilesize[1]])

    def PlaceElement(self, mouse):
        for i in range(-(self.brushsize//2), self.brushsize//2 + 1):
            for j in range(-(self.brushsize//2), self.brushsize//2 + 1):
                try:
                    if ((i)**2 + (j)**2)**0.5 <= self.brushsize/2:
                        self.grid[((mouse[1]//self.tilesize[1]) + i)][((mouse[0]//self.tilesize[0]) + j)] = 1
                except: pass
    
    def DeleteElement(self, mouse):
        for i in range(-(self.brushsize//2), self.brushsize//2 + 1):
            for j in range(-(self.brushsize//2), self.brushsize//2 + 1):
                try:
                    if ((i)**2 + (j)**2)**0.5 <= self.brushsize/2:
                        self.grid[((mouse[1]//self.tilesize[1]) + i)][((mouse[0]//self.tilesize[0]) + j)] = 0
                except: pass

    def ElementGravity(self):

        for i in range(len(self.grid)-2, -1, -1):
            for j in range(len(self.grid[i])):
                if self.grid[i][j] > 0:
                    try:
                        if self.grid[i+1][j] == 0:
                            self.grid[i+1][j] = self.grid[i][j]
                            self.grid[i][j] = 0
                        
                        if self.grid[i+1][j+1] == 0:
                            self.grid[i+1][j+1] = self.grid[i][j]
                            self.grid[i][j] = 0
                        if self.grid[i+1][j-1] == 0:
                            self.grid[i+1][j-1] = self.grid[i][j]
                            self.grid[i][j] = 0
                    except: pass

    def Loop(self):
        while self.run:
            mouse = pygame.mouse.get_pos()

            self.win.fill(self.colour)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False
                    pygame.quit()
                    quit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_w:
                        self.brushsize += 1
                    if event.key == pygame.K_s:
                        self.brushsize -= 1

            if pygame.mouse.get_pressed()[0]:
                self.PlaceElement(mouse)
            if pygame.mouse.get_pressed()[2]:
                self.DeleteElement(mouse)

            self.DrawElement()
            self.DrawBrush(mouse)
            self.DrawGrid()

            self.ElementGravity()

            pygame.display.update()
            self.clock.tick(self.fps)
    
    def Update(self):
        self.Loop()

window = Window(500, 500, (0, 0, 0), "Sandbox Game", (20, 20), (255, 255, 255))
window.Update()