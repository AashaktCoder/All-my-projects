import pygame

class player:
    def __init__(self, win, x, y, w, h, collideList, color):
        self.win = win

        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.rect = [self.x, self.y, self.w, self.h]

        self.speed = 4
        self.g = 0.8
        self.direction = [0, 0]

        self.JumpHeight = -16

        self.OnGround = False

        self.color = color

        self.collideList = collideList

    def Draw(self):
        self.img = pygame.draw.rect(self.win, self.color, self.rect)

    def Movement(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_d] and self.rect[0] <= (self.win.get_width() - self.rect[2]):
            self.direction[0] = 1
        elif keys[pygame.K_a] and self.rect[0] >= 0:
            self.direction[0] = -1
        else:
            self.direction[0] = 0

        if keys[pygame.K_SPACE] and self.OnGround:
            self.direction[1] = self.JumpHeight

    def Gravity(self):
        self.direction[1] += self.g

    def VerticalCollision(self):
        for tile in self.collideList:
            if pygame.Rect(tile[0], tile[1], tile[2], tile[3]).colliderect(self.rect):
                if self.direction[1] > 0:
                    self.rect[1] = (tile[1] - self.rect[3])
                    self.direction[1] = 0
                    self.OnGround = True

                if self.direction[1] < 0:
                    self.rect[1] = (tile[1] + self.rect[3])
                    self.direction[1] = 0
                                             
        if self.OnGround and self.direction[1] != 0:
            self.OnGround = False

    def HorizontalCollision(self):
        for tile in self.collideList:
            if pygame.Rect(tile[0], tile[1], tile[2], tile[3]).colliderect(self.rect):
                if self.direction[0] > 0:
                    self.rect[0] = (tile[0] - self.rect[2])
                if self.direction[0] < 0:
                    self.rect[0] = (tile[0] + self.rect[2])         

    def Update(self):
        self.Movement()
        self.rect[0] += (self.direction[0] * self.speed)
        self.HorizontalCollision()
        self.Gravity()
        self.rect[1] += self.direction[1]
        self.VerticalCollision()
        self.Draw()