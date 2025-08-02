import pygame
from Snake import Snake
from Food import Food

pygame.init()

class Grid:
    def __init__(self, win, w, h):
        self.win = win

        self.w = w
        self.h = h

        self.GridList = []
        self.GridList = self.MakeGrid()
    
    def MakeGrid(self):
        for i in range(self.win.get_height()//self.h):
            for j in range(self.win.get_width()//self.w):
                self.GridList.append([j*self.w, i*self.h, self.w, self.h])
        return self.GridList

    def DrawGrid(self):
        for cell in self.GridList:
            pygame.draw.rect(self.win, (0,0,0), cell, 1)

class Window:
    def __init__(self, w, h):
        self.w = w
        self.h = h

        self.gridW = 25
        self.gridH = 25

        self.win = pygame.display.set_mode((self.w, self.h))
        pygame.display.set_caption("Snake Game")

        self.run = True

        self.FPS = 10
        self.clock = pygame.time.Clock()

        self.grid = Grid(self.win, self.gridW, self.gridH)
        
        self.snake = Snake(self.win, 0, 0, self.gridW, self.gridH, (0, 255, 0))
        self.food = Food(self.win, self.gridW, self.gridH, (255, 0, 0))

    def Loop(self):
        while self.run:
            self.win.fill((255, 255, 255))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False
                    pygame.quit()
                    quit()

            self.snake.Update()
            self.food.Update(self.snake.SnakeList, self.snake.direction)
            self.grid.DrawGrid()
            pygame.display.update()
            self.clock.tick(self.FPS)
    
    def Update(self):
        self.Loop()

window = Window(500, 500)
window.Update()