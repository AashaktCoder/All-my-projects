import pygame
from Tilemap import tilemap
from Player import player

pygame.init()

class Window:
    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.win = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Platformer Game By Aashakt")

        self.run = True

        self.FPS = 60
        self.clock = pygame.time.Clock()

        self.LevelMap = [['0', '0', '0', '0', '0', '0', '0', '0', '0', '0'], ['0', '0', '1', '2', '0', '0', '0', '0', '0', '0'], ['0', '0', '1', '1', '1', '1', '0', '0', '0', '0'], ['0', '0', '1', '1', '1', '1', '1', '1', '0', '0'], ['0', '0', '0', '0', '0', '0', '0', '0', '0', '1'], ['1', '0', '0', '0', '0', '0', '0', '0', '1', '1'], ['1', '1', '0', '0', '0', '0', '0', '1', '1', '1'], ['1', '1', '1', '1', '0', '0', '1', '1', '1', '1'], ['1', '1', '1', '1', '1', '1', '1', '1', '1', '1'], ['1', '1', '1', '1', '1', '1', '1', '1', '1', '1']]

        self.Tilemap = tilemap(self.win , self.LevelMap, 50, (0, 155, 255))

        self.Player = player(self.win, 0, 250, 50, 50, self.Tilemap.MapList + self.Tilemap.MovableTiles, (0, 255, 155))

    def Loop(self):
        while self.run:
            self.win.fill((255, 255, 255))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False
                    pygame.quit()
                    quit()

            self.Tilemap.Update()
            self.Player.Update()
            pygame.display.update()
            self.clock.tick(self.FPS)
    
    def Update(self):
        self.Loop()

window = Window(500, 500)
window.Update()
