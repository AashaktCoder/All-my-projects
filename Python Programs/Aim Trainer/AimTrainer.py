import pygame
from random import randint
import time

pygame.init()

WIDTH, HEIGHT = 500, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Aim Trainer by Aashakt")

class Aim:
    def __init__(self):
        self.x = 225
        self.y = 225
        self.rect = [self.x, self.y, 50, 50]
        self.AimImg = pygame.image.load("C:\\MyFolder\\PythonProgramming\\Aim Trainer\\AimIcon.png")
        self.AimImg = pygame.transform.scale(self.AimImg, (50, 50))
        self.AccurateClicks = 0
        self.AllClicks = 0

    def Draw(self):
        pygame.draw.rect(WIN, (255, 255, 255), self.rect)
        WIN.blit(self.AimImg, (self.rect[0], self.rect[1]))
    
    def CheckClick(self):
        mouse = pygame.mouse.get_pos()
        
        if self.rect[0] < mouse[0] < (self.rect[0]+50):
            if self.rect[1] < mouse[1] < (self.rect[1]+50):
                if pygame.mouse.get_pressed()[0]:
                    self.x, self.y = randint(0, 450), randint(0, 450)
                    self.rect = [self.x, self.y, 50, 50]
                    self.AccurateClicks += 1

    def Update(self):
        self.CheckClick()
        self.Draw()

def Text(msg, x, y, size):
    font = pygame.font.SysFont("Aerial", size)
    text = font.render(msg, True, (0, 0, 0))
    WIN.blit(text, (x, y))

def Main():
    run = True
    clock = pygame.time.Clock()
    FPS = 60

    aim = Aim()
    StartTime = time.time()

    while run:
        WIN.fill((255, 255, 255))
        TimeCount = round((time.time()-StartTime))
        Text(f"Time: {TimeCount}", 0, 0, 30)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                aim.AllClicks += 1

        if TimeCount >= 10:
            EndScreen(aim.AllClicks, aim.AccurateClicks)

        aim.Update()
        pygame.display.update()
        clock.tick(FPS)

def EndScreen(AllClicks, AccurateClicks):
    run = True
    clock = pygame.time.Clock()
    FPS = 60

    while run:
        WIN.fill((255, 255, 255))
        Text("Time Up", 100, 0, 105)
        Text(f"Total Clicks: {AllClicks}", 50, 100, 40)
        Text(f"Accurate Clicks: {AccurateClicks}", 50, 140, 40)
        Text(f"Accuracy Percent: {round((AccurateClicks/AllClicks)*100)}%", 50, 180, 40)
        Text(f"Clicks Per Second: {AccurateClicks/10}", 50, 220, 40)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                quit()

        pygame.display.update()
        clock.tick(FPS)

Main()
