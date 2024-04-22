import turtle

from random import *

# 1
for i in range(100):
    turtle.forward(randint(-100, 100))
    turtle.left(randint(-180, 180))
    turtle.goto(randint(-100, 100) * randint(1, 3), randint(-100, 100) * randint(1, 3))

turtle.exitonclick()
