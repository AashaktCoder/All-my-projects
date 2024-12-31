from ast import Delete
import pygame
from random import randint

pygame.init()

WIDTH, HEIGHT = 500, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dodger Game By Aashakt")

def Text(msg, x, y):
    font = pygame.font.SysFont("Aerial", 45)
    text = font.render(msg, True, (255, 255, 255))
    WIN.blit(text, (x, y))

def Main():
    run = True
    clock = pygame.time.Clock()
    FPS = 60
    
    Velocity = 4
    PlayerX = 225
    PlayerHealth = 10
    Score = 0
    Gravity = 5

    ObjList = []

    while run:
        WIN.fill((0, 0, 0))

        Player = pygame.draw.rect(WIN, (50, 100, 255), [PlayerX, 425, 50, 50])

        Text(f"Health: {PlayerHealth}", 0, 0)
        Text(f"Score: {Score}", 180, 0)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                quit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_d] and PlayerX <= 450:
            PlayerX += Velocity
        if keys[pygame.K_a] and PlayerX >= 0:
            PlayerX -= Velocity

        # Creating Obstacles
        ObjSpawnRate = randint(0, 1000)
        if (ObjSpawnRate > 920):
            ObjSize = randint(10, 50)
            Obj = [randint(0, 450), 50, ObjSize, ObjSize]
            ObjList.append(Obj)     

        # Moving the Obstacles and Collisions
        for obj in ObjList:
            pygame.draw.rect(WIN, (0, 255, 0), obj)    
            if (obj[1] >= (500 - obj[3])):
                ObjList.remove(obj)
                Score += 1

            if (Player.colliderect(obj)):
                ObjList.remove(obj)
                PlayerHealth -= 1 

            obj[1] += Gravity        

        if (PlayerHealth <= 0):
            run = False
            pygame.quit()
            quit()

        pygame.display.update()
        clock.tick(FPS)        

Main()            