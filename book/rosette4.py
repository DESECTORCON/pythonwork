import turtle

colors = ["red", "yellow", "blue", "green"]
t = turtle.Pen()

for x in range(12): # 0 ~ 11까지 반복
    t.color(colors[x % 4]) # 펜색 정하는 부분
    t.circle(100)
    t.left(30)