import pygame
from random import randint

pygame.init()

WIDTH, HEIGHT = 500, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Endless Runner By Aashakt")

class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.rect = [x, y, 50, 50]
        self.JumpCount = 10 
        self.IsJump = False
        self.negative = 1

    def Draw(self):
        pygame.draw.rect(WIN, (0, 155, 255), self.rect)

    def Jump(self): 
        keys = pygame.key.get_pressed()
        if not(self.IsJump):
            if keys[pygame.K_SPACE]:
                self.IsJump = True
        else:
            if self.JumpCount >= 0:
                self.rect[1] -= (self.JumpCount ** 2) / 2
                self.JumpCount -= 1
            else:
                self.IsJump = False
                self.JumpCount = 10

    def Gravity(self):
        if self.rect[1] <= 250:
            self.rect[1] += 6             

    def Update(self):
        self.Draw()  
        self.Jump()
        self.Gravity()      

def Text(msg, x, y):
    font = pygame.font.SysFont("Aerial", 40)
    text = font.render(msg, True, (0, 0, 0))
    WIN.blit(text, (x, y))

def Main():
    run = True
    clock = pygame.time.Clock()
    FPS = 60

    player = Player(50, 250)

    ObstacleList = []
    score = 0

    while run:
        WIN.fill((255, 255, 255))
        pygame.draw.rect(WIN, (150, 150, 150), [0, 300.5, 500, 200])
        Text(f"Score:{score}", 0, 0)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                quit()

        for Obstacles in ObstacleList:
            pygame.draw.rect(WIN, (0, 255, 155), Obstacles)
            Obstacles[0] -= 6
            if Obstacles[0] <= -50:
                ObstacleList.remove(Obstacles)
                score += 1
            if pygame.Rect(Obstacles).colliderect(player.rect):
                ObstacleList.remove(Obstacles)    
                run = False
                pygame.quit()
                quit()

        ObstacleSpawn = randint(0, 1000)
        if ObstacleSpawn > 995:
            ObstacleList.append([randint(500, 600), 270, 30, 30])

        player.Update()
        pygame.display.update()
        clock.tick(FPS)        

Main()                