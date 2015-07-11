driving_age = eval(input("지금있는 지역에 드라이빙을 할 수 있는 나이는 몇세입니까?"))
your_age = eval(input("몇세입니까?"))
if your_age >= driving_age:
    print("너는 운전을 할 수 있어! :)")
if your_age < driving_age:
    print("너는", driving_age - your_age, "년을 기다려야되. :(")
