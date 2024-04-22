import turtle

# 2
digits = {
    '0': [(0, 0), (90, 0), (90, -150), (0, -150), (0, 0)],
    '1': [(90, -150), (90, 0),(0, -75)],
    '2': [(0, 0), (90, 0), (90, -75), (0, -150), (90, -150)],
    '3': [(0, 0), (90, 0), (0, -75), (90, -75), (0, -150)],
    '4': [(0, 0), (0, -75), (90, -75), (90, 0), (90, -150)],
    '5': [(90, 0), (0, 0), (0, -75), (90, -75), (90, -150), (0, -150)],
    '6': [(90, 0),(0,-75), (0, -150), (90, -150), (90, -75), (0, -75)],
    '7': [(0, 0), (90, 0), (0, -75),(0,-150)],
    '8': [(0, 0), (90, 0), (90, -150), (0, -150), (0, 0), (0, -75), (90, -75)],
    '9': [(0, -150), (90, -75), (90, 0), (0, 0), (0, -75),(90, -75)]
}

t = turtle.Turtle()

turtle.screensize(500, 500)

x = -200
y = 200

t.pensize(5)


def draw_digit(digit):
    global x
    global y

    t.penup()
    t.goto(x + digits[digit][0][0], y + digits[digit][0][1])
    t.pendown()

    for point in digits[digit][1:]:
        t.goto(x + point[0], y + point[1])


for digit in "228069":
    draw_digit(digit)
    x += 100


turtle.exitonclick()