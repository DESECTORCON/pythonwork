import random
import turtle
t = turtle.Pen()
t.speed(0)
turtle.bgcolor("black")
colors = ["red", "yellow", "blue", "green", "orange", "purple", "white", "gray"]
for n in range(50):
    t.pencolor(random.choice(colors))
    size = random.randint(10, 40)
    x = random.randrange(0, turtle.window_width()//2)  # 문제1('window_width'를 turtle 라이버리에서 찾을 수 없음)
    y = random.randrange(0, turtle.window_height()//2)  # 문제('window height'를 turtle 라이버리에서 찾을 수 없음)