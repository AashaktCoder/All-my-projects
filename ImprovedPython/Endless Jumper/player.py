import pygame

class Player:
    def __init__(self, win, tl):
        self.win = win

        self.rect = [0, 0, 50, 50]
        self.color = (0, 100, 255)

        self.g = 0.281
        self.vy = 0
        self.tl = tl

    def Draw(self):
        pygame.draw.rect(self.win,  self.color, self.rect)

    def Movement(self):
        if self.rect[1] < 400:
            self.vy += self.g

        keys = pygame.key.get_pressed()
        if keys[pygame.K_d] and self.rect[0] <= 450: self.rect[0] += 4  
        if keys[pygame.K_a] and self.rect[0] >= 0: self.rect[0] -= 4  

        if (self.rect[1] >= 400 or (self.Collision() and self.vy>= 0)):
            self.vy = 0
            if keys[pygame.K_SPACE]:
                self.vy -= 8
        self.rect[1] += self.vy

    def Collision(self):
        for i in self.tl:
            if pygame.Rect(self.rect).colliderect(i) :
                if (self.rect[1] + 45) <= i[1]:
                    return True
        return False
    
    def Update(self):
        self.Movement()
        self.Draw()