import pygame
from random import randint

pygame.init()

WIDTH, HEIGHT = 300, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Piano Tiles")

def Main():
    run = True
    clock = pygame.time.Clock()
    FPS = 60

    TileList = []
    TileProbability = 0

    while run:
        mouse = pygame.mouse.get_pos()
        WIN.fill((255, 255, 255))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                quit()

        TileProbability = randint(0, 1000)
        if TileProbability > 920:
            if len(TileList) <= 10:
                Tile = [randint(0, 2)*100, randint(-200, -100), 100, 100]
                TileList.append(Tile)

        for Tiles in TileList:
            pygame.draw.rect(WIN, (0,0,0), Tiles)
        for Tiles in TileList:
            Tiles[1] += 4
            if Tiles[1] >= 400:
                TileList.remove(Tiles)
        for Tiles in TileList:    
            if Tiles[1] >= 400:
                Tiles[0] = randint(0, 2) * 100
                Tiles[1] = -100     
        for Tiles in TileList:   
            if Tiles[0] < mouse[0] < Tiles[0]+100:
                if Tiles[1] < mouse[1] < Tiles[1]+100:
                    if pygame.mouse.get_pressed()[0]:
                        TileList.remove(Tiles)

        pygame.display.update()
        clock.tick(FPS)

Main()                