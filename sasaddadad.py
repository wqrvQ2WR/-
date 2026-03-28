import turtle
import random

turtle.hideturtle()
turtle.speed(10)

colors = ["red", "blue", "green", "purple", "orange", "black"]

while True :
    turtle.color(random.choice(colors))
    x = random.randint(-300,300)
    y = random.randint(-300, 300)
    turtle.goto(x, y)