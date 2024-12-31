from random import choice
import pygame

pygame.init()

WIDTH, HEIGHT = 500, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Brick Breaker By Aashakt")

class Paddle:
    def __init__(self):
        self.x = 175
        self.y = 420
        self.rect = [self.x, self.y, 150, 20]
        self.direction = 0
        self.speed = 4

    def Movement(self):
        keys = pygame.key.get_pressed()
        if (keys[pygame.K_d] or keys[pygame.K_RIGHT]) and self.rect[0] <= 350:
            self.direction = 1
        elif (keys[pygame.K_a] or keys[pygame.K_LEFT]) and self.rect[0] >= 0:
            self.direction = -1    
        else:
            self.direction = 0  
        return self.rect      

    def Draw(self):
        pygame.draw.rect(WIN, (0, 255, 0), self.rect)

    def Update(self):
        self.Movement()
        self.rect[0] += self.speed * self.direction
        self.Draw()        

class Ball:
    def __init__(self, paddle, BrickList):
        self.x = 240
        self.y = 360
        self.rect = [self.x, self.y, 20, 20]
        self.direction = [1, 1]
        self.paddle = paddle
        self.BrickList = BrickList
        
    def Draw(self):
        pygame.draw.rect(WIN, (255, 255, 255), self.rect, 0, 50)

    def Collision(self):
        if self.rect[1] <= 0:
            self.direction[0] = choice([1, 2, -1, -2])   
            self.direction[1] = 1

        if self.rect[0] >= 480:
            self.direction[0] = choice([-2, -1])    
        if self.rect[0] <= 0:
            self.direction[0] = choice([2, 1])    

        if self.rect[1] >= 480:
            self.rect[0] = 240
            self.rect[1] = 360    

        if pygame.draw.rect(WIN, (0, 255, 0), self.paddle).colliderect(self.rect):
            self.direction[0] = choice([1, 2, -1, -2])   
            self.direction[1] = -1

        for bricks in self.BrickList:
            if pygame.draw.rect(WIN, (0, 0, 255), bricks).colliderect(self.rect):
                self.direction[1] = 1
                self.direction[0] = choice([1, 2, -1, -2])  
                self.BrickList.remove(bricks)  

    def Update(self):
        self.rect[0] += self.direction[0]
        self.rect[1] += (self.direction[1] * 3)
        
        self.Collision()
        self.Draw()

class Brick:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.rect = [self.x, self.y, 92, 80]

    def Draw(self):
        pygame.draw.rect(WIN, (0, 0 , 255), self.rect)
        return pygame.draw.rect(WIN, (0, 0 , 255), self.rect)    

def Main():
    run = True
    clock = pygame.time.Clock()
    FPS = 60

    paddle = Paddle()

    BrickList = []

    for i in range(3):
        for j in range(5):
            x = j * 105
            y = i * 95
            brick = Brick(x, y)
            brickRect = brick.Draw()
            BrickList.append(brickRect)

    ball = Ball(paddle.Movement(), BrickList)

    while run:
        WIN.fill((0, 0, 0))
        for bricks in BrickList:
            pygame.draw.rect(WIN, (0, 0, 255), bricks)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                quit()

        paddle.Update()   
        ball.Update()     
        pygame.display.update()
        clock.tick(FPS)  

Main()              