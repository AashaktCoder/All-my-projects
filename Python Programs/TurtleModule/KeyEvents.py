import turtle

player = turtle.Turtle()
player.pensize(5)
player.shape('square')
player.penup()

def move(angle):
    player.setheading(angle)
    player.forward(10)

turtle.listen()

turtle.onkeypress(lambda: move(90), 'w')
turtle.onkeypress(lambda: move(270), 's')
turtle.onkeypress(lambda: move(0), 'd')
turtle.onkeypress(lambda: move(180), 'a')

turtle.done()