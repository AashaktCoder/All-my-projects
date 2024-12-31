import pygame
from random import choice

pygame.init()

WIDTH, HEIGHT = 600, 450
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pacman By Aashakt")

class Tilemap:
    def __init__(self, tileList):
        self.lis = tileList
        self.collisionList = []
        self.foodList = []

    def InitialDraw(self):
        for yPos, row in enumerate(self.lis):
            for xPos, col in enumerate(row):
                TileX = xPos * 25
                TileY = yPos * 25
                if col == 'X':
                    Tile = [TileX, TileY, 25, 25]
                    self.collisionList.append(Tile)
                if col == '.':
                    Food = [TileX+9.5, TileY+9.5, 6, 6]
                    self.foodList.append(Food)

        return self.collisionList, self.foodList

    def ContinousDraw(self):
        for rect in self.collisionList:
            pygame.draw.rect(WIN, (0, 0, 240), rect, 2)
        for rect in self.foodList:
            pygame.draw.rect(WIN, (245, 180, 122), rect, 0, 50)

class Player:
    def __init__(self, x, y, collideList, foodList):
        self.x = x
        self.y = y
        self.direction = [0, 0]
        self.speed = 1.2
        self.rect = [self.x+2, self.y+2, 20, 20]
        self.colList = collideList
        self.foodList = foodList

    def Draw(self):
        pygame.draw.rect(WIN, (255, 255, 0), self.rect, 0, 50)

    def Movement(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_d]:
            self.direction = [1, 0]
        if keys[pygame.K_a]:
            self.direction = [-1, 0]
        if keys[pygame.K_w]:
            self.direction = [0, -1]
        if keys[pygame.K_s]:
            self.direction = [0, 1]

    def HorizontalCollision(self):
        for rect in self.colList:
            if pygame.draw.rect(WIN,(0,0,240),rect,2).colliderect(self.rect):
                if self.direction[0] < 0:
                    self.rect[0] = rect[0] + 27.5
                    self.direction[0] = 0
                elif self.direction[0] > 0:
                    self.rect[0] = rect[0] - 22.5
                    self.direction[0] = 0

    def VerticalCollision(self):
        for rect in self.colList:
            if pygame.draw.rect(WIN,(0,0,240),rect,2).colliderect(self.rect):
                if self.direction[1] < 0:
                    self.rect[1] = rect[1] + 27.5
                    self.direction[1] = 0
                elif self.direction[1] > 0:
                    self.rect[1] = rect[1] - 22.5
                    self.direction[1] = 0

    def EatFood(self):
        for rect in self.foodList:
            if pygame.draw.rect(WIN, (245, 180, 122), rect, 0, 50).colliderect(self.rect):
                self.foodList.remove(rect)

    def Update(self):
        self.Movement()
        self.rect[0] += self.direction[0] * self.speed
        self.HorizontalCollision()
        self.rect[1] += self.direction[1] * self.speed
        self.VerticalCollision()
        self.EatFood()
        self.Draw()

class Enemy:
    def __init__(self, x, y, collideList, player):
        self.x = x
        self.y = y
        self.rect = [self.x, self.y, 20, 20]
        self.direction = [1, 0]
        self.speed = 4
        self.colList = collideList
        self.distanceFromPlayer = 0
        self.distanceDecreased = [600, 600]
        self.player = player
    
    def Draw(self):
        pygame.draw.rect(WIN, (0, 150, 255), self.rect)

    def HorizontalCollision(self):
        for rect in self.colList:
            if pygame.draw.rect(WIN,(0,0,240),rect,2).colliderect(self.rect):
                if self.direction[0] < 0:
                    self.rect[0] = rect[0] + 27.5
                elif self.direction[0] > 0:
                    self.rect[0] = rect[0] - 22.5

    def VerticalCollision(self):
        for rect in self.colList:
            if pygame.draw.rect(WIN,(0,0,240),rect,2).colliderect(self.rect):
                if self.direction[1] < 0:
                    self.rect[1] = rect[1] + 27.5
                elif self.direction[1] > 0:
                    self.rect[1] = rect[1] - 22.5

    def FindShortestDistance(self):
        if (self.rect[0] < self.distanceDecreased[0]):
            self.distanceDecreased[0] = self.rect[0]
            self.direction[0] = choice([0, 1])
        if (self.rect[1] < self.distanceDecreased[1]):
            self.distanceDecreased[1] = self.rect[1]
            self.direction[1] = choice([0, 1])

    def Update(self):
        self.rect[0] += self.direction[0] * self.speed
        self.HorizontalCollision()
        self.rect[1] += self.direction[1] * self.speed
        self.VerticalCollision()
        self.FindShortestDistance()
        self.Draw()

def Main():
    run = True
    clock = pygame.time.Clock()
    FPS = 60

    Map = ["XXXXXXXXXXXXXXXXXXXXXXXX", 
           "X.X...X....X....X.X....X", 
           "X.X.....XXXXXXX.X.XX.X.X", 
           "X.XXXX...X...X.....X.X.X", 
           "X................X.X.X.X", 
           "X.XX..X.XXX..XXX.X.X.X.X", 
           "X.X...X.X......X.XXX.X.X", 
           "X.X.X...X......X.......X", 
           "X.X.XXX.XXXXXXXX..XXXX.X", 
           "X.X.X.X............X.X.X", 
           "X.X.X.X.X..X.XXXXXXX.X.X", 
           "X.X...X.XXXX.X.X...X...X", 
           "X.XXX.X......X.X.XXXXX.X", 
           "X.....X.X..X.........X.X", 
           "X.XXXXX.X..X...X.....X.X", 
           "X.X.....X..XX..X.XXXXX.X", 
           "X.......X..X...X.......X", 
           "XXXXXXXXXXXXXXXXXXXXXXXX",]

    tileMap = Tilemap(Map)
    CollideList, FoodList = tileMap.InitialDraw()

    player = Player(25, 25, CollideList, FoodList)

    enemy = Enemy(550, 25, CollideList, player)

    while run:
        WIN.fill((0, 0, 0))
        tileMap.ContinousDraw()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                quit()
        player.Update()
        enemy.Update()
        pygame.display.update()
        clock.tick(FPS)

Main()        