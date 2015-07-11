import turtle # 기본준비과정
t = turtle.Pen()
turtle.bgcolor("black")
colors = ["red","yellow","blue","green","orange",
          "purple","white","brown","gray","pink" ]
family = []  # 빈 리스트 준비하기
name = turtle.textinput("나의 가족",
                        "이름을 적거나[ENTER]를 눌러서 나간다:")

while name != "":
    family.append(name)
    name = turtle.textinput("나의 가족",
                            "이름을 적거나[ENTER]를 눌러서 나간다:")

for x in range(100):
    t.pencolor(colors[x % len(family)])
    t.penup()
    t.forward(x*4)
    t.pendown()
    t.write(family[x%len(family)],font = ("Arial",int((x+4)/4),"bold"))
    t.left(360/len(family) + 2)

input("")