import random
import turtle
t = turtle.Pen()
t.speed(0)
turtle.bgcolor("black")
colors = ["red", "yellow", "blue", "green", "orange", "purple", "white", "gray"]
def fff():
    for m in range(size):
        t.forward(m*2)
        t.left(91)
def ddd(dfd1, dfd2):
    t.penup()
    t.setpos(dfd1, dfd2)
    t.pendown()
for n in range(50):
    t.pencolor(random.choice(colors))
    size = random.randint(10, 40)
    x = random.randrange(0, turtle.window_width()//2)
    y = random.randrange(0, turtle.window_height()//2)
    ddd(x, y)
    fff()
    ddd(-x, y)
    fff()
    ddd(-x, -y)
    fff()
    ddd(x, -y)
    fff()
input(":::...")