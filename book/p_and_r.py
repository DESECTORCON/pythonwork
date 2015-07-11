import turtle
t = turtle.Pen()
sides = int(turtle.numinput("변의수",
                            "얼만큼으로 변의 수를 정하시겠습니까?",4)) # 변의 수 정하기

for m in range(5,75):
    t.left(360/sides + 5)
    t.width(m//25+1)
    t.penup()
    t.forward(m*4)
    t.pendown()
    if (m % 2 == 0):
        for n in range(sides):
            t.circle(m/3)
            t.right(360/sides)

        else:
            for n in range(sides):
                t.forward(m)
                t.right(360/sides)
