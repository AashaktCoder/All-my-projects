import pygame
from random import randint

pygame.init()

WIDTH, HEIGHT = 500, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Endless Jumper By Aashakt")

class Player:
    def __init__(self, x, y, spawnPlat):
        self.x = x
        self.y = y
        self.rect = [self.x, self.y, 40, 40]
        self.speed = 4
        self.direction = [0, 0]
        self.OnPlatform = True
        self.Colliding = True
        self.CanJump = True
        self.JumpCount = 12
        self.spawnPlat = spawnPlat
    
    def Draw(self):
        pygame.draw.rect(WIN, (65, 156, 217), self.rect, border_radius=8)

    def Movement(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_d] and self.rect[0] <= (WIDTH-self.rect[2]):
            self.direction[0] = 1
        elif keys[pygame.K_a] and self.rect[0] >= 0:
            self.direction[0] = -1
        else:
            self.direction[0] = 0

        if keys[pygame.K_SPACE] and self.CanJump:
            if not(self.OnPlatform):
                for plat in self.platList:
                    plat[1] = plat[1] + 10
            if self.CanJump:
                if self.JumpCount >= 0:
                    neg = 1
                    if self.JumpCount < 0:
                        neg = -1
                    self.rect[1] -= (self.JumpCount ** 2) * 0.5 * neg
                    self.JumpCount -= 1
                else:
                    self.CanJump = False
                    self.JumpCount = 10

            self.OnPlatform = False
            self.Colliding = False
            self.spawnPlat() 

    def Gravity(self):
        self.rect[1] += 4

    def Collision(self, platList, ground):
        for plat in platList:
            if pygame.draw.rect(WIN, (52, 163, 54), plat).colliderect(self.rect):
                if plat[0] < (self.rect[0]+self.rect[2]) < (plat[0] + plat[2]+40):
                    if plat[1] >= (self.rect[1]+self.rect[3]-5):
                        self.OnPlatform = True
                        self.Colliding = True
                        self.CanJump = True
                        self.rect[1] = plat[1] - self.rect[3]
            else: self.Colliding = False

        if not(self.Colliding):
            self.OnPlatform = False

        if ground.colliderect(self.rect):
            pygame.quit()
            quit()

    def Update(self, platList, ground):
        self.platList = platList
        self.Movement()
        self.rect[0] += self.direction[0] * self.speed
        if not(self.OnPlatform): self.Gravity()
        self.Collision(platList, ground)
        self.Draw()

class Platforms:
    def __init__(self):
        self.platformList = [[0, 460, WIDTH, 10]]
        self.SpawnInitialPlatform()
    
    def Draw(self):
        for platform in self.platformList:
            pygame.draw.rect(WIN, (52, 163, 54), platform)

    def SpawnInitialPlatform(self):
        for i in range(1, 6):
            self.platformList.append([randint(100, 300), 460-(i*100), 100, 10])

    def SpawnPlatforms(self):
        self.platformList.append([randint(100, 300), self.platformList[len(self.platformList)-1][1]-120, 100, 10])

    def Update(self):
        self.Draw()
        for plat in self.platformList:
            if plat[1] >= 480:
                self.platformList.remove(plat)
        return self.platformList

def Main():
    run = True
    clock = pygame.time.Clock()
    FPS = 60

    platforms = Platforms()

    player = Player(225, 419, platforms.SpawnPlatforms)

    while run:
        WIN.fill((255, 255, 255))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                quit()

        platformList = platforms.Update()
        Ground = pygame.draw.rect(WIN, (176, 114, 67), [0, 460, 500, 40])
        player.Update(platformList, Ground)
        pygame.display.update()
        clock.tick(FPS)

Main()