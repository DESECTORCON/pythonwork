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
        print("공부를 좀더 해야되겠내요.")
        print("")
    else:
        print("점수는:(두구.두구.두구)F. :(")
        print("...")
        print("")
    nxx = input("종료를 원하십니까?(y,n)").lower()

print("안녕히 계십시오.")
print("")