import turtle
import random

sss = input("실행하고싶은 프로그램을 입력해 주십시오:")
if sss == '1':
    t = turtle.Pen()
    t.penup()

    turtle.bgcolor("black")
    sides = int(turtle.numinput("변의 수",
                                "얼만큼 변의 수를 정하시겠슴니까(2-6)?", 4, 2, 6))
    colors = ["red","yellow","blue","green","orange","purple"]
    for m in range(100):
        t.forward(m * 4)

        position = t.position()
        heading = t.heading()
        print(position,heading)

        for n in range(int(m / 2)):
            t.pendown()
            t.pencolor(colors[n % sides])
            t.forward(n * 2)
            t.right(360 / sides - 2)
            t.penup()
        t.setx(position[0])
        t.sety(position[1])
        t.setheading(heading)
        t.left(360 / sides + 2)
    input("")

elif sss =='2':
    message = input("메시지를 입력해 주십시오.: ")
    message = message.upper()
    output = ""

    for letter in message:
        if letter.isupper():
            value = ord(letter) + 13
            letter = chr(value)
            if not letter.isupper():
                value -= 26
                letter = chr(value)
        output += letter
    print("출력 메시지:  ", output)

elif sss == '3':
    iff = 5
    the_number = random.randint(1, 10)
    guess = int(input("숫자를 1 부터 10중 하나를 추축하여 보세요.: "))
    while guess != the_number:
        if iff == 0:
            print("기회가 다 없어졌어. :(")
            break
        if guess > the_number:
            print(guess, "는 너무 높았어. 다시해봐. :ㅣ")
            iff = iff - 1
            print("남은 기회는: ", iff)
            print("")
        if guess < the_number:
            print(guess, "는 너무 낮았어. 다시해봐. :ㅣ")
            iff = iff - 1
            print("남은 기회는: ", iff)
            print("")
        guess = int(input("다시 추측 해봐. : "))
    if guess == the_number:
        print(guess, "가 정답이였어! 축하해!!  :)")
    if iff == 0:
        print(the_number, "가 정답이였어.:( 다음에 다시해봐.")
    print("")

elif sss == '4':
    nxx = "n"
    while nxx != "y":
        grade = eval(input("점수를 입력해 주십시오.(1-100): "))
        if grade >= 90:
            print("점수는:(두구.두구.두구)A :) ")
            print("잘했어요!")
            print("")
        elif grade >= 80:
            print("점수는:(두구.두구.두구)B!")
            print("좀더 연습해야 되겠내요.")
            print("")
        elif grade >= 70:
            print("점수는:(두구.두구.두구)C.")
            print("좀~더 연습해야 되겠어요.")
            print("")
        elif grade >= 60:
            print("점수는:(두구.두구.두구)D...")
            print("공부를 좀 더 해야되겠내요.")
            print("")
        else:
            print("점수는:(두구.두구.두구)F. :(")
            print("...")
            print("")
        nxx = input("종료를 원하십니까?(y,n)").lower()
    print("안녕히 계십시오.")
    print("")

elif sss == '5':
    answer = input("스프라이얼을 보고십습니까?(y,n)")
    if answer == 'y':
        print("작업중...")
        t = turtle.Pen()
        t.width(2)
        for x in range(100):
            t.forward(x * 2)
            t.left(89)
    print("이제 다했어!")

elif sss == '6':
    driving_age = eval(input("지금있는 지역에 드라이빙을 할 수 있는 나이는 몇세입니까?"))
    your_age = eval(input("몇세입니까?"))
    if your_age >= driving_age:
        print("너는 운전을 할 수 있어! :)")
    if your_age < driving_age:
        print("너는", driving_age - your_age, "년을 기다려야되. :(")

elif sss == '7':
    t = turtle.Pen()
    sides = int(turtle.numinput("변의수",
                                 "얼만큼으로 변의 수를 정하시겠습니까?", 4)) # 변의 수 정하기
    for m in range(5, 75):
        t.left(360 / sides + 5)
        t.width(m / 25 + 1)
        t.penup()
        t.forward(m * 4)
        t.pendown()
        if (m % 2 == 0):
            for n in range(sides):
                t.circle(m / 3)
                t.right(360 / sides)

        else:
            for n in range(sides):
                t.forward(m)
                t.right(360 / sides)
input("")
