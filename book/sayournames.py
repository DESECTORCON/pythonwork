name = input("what is your name?   ")
while name != "":
    for x in range(100):
        print(name, end= " ")
    print()
    name = input("Type another name, or just hit [ENTER] to quit:  ")
print("Thanks fo playing!!")
