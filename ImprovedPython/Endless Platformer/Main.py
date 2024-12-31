import pygame
from TilemapGenerator import tilemap
from Player import player

pygame.init()

class Window:
    def __init__(self):
        self.width = 1000
        self.height = 350

        self.tilesize = 25
        self.mapheight = 5

        self.win = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Endless Platformer By Aashakt")

        self.run = True

        self.FPS = 60
        self.clock = pygame.time.Clock()

        self.Tilemap = tilemap(self.win, self.tilesize, self.mapheight, (0, 155, 255))

        self.Player = player(self.win, self.win.get_width()//2, 0, self.tilesize, self.tilesize, self.Tilemap.TileList, (0, 255, 105))

    def Loop(self):
        while self.run:
            self.win.fill((255, 255, 255))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False
                    pygame.quit()
                    quit()

            self.Player.Update()
            self.Tilemap.Update()
            self.Player.collideList = self.Tilemap.TileList
            pygame.display.update()
            self.clock.tick(self.FPS)
    
    def Update(self):
        self.Loop()

window = Window()
window.Update()