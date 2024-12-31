import pygame

pygame.init()

WIDTH, HEIGHT = 750, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Rpg Game By Aashakt")

class Player:
    def __init__(self, x, y, TileMap):
        self.x = x
        self.y = y
        self.speed = 4
        self.direction = [0, 0]
        self.rect = [self.x, self.y, 50, 50]
        self.TileMap = TileMap

    def Draw(self):
        self.image = pygame.draw.rect(WIN, (36, 143, 224), self.rect)

    def Movement(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.direction[0] = -1        
        elif keys[pygame.K_d]:
            self.direction[0] = 1 
        else:
            self.direction[0] = 0      
        if keys[pygame.K_w]:
            self.direction[1] = -1
        elif keys[pygame.K_s]:
            self.direction[1] = 1
        else:
            self.direction[1] = 0    

    def HorizontalCollision(self):
        for Tiles in self.TileMap:
            if Tiles.colliderect(self.rect):
                if self.direction[0] > 0:
                    self.rect[0] = (Tiles[0] - 50)
                    self.direction[0] = 0
                elif self.direction[0] < 0:
                    self.rect[0] = (Tiles[0] + 50)
                    self.direction[0] = 0

    def VerticalCollision(self):
        for Tiles in self.TileMap:
            if Tiles.colliderect(self.rect):
                if self.direction[1] > 0:
                    self.rect[1] = (Tiles[1] - 50)
                    self.direction[1] = 0
                elif self.direction[1] < 0:
                    self.rect[1] = (Tiles[1] + 50)                  
                    self.direction[1] = 0                   

    def Update(self):
        self.Movement()
        self.rect[0] += self.speed * self.direction[0]
        self.HorizontalCollision()                                 
        self.rect[1] += self.speed * self.direction[1] 
        self.VerticalCollision()
        self.Draw()

class GridSystem:
    def __init__(self, TileSize, TileList):
        self.List = TileList
        self.Size = TileSize
        self.Rect = []
        self.DrawList = []

    def InitilaizeGrid(self):
        for yPos, rows in enumerate(self.List):
            for xPos, cols in enumerate(rows):
                x = xPos * self.Size
                y = yPos * self.Size
                if cols == 1:
                    self.Rect = [x, y, self.Size, self.Size]
                    Tiles = pygame.draw.rect(WIN, (64, 64, 64), self.Rect) 
                    self.DrawList.append(Tiles)
        return self.DrawList

    def DrawGrid(self):
        for Tiles in self.DrawList:
            pygame.draw.rect(WIN, (64, 64, 64), Tiles)                

def Main():
    run = True
    clock = pygame.time.Clock()
    FPS = 60

    LevelMap = [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                [1,0,0,0,0,0,0,0,0,0,0,1,0,0,1],
                [1,0,0,1,1,1,1,1,1,0,0,1,0,0,1],
                [1,0,0,1,0,0,0,0,0,0,0,1,0,0,1],
                [1,0,0,1,0,0,0,0,0,0,0,1,0,0,1],
                [1,0,0,1,0,0,0,0,0,0,0,0,0,0,1],
                [1,1,1,1,1,1,1,1,0,0,0,0,0,1,1],
                [1,0,0,0,0,0,0,0,0,1,1,1,0,0,1],
                [1,0,0,0,0,0,0,0,0,0,0,1,0,0,1],
                [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]

    LevelSystem = GridSystem(50, LevelMap)
    TileList = LevelSystem.InitilaizeGrid()

    player = Player(350, 225, TileList)

    while run:
        WIN.fill((255, 255, 255))
        LevelSystem.DrawGrid()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                quit()

        player.Update()

        pygame.display.update()
        clock.tick(FPS)        

Main()                