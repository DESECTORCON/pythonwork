x = 'y'
xc = 0
while x == 'y':
    if xc == 3:
        print("애러코드")
        print("")
        print("종료")
        break
    rainy = input("지금 비가 오고 있나요?:(y,n)").lower()
    print("")
    cold = input("지금 밖이 춥나요?:(y,n)").lower()
    print("")
    if rainy == 'y' and cold == 'y':
        print("우비를 입어야 되겠내요.")
        print("")
    elif rainy == 'y' and cold == 'n':
        print("우산을 쓰고 나가세요")
        print("")
    elif rainy == 'n' and cold == 'y':
        print("두꺼운 점퍼를 입으세요.")
        print("")
    elif rainy == 'n' and cold == 'n':
        print("자기가 입고 십은걸 입으세요!!")
        print("")
    else:
        print("타이핑을 확인해 주십시오.")
        xc += 1
    x = input("다시하시겠습니까?(n,y):").lower()
    print("")
print("안녕히 계십시오.")
print("")