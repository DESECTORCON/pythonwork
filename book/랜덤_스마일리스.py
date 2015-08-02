import random
import turtle
t = turtle.Pen()
t.speed(-50)
t.hideturtle()
turtle.bgcolor("black")


def draw_smiley(x, y):  # 경고 표시가 난 부분1
    t.penup()
    t.setpos(x, y)
    t.pendown()
    # 머리
    t.pencolor("yellow")
    t.fillcolor("yellow")
    t.begin_fill()
    t.circle(50)
    t.end_fill()
    # 왼쪽눈
    t.setpos(x-15, y+60)
    t.fillcolor("blue")
    t.begin_fill()
    t.circle(10)
    t.end_fill()
    # 오른쪽눈
    t.setpos(x+15, y+60)
    t.begin_fill()
    t.circle(10)
    t.end_fill()
    # 입
    t.setpos(x-25, y+40)
    t.pencolor("black")
    t.width(10)
    t.goto(x-10, y+20)
    t.goto(x+10, y+20)
    t.goto(x+25, y+40)
    t.width(1)
for n in range(50):
    x = random.randrange(-turtle.window_width()//2,
                         turtle.window_width()//2)
    y = random.randrange(-turtle.window_height()//2,
                         turtle.window_height()//2)
    draw_smiley(x, y)