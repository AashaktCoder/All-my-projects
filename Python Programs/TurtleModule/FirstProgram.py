import turtle

turtle.colormode(255)

player = turtle.Turtle()
player.pencolor(0, 155, 255)
player.pensize(5)
player.shape('turtle')

for i in range(40):
    if i%2 == 0:
        player.pencolor(0, 125, 255)
        player.forward(10)
        player.right(10) 
    else:
        player.color(0, 235, 0)
        player.forward(10)
        player.right(10) 

turtle.done()