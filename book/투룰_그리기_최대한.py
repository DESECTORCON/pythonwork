import turtle
t = turtle.Pen()
t.speed(0)
turtle.bgcolor("blue")
t.pencolor("green")
t.width(99)
while True:
    turtle.onscreenclick(t.setpos)
