import pygame
from random import randint

pygame.init()

WIDTH, HEIGHT = 300, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird by Aashakt")

IsJump = False

class Bird:
    def __init__(self, obstacle):
        self.x = 50
        self.y = 235
        self.rect = [self.x, self.y, 30, 30]
        self.gravity = 3
        self.FallVel = 0
        self.JumpVel = 15

        self.obstacle = obstacle

    def Draw(self):
        self.image = pygame.draw.rect(WIN, (255, 255, 255), self.rect)
        return self.image

    def Movement(self):
        global IsJump
        if IsJump:
            self.FallVel = 0
            self.gravity = 0
            self.JumpVel -= 1
            self.rect[1] -= self.JumpVel
            if self.JumpVel < 0:
                IsJump = False
                self.JumpVel = 15

    def Collision(self):
        if pygame.draw.rect(WIN, (255, 255, 255), self.obstacle[0]).colliderect(self.rect) or pygame.draw.rect(WIN, (255, 255, 255), self.obstacle[1]).colliderect(self.rect):
            pygame.quit()
            quit()

        if self.rect[1] >= 470:
            pygame.quit()
            quit()    

    def Update(self):
        global IsJump

        if not IsJump:
            if self.gravity <= 9.81:    
                self.FallVel += 0.1
                self.gravity += self.FallVel
        self.rect[1] += self.gravity   

        self.Movement()
        self.Collision()
        self.Draw()   

class Obstacle:
    def __init__(self):
        self.x1 = 350
        self.x2 = 350

        self.height1 = randint(50, 300)
        self.height2 = (350 - self.height1)

        self.y1 = (500 - self.height1)
        self.y2 = 0

        self.rect1 = [self.x1, self.y1, 50, self.height1]
        self.rect2 = [self.x2, self.y2, 50, self.height2] 

    def Collision(self):
        if self.rect1[0] <= -50:
            self.rect1[0] = 350
            self.rect2[0] = 350
            self.rect1[3] = randint(50, 300)
            self.rect2[3] = (350 - self.rect1[3])
            self.rect1[1] = (500 - self.rect1[3])

    def Movement(self):
        self.rect1[0] -= 3
        self.rect2[0] -= 3
        return [self.rect1, self.rect2]
 
    def Draw(self):
        self.image = pygame.draw.rect(WIN, (255, 255, 255), self.rect1)
        self.image2 = pygame.draw.rect(WIN, (255, 255, 255), self.rect2)   

    def Update(self):
        self.Movement()
        self.Collision()
        self.Draw()                 

def Main():
    global IsJump

    run = True
    clock = pygame.time.Clock()
    FPS = 60


    obstacle = Obstacle()

    bird = Bird(obstacle.Movement())

    while run:
        WIN.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    IsJump = True  
            if event.type == pygame.MOUSEBUTTONDOWN:
                IsJump = True        

        bird.Update()    
        obstacle.Update()    
        pygame.display.update()
        clock.tick(FPS)        

Main()                