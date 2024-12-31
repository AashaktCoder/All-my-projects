from random import choice
import pygame

pygame.init()

WIDTH, HEIGHT = 240, 400
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Car Game")

class Player:
    def __init__(self, enemy):
        self.x = 14
        self.y = 340
        self.rect = [self.x, self.y, 50, 50]
        self.speed = 2 
        self.enemy = enemy

    def Draw(self):
        self.image = pygame.draw.rect(WIN, (0, 155, 255), self.rect)

    def Movement(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and self.rect[1] >= 10:
            self.rect[1] -= self.speed
        elif keys[pygame.K_s] and 340 >= self.rect[1]:
            self.rect[1] += self.speed

    def Collisions(self):
        if self.rect[0] >= 254:
            self.rect[0] = 176
        if self.rect[0] <= -14:
            self.rect[0] = 14

        if pygame.draw.rect(WIN, (0, 155, 255), self.rect).colliderect(self.enemy):
            pygame.quit()
            quit()     

    def Update(self):
        self.Movement()
        self.Collisions()
        self.Draw()    

class Enemy:
    def __init__(self):
        self.x = 96
        self.y = -60
        self.rect = [self.x, self.y, 50, 50]
        self.OldXpos = 96
        self.PosList = [14, 96, 178]

    def Draw(self):
        self.image = pygame.draw.rect(WIN, (255, 0, 80), self.rect)    

    def Movement(self):
        if self.rect[1] >= 400:
            self.rect[0] = choice(self.PosList)
            if self.rect[0] == self.OldXpos:
                self.rect[0] = choice(self.PosList)
                self.OldXpos = self.rect[0]
            self.rect[1] = -50
        self.rect[1] += 15

    def Update(self):
        self.Movement()
        self.Draw()    

def Main():
    run = True
    clock = pygame.time.Clock()
    FPS = 60

    enemy = Enemy()
    player = Player(enemy)

    while run:
        WIN.fill((255, 255, 255))
        for i in range(1, 3): pygame.draw.line(WIN, (0, 0, 0), (i*80, 0), (i*80, 400), 2)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d:
                    player.rect[0] += 82
                elif event.key == pygame.K_a:
                    player.rect[0] -= 82     

        player.Update()
        enemy.Update()
        pygame.display.update()
        clock.tick(FPS)

Main()                