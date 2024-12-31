import turtle
from random import randint

turtle.screensize(canvwidth=500, canvheight=500)

player = turtle.Turtle()
player.shape('square')
player.penup()

playerX = player.xcor()
playerY = player.ycor()

food = turtle.Turtle()
food.shape('square')
food.penup()
foodX = randint(-240, 240)
foodY = randint(-240, 240)
food.setpos(foodX, foodY)

def move(angle):
    player.setheading(angle)
    player.forward(10)

turtle.listen()

turtle.onkeypress(lambda: move(90), 'w')
turtle.onkeypress(lambda: move(270), 's')
turtle.onkeypress(lambda: move(0), 'd')
turtle.onkeypress(lambda: move(180), 'a')

turtle.done()