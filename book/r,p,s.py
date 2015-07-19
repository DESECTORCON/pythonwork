import random
lele = 1
computer2 = 0
player2 = 0
choices = ["주먹", "종이", "가위","주먹", "종이", "가위"]
print("'가위 바위 보' 게임 첫번째판")
print("주먹은 가위를 없에고,가위는 종이를 없에고,종이는 주먹을 없엔다.")
player = input("너는 주먹이 되고싶니; 아니면 종이; 아니면 가위가 되고십니?(그만하고싶으면 'Q'):")
while player != "q":
    player = player.lower()
    computer = random.choice(choices)
    print("너는 " + player + '을 골랐고,나는 ' + computer + "를 골랐어.")
    if player == computer:
        print("우리 서로 똑같은것을 낸내.")
    elif player == "주먹":
        if computer == "가위":
            print("너가 이겼어.")
            player2 = player2 + 1  # 약한 애러
        else:
            print("네가 이겼어.")
            computer2 = computer2 + 1  # 약한 애러
    elif player == "종이":
        if computer == "주먹":
            print("너가 이겼어.")
            player2 = player2 + 1   # 약한 애러
        else:
            print("네가 이겼어.")
            computer2 = computer2 + 1    # 약한 애러
    elif player == "가위":
        if computer == "종이":
            print("너가 이겼어.")
            player2 = player2 + 1    # 약한 애러
        else:
            print("네가 이겼어.")
            computer2 = computer2 + 1   # 약한 애러
    else:
        print("타이핑에 애러가 있었어.")
    lele = lele + 1
    print("")
    print("'가위 바위 보' 게임", lele, "번째판")
    player = input("너는 주먹이 되고싶니; 아니면 종이; 아니면 가위가 되고십니?(그만하고싶으면 'Q'):")
print("이긴 사람은 (두구 두구 두구 두구!!):")
if computer2 > player2:
    print("내가 이겼어!")
if computer2 < player2:
    print("너가 이겼어!")
if computer2 == player2:
    print("비겼어.")
