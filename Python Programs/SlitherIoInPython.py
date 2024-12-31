import pygame
from random import randint

pygame.init()

WIDTH, HEIGHT = 500, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Slither Io By Aashakt")

class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.rect = [self.x, self.y, 50, 50]
        self.speed = 2

    def Draw(self):
        pygame.draw.rect(WIN, (0, 155, 255), self.rect, 0, int(self.rect[3]))

    def Movement(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_d] and self.rect[0] <= WIDTH-self.rect[2]:
            self.rect[0] += self.speed
        elif keys[pygame.K_a] and self.rect[0] >= 0:
            self.rect[0] -= self.speed          
        if keys[pygame.K_w] and self.rect[1] >= 0:
            self.rect[1] -= self.speed
        elif keys[pygame.K_s] and self.rect[1] <= WIDTH-self.rect[3]:
            self.rect[1] += self.speed

    def Update(self):
        self.Movement()
        self.Draw()                      

class Food:
    def __init__(self, x, y, w, h, color):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.rect = [self.x, self.y, self.w, self.h]
        self.color = color
        self.collided = False

    def Draw(self):
        pygame.draw.rect(WIN, self.color, self.rect, 0, 50)

    def Collision(self, playerRect):
        if pygame.draw.rect(WIN, self.color, self.rect, 0, 50).colliderect(playerRect):
            playerRect[2] += (self.w - 10)/20
            playerRect[3] += (self.h - 10)/20
            self.collided = True

    def CheckCollision(self):
        return self.collided

    def Update(self, playerRect):
        self.Collision(playerRect)
        self.Draw()    

def Main():
    run = True
    clock = pygame.time.Clock()
    FPS = 60

    player = Player(225, 225)

    NoOfFood = randint(20, 40)
    FoodList = []

    for i in range(NoOfFood):
        w = randint(10, 20)
        h = w
        food = Food(randint(0, WIDTH-w), randint(0, HEIGHT-h), w, h, (randint(0,255), randint(0, 255), randint(0, 255)))
        FoodList.append(food)

    while run:
        WIN.fill((255, 255, 255))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                quit()

        player.Update()
        for f in FoodList:
            f.Update(player.rect)
            c = f.CheckCollision()
            if c:
                FoodList.remove(f)
                w = randint(10, 20)
                h = w
                food = Food(randint(0, WIDTH-w), randint(0, HEIGHT-h), w, h, (randint(0,255), randint(0, 255), randint(0, 255)))
                FoodList.append(food)
        pygame.display.update()
        clock.tick(FPS)

Main()                        