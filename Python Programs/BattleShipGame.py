from random import choice
import pygame
from pygame import mixer

pygame.init()
mixer.init()

WIDTH, HEIGHT = 500, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Battle Ship Game by Aashakt")
Icon = pygame.image.load("C:\\MyFolder\\BattleShipIcon.png")
pygame.display.set_icon(Icon)

totalNoOfTurns = 15
turns = totalNoOfTurns
ResultText = ""
HasWon = False
IsReset = False

mixer.music.set_volume(0.1)

class GridBox:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.color = (0, 0, 0)

    def Draw(self):
        pygame.draw.rect(WIN, self.color, [self.x, self.y, 100, 100], 3)

    def ClickGrid(self, mouse, Box):
        global turns
        global ResultText
        global HasWon
        if ((self.x+100) > mouse[0] > self.x) and ((self.y+100) > mouse[1] > self.y):
            if pygame.mouse.get_pressed()[0]:
                if (Box.x == self.x) and (Box.y == self.y):
                    self.color = (0, 255, 0)  
                    pygame.draw.rect(WIN, self.color, [self.x, self.y, 100, 100], 3)
                    ResultText = "You Won !!"
                    HasWon = True
                else:
                    if (self.color == (0, 0, 0)) and not HasWon:
                        if (turns >= 1):
                            turns -= 1 
                            mixer.music.load("BattleShip.wav")
                            mixer.music.play()
                    self.color = (255, 0, 0) 
                    pygame.draw.rect(WIN, self.color, [self.x, self.y, 100, 100], 3)         

def Text(msg, x, y):
    font = pygame.font.SysFont("Aerial", 50)
    text = font.render(msg, True, (0, 0, 0))
    WIN.blit(text, (x, y))

def Main():
    global ResultText
    global IsReset
    global HasWon
    global turns
    global totalNoOfTurns

    run = True
    clock = pygame.time.Clock()
    FPS = 60

    GridList = []

    for j in range(5):
        for i in range(5):
            Grid = GridBox(i*100, j*100)
            GridList.append(Grid)

    ShipBox = choice(GridList)     

    while run:
        mouse = pygame.mouse.get_pos()

        WIN.fill((255, 255, 255))
        for Grids in GridList:
            Grids.ClickGrid(mouse, ShipBox)
            Grids.Draw()

            if IsReset:
                Grids.color = (0 ,0, 0)
                ShipBox = choice(GridList) 
                turns = totalNoOfTurns
                ResultText = ""   
                HasWon = False
            if (turns == totalNoOfTurns):
                IsReset = False
                Grids.color = (0, 0, 0)

        Text(f"Turns: {turns}", 0, 530) 
        Text(ResultText, 175, 530) 

        pygame.draw.rect(WIN, (0, 0, 0), [425, 520, 50, 50], 3, 3)
        Text("R", 437, 530)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                quit()

        if (turns <= 0):
            ResultText = "You Loose !!"

        if (475 > mouse[0] > 425) and (570 > mouse[1] > 520):
            if pygame.mouse.get_pressed()[0]:
                IsReset = True

        pygame.display.update()
        clock.tick(FPS)

Main()