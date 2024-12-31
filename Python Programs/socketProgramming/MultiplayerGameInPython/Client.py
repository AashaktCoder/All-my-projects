import pygame
import socket

pygame.init()

WIDTH, HEIGHT = 500, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Multiplayer game by Aashakt")

c = socket.socket()
c.connect(("localhost", 9999))

class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.rect = [self.x, self.y, 50, 50]
        self.vel = 4

    def Draw(self):
        pygame.draw.rect(WIN, (0, 155, 255), self.rect)

    def Movement(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_d]:
            self.rect[0] += self.vel
            c.send(bytes(str(self.rect[0]), "utf-8"))
        if keys[pygame.K_a]:
            self.rect[0] -= self.vel
            c.send(bytes(str(self.rect[0]), "utf-8"))
        if keys[pygame.K_s]:
            self.rect[1] += self.vel
        if keys[pygame.K_w]:
            self.rect[1] -= self.vel  

    def Update(self):
        self.Draw() 
        self.Movement()
        print(c.recv(1024).decode())

def Main():
    run = True
    clock = pygame.time.Clock()
    FPS = 60

    player = Player(225, 225)

    while run:
        WIN.fill((255, 255, 255))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                quit()
        player.Update()      
        pygame.display.update()
        clock.tick(FPS)

Main()                