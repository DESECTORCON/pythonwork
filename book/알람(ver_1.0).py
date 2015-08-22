from time import sleep
lop = True
while lop:
    sleeptime1 = int(input('알람이 울릴 시간을 정하싶시오.(단위:초)(프로그램 종료:"0"):'))
    if sleeptime1 == 0:
        lop = False
    elif sleeptime1 != 0:
        sleep(sleeptime1)
        con = input("시간이 다 되었어요!!")
        if con == "":
            continue
        if con != "":
            print("애러 타입!!")
            break
print("알람 프로그램 종료")