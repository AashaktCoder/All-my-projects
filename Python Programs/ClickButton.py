import pygame

pygame.init()

WIDTH, HEIGHT = 500, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("A button clicker game")

def Text(msg, x, y, color, size):
    font = pygame.font.SysFont("Aerial", size)
    text = font.render(msg, True, color)
    WIN.blit(text, (x, y))

def Main():
    run = True
    bColor = (0, 155, 255)
    pos = [195, 220]
    tPos = [210, 232]
    score = 0

    while run:
        mouse = pygame.mouse.get_pos()
        
        WIN.fill((255, 255, 255))
        backButton = pygame.draw.rect(WIN, (0, 110, 210), [199, 224, 100, 50], 0, 8)
        button = pygame.draw.rect(WIN, bColor, [pos[0], pos[1], 100, 50], 0, 8)
        Text("Click", tPos[0], tPos[1], (255, 255, 255), 40)
        Text(f"Score: {score}", 145, 30, (0, 0, 0), 75)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                quit()  
            if 195 < mouse[0] < 295 and 220 < mouse[1] < 270:
                if event.type == pygame.MOUSEBUTTONDOWN: score += 1    

        if 195 < mouse[0] < 295 and 220 < mouse[1] < 270:
            bColor = (0, 145, 245)
            if pygame.mouse.get_pressed()[0]:
                pos = [199, 224]
                tPos = [214, 236]
            else:
                pos = [195, 220]
                tPos = [210, 232] 
        else: bColor = (0, 155, 255) 

        pygame.display.update()

Main()                