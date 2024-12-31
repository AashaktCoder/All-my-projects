import pygame

pygame.init()

WIDTH, HEIGHT = 300, 350
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("TicTacToe By Aashakt")

def Text(msg):
    font = pygame.font.SysFont("Aerial", 40)
    text = font.render(msg, True, (0, 0, 0))
    WIN.blit(text, (0, 310))

def Main():
    run = True
    clock = pygame.time.Clock()
    FPS = 60

    Map = [[0,0,0],
           [0,0,0],
           [0,0,0]]        

    boxList = []
    for i in range(0, 3):
        for j in range(0, 3):
            box = [i*100, j*100, 100, 100]
            boxList.append(box)

    moreBoxList = []
    turns = 0     

    resultText = "Play Game"

    while run:
        mouse = pygame.mouse.get_pos()
        WIN.fill((255, 255, 255))
        for box in boxList: pygame.draw.rect(WIN, (0, 0, 0), box, 1)
        for box in moreBoxList: pygame.draw.rect(WIN, (0, 0, 0), box)
        Text(resultText)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    turns += 1    
                
        if pygame.mouse.get_pressed()[0]:
            if turns%2 == 0:
                for box in boxList:
                    if box[0] < mouse[0] < box[0]+100 and box[1] < mouse[1] < box[1]+100:
                        moreBox = [box[0]+25, box[1]+25, 50, 50]
                        moreBoxList.append(moreBox)
                        Map[int(box[1]/100)][int(box[0]/100)] = 1 
            if turns%2 != 0:
                for box in boxList:
                    if box[0] < mouse[0] < box[0]+100 and box[1] < mouse[1] < box[1]+100:
                        moreBox = [box[0]+40, box[1]+40, 20, 20]
                        moreBoxList.append(moreBox)
                        Map[int(box[1]/100)][int(box[0]/100)] = 2   

        if Map[0] == [1, 1, 1] or Map[1] == [1, 1, 1] or Map[2] == [1, 1, 1]: resultText = "Big Box Won"  
        if (Map[0][0] == 1 and Map[1][0] == 1 and Map[2][0] == 1) or (Map[0][1] == 1 and Map[1][1] == 1 and Map[2][1] == 1) or (Map[0][2] == 1 and Map[1][2] == 1 and Map[2][2] == 1):  resultText = "Big Box Won"  
        if (Map[0][0] == 1 and Map[1][1] == 1 and Map[2][2] == 1) or (Map[0][2] == 1 and Map[1][1] == 1 and Map[2][0] == 1): resultText = "Big Box Won" 

        if Map[0] == [2, 2, 2] or Map[1] == [2, 2, 2] or Map[2] == [2, 2, 2]: resultText = "Small Box Won"     
        if (Map[0][0] == 2 and Map[1][0] == 2 and Map[2][0] == 2) or (Map[0][1] == 2 and Map[1][1] == 2 and Map[2][1] == 2) or (Map[0][2] == 2 and Map[1][2] == 2 and Map[2][2] == 2):  resultText = "Small Box Won"  
        if (Map[0][0] == 2 and Map[1][1] == 2 and Map[2][2] == 2) or (Map[0][2] == 2 and Map[1][1] == 2 and Map[2][0] == 2): resultText = "Small Box Won" 
        pygame.display.update()
        clock.tick(FPS)

Main()                