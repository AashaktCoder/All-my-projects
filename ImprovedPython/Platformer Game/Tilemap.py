import pygame

class tilemap:
    def __init__(self, win, map, tilesize, tilecolor):
        self.win = win

        self.map = map

        self.tilesize = tilesize
        self.tilecolor = tilecolor

        self.MapList = []
        self.MapList = self.MakeMap()

        self.MovableTiles = []
        self.MovableTiles = self.MoveTile()

    def MakeMap(self):
        for y, row in enumerate(self.map):
            for x, col in enumerate(row):
                X = x * self.tilesize
                Y = y * self.tilesize

                if col == '1':
                    self.MapList.append([X, Y, self.tilesize, self.tilesize])
        
        return self.MapList

    def MoveTile(self):
        for y, row in enumerate(self.map):
            for x, col in enumerate(row):
                X = x * self.tilesize
                Y = y * self.tilesize
                if col == '2':
                    self.MovableTiles.append([X, Y, self.tilesize, self.tilesize])
        
        return self.MovableTiles
    
    def Draw(self):
        for tile in self.MapList:
            pygame.draw.rect(self.win, self.tilecolor, tile)
        
        for tile in self.MovableTiles:
            pygame.draw.rect(self.win, self.tilecolor, tile)
            tile[0] += 0.5

    def Update(self):
        self.Draw()