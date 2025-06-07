import pygame

class Particle:
    def __init__(self, win, n, w, h, x, y, m, c, pl, arl):

        self.win = win

        self.pos = pygame.math.Vector2(x, y)
        self.vel = pygame.math.Vector2(0, 0)
        self.acc = pygame.math.Vector2(0, 0)
        self.force = pygame.math.Vector2(0, 0)

        self.w, self.h = w, h
        self.m = m

        self.c = c

        self.n = n

        self.pl = pl

        self.arl = arl
                    

    def Draw(self):
        pygame.draw.rect(self.win, self.c, [self.pos.x, self.pos.y, self.w, self.h])

    def ApplyForce(self):
        for p in self.pl:
            ar = self.arl[self.n][p.n]

            if ar != 0 and p != self:
                dir = (self.pos - p.pos)
                dis = dir.length()

                if 1 < dis < 100:
                    fmag = ((10**-1) * self.m * p.m) / (dis)
                    force = dir.normalize() * fmag * ar
                    p.acc += (force / p.m)

    def Move(self):
        self.vel += self.acc
        self.pos += self.vel

        if self.pos.x > self.win.get_width()-self.w: 
            self.pos.x = self.win.get_width()-self.w
            self.vel = -self.vel
        if self.pos.x < 0:
            self.pos.x = 0
            self.vel = -self.vel
        if self.pos.y > self.win.get_height()-self.h:
            self.pos.y = self.win.get_height()-self.h
            self.vel = -self.vel
        if self.pos.y < 0:
            self.pos.y = 0 
            self.vel = -self.vel

    def Update(self):
        self.ApplyForce()
        self.Move()
        self.Draw()
        self.vel *= 0.98
        self.acc = pygame.Vector2(0, 0)