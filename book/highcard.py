import random
suits = ["clubs", "diamonds", "hearts", "spades"]
faces = ["two", "three", "four", "five", "six", "seven", "eight", "nine",
         "ten", "jack", "queen", "king", "ace"]
keep_going = True
while keep_going:
    my_face = random.choice(faces)
    my_suit = random.choice(suits)
    your_face = random.choice(faces)
    your_suit = random.choice(suits)
    print("나는", my_face, "이고 팀은", my_suit, "이야.")
    print("너는", your_face, "이고 팀은", your_suit, "이야.")
    if faces.index(my_face) > faces.index(your_face):
        print("내가 이겼어!")
    elif faces.index(my_face) < faces.index(your_face):
        print("너가 이겼어!")
    else:
        print("비겼내.")
    answer = input("[ENTER]을 눌르면 개임 진행, 아무키를 눌르면 개임끝. ")
    keep_going = (answer == "")