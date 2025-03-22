import pygame

pygame.init()

win = pygame.display.set_mode((500, 500))

l = [complex(0, 0)]

run = True

while run:
    win.fill((255, 255, 255))

    for i in l:
        pygame.draw.rect(win, (0, 0, 0), [(i.real+250), (i.imag+250), 5, 5])

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
            quit()

    m = pygame.mouse.get_pos()

    l = []
    z = complex(0, 0)
    c = complex(m[0]//50, m[1]//50)

    for i in range(10):
        z = z**2 + c
        l.append(z+c)  
    print(l)

    pygame.display.update()
