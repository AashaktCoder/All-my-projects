import pygame

pygame.init()

WIDTH, HEIGHT = 500, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("First Program")

def Main():
    run = True
    clock = pygame.time.Clock()
    FPS = 60
    PlayerX = 225
    PlayerY = 225
    Velocity = 4
    while run:
        WIN.fill((255, 255, 255))
        Player = pygame.draw.rect(WIN, (0, 255, 0), [PlayerX, PlayerY, 50,50])
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                quit()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_d]:
            PlayerX += Velocity
        if keys[pygame.K_a]:
            PlayerX -= Velocity
        if keys[pygame.K_w]:
            PlayerY -= Velocity        
        if keys[pygame.K_s]:
            PlayerY += Velocity    
        pygame.display.update()        
        clock.tick(FPS)

Main()                
