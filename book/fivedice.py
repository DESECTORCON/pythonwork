import random
# 개임 루프
game_count = 0
keep_going = True
while keep_going:
    dice = [0, 0, 0, 0, 0]
    for i in range(5):
        dice[i] = random.randint(1, 6)
    print("너가 나온 주사위 수는;", dice)
    dice.sort()
    if dice[0] == dice[4]:
        print("얐지닷!!!!!!!")
    elif (dice[0] == dice[3]) or (dice[1] == dice[4]):
        print("포 어브 카인드!!")
    elif (dice[0] == dice[2]) or (dice[1] == dice[3]) or (dice[2] == dice[4]):
        print("트리 어브카인드!")
    game_count += game_count + 1
    keep_going = (input("다시할꺼면 [ENTER];어떤키를 눌러도 개임끝!!:") == "")