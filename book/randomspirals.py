import random
import turtle
t = turtle.Pen()
turtle.bgcolor("black")  #ask 경고3
colors = ["red", "yellow", "blue", "green", "orange", "purple",
          "while", "gray"]
for n in range(50):
    t.pencolor(random.choice(colors))
    size = random.randint(10, 40)
    x = random.randrange(-turtle.window_width()//2,  #ask 경고1
                         turtle.window_width()//2)   #ask 경고4
    y = random.randrange(-turtle.window_height()//2,  #ask 경고2
                         turtle.window_height()//2)    #ask 경고5
    t.penup()
    t.setpos(x, y)
    t.pendown()
    for m in range(size):
        t.forward(m * 2)
        t.left(91)
        
