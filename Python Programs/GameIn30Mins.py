from random import choice
import pygame

pygame.init()

WIDTH, HEIGHT = 750, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

GoToRandom = False

class Player:
    def __init__(self):
        self.rect = [225, 300, 50, 50]
        self.ApplePosList = [82, 282, 482, 682]

    def Draw(self):
        pygame.draw.rect(WIN, (16, 140, 31), self.rect)    

    def Movement(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_d]:
            self.rect[0] += 10
        if keys[pygame.K_a]:
            self.rect[0] -= 10

    def Collision(self, apple):
        global GoToRandom
        if apple.colliderect(self.rect):
            GoToRandom = True

    def Update(self, apple):
        self.Movement()
        self.Collision(apple)
        self.Draw()

class Tree:
    def __init__(self, x):
        pygame.draw.rect(WIN, (94, 64, 19), [x + 65, 175, 40, 175])
        pygame.draw.rect(WIN, (25, 189, 44), [x, 20, 175, 175])

def Main():
    global GoToRandom

    run = True
    clock = pygame.time.Clock()
    FPS = 60

    ApplePosList = [82, 282, 482, 682]
    AppleX = choice(ApplePosList)
    AppleY = 100

    player = Player()

    while run:
        WIN.fill((30, 190, 255))
        Ground = pygame.draw.rect(WIN, (128, 66, 0), [0, 350, 750, 150])
        Tree(200)
        Tree(400)
        Tree(600)
        Tree(0)
        Apple = pygame.draw.rect(WIN, (252, 59, 0), [AppleX, AppleY, 25, 25])
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                quit()
        
        AppleY += 4
        if AppleY >= 475:
            AppleY = 100
            AppleX = choice(ApplePosList)

        if GoToRandom:
            AppleY = 100
            AppleX = choice(ApplePosList)
            GoToRandom = False   

        player.Update(Apple)
        pygame.display.update()
        clock.tick(FPS)

Main()                