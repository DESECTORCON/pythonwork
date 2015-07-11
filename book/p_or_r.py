import turtle
t = turtle.Pen()
number = int(turtle.numinput("변 또는 동그라미의 수",
             "변 또는 동그라미의 수를 입력해 주세요:",6))
shape = turtle.textinput("어떤 모양을 원하십니까?",
                         "p는 세모,r는 동그라미:")
for x in range(number):
    if shape == 'r':
        t.circle(100)
    else:
        t.forward(150)
    t.left(360/number)

