import pygame
from random import randint

class tilemap:
    def __init__(self, win, tilesize, maxheight, tilecolor):
        self.win = win

        self.tilesize = tilesize
        self.tilecolor = tilecolor

        self.maxheight = maxheight
        
        self.MapList = []
        self.MapList = self.NewMap()

        self.Chunks = []
        self.Chunks.append(self.NewMap())
        self.Chunks.append(self.NewMap())

        self.TileList = []
        self.TileList = self.DrawMap()

    def NewMap(self):
        self.MapList = []

        for i in range(self.win.get_height()//self.tilesize):self.MapList.append([])
        for j in range(self.win.get_height()//self.tilesize):
            for i in range(self.win.get_width()//self.tilesize):
                self.MapList[j].append('0')
            
        self.MapList = self.MakeMap()

        return self.MapList

    def MakeMap(self):
        for i in range(len(self.MapList[0])):
            y = randint((((self.win.get_height()-self.tilesize))//self.tilesize) - self.maxheight, (((self.win.get_height()-self.tilesize))//self.tilesize) - 1)
            
            self.MapList[y][i] = '1'

            for j in range(y, (self.win.get_height()//self.tilesize)):
                self.MapList[j][i] = '1'

        return self.MapList
    
    def DrawMap(self):
        for MapList in self.Chunks:
            for y, i in enumerate(MapList):
                for x, j in enumerate(i):
                    if j == '1':
                        self.TileList.append([(x*self.tilesize)+(self.win.get_width()*self.Chunks.index(MapList)), (y*self.tilesize), self.tilesize, self.tilesize])

        return self.TileList

    def Draw(self):
        for tile in self.TileList:
            pygame.draw.rect(self.win, self.tilecolor, tile)

    def GenerateChunk(self):
        if (self.TileList[len(self.TileList)-1][0]) <= (self.win.get_width()-self.tilesize):
            self.Chunks.pop(0)
            self.Chunks.append(self.NewMap())
            self.TileList = []
            self.TileList = self.DrawMap()

    def Update(self):
        self.GenerateChunk()
        self.Draw()