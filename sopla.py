import turtle

# 4
t = turtle
t.shape("turtle")
x = -200
y = 0
dt = 0
Vx = 5
Vy = 70
Ay = -10

t.penup()
t.goto(-200, 0)
t.pendown()
for i in range(20):
    while True:
        x += Vx * dt
        y += Vy * dt + Ay * (dt**2) / 2
        Vy += Ay * dt
        t.goto(x, y)
        dt += 10**(-3)
        if y < 0:
            break
    Vy = abs(Vy) / 1.3

turtle.exitonclick()