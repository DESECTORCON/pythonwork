import random
iff = 5
the_number = random.randint(1, 10)
guess = int(input("숫자를 1 부터 10중 하나를 추축하여 보세요.: "))
while guess != the_number:
    if iff == 0:
        print("귀회가 다 없어졌어. :(")
        break
    if guess > the_number:
        print(guess, "는 너무 높앗어. 다시해봐. :ㅣ")
        iff = iff - 1
        print("남은 기회는: ", iff)
        print("")
    if guess < the_number:
        print(guess, "는 너무 낮앗어. 다시해봐. :ㅣ")
        iff = iff - 1
        print("남은 기회는: ", iff)
        print("")
    guess = int(input("다시 추측 해봐,: "))
if guess == the_number:
    print(guess, "가 정답이였어! 축하해!!  :)")
if iff == 0:
    print(the_number, "가 정답이였어.:( 다음에 다시해봐.")
print("")
