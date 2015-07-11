answer = input("스프라이얼을 보고십니?(y,n)")
if answer == 'y':
    print("작업중...")
    import turtle
    t = turtle.Pen()
    t.width(2)
    for x in range(100):
        t.forward(x*2)
        t.left(89)
print("이제 다했어!")