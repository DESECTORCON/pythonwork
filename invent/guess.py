import random
tes = True
guess = 0
guessesTaken = 0
print("hello! What is your name?")
users_name = input()
number = random.randint(1, 20)
print("Well, " + users_name + ' I am thinking of a number between 1 and 20.')
while guessesTaken < 6:
    print(users_name + ' 숫자를 입력해 주십시오.')
    print("Take a guess.")
    guess = input()
    guess = int(guess)
    guessesTaken = guessesTaken + 1
    if guess < number:
        print('Your guess is too low.')
    if guess > number:
        print('Your guess is too high.')
    if guess == number:
        break
if guess == number:
    guessesTaken = str(guessesTaken)
    print('Good job, ' + users_name + 'You guessed my number in ' + guessesTaken + ' guesses!!')
if guess != number:
    number = str(number)
    print('Nope. The number I was tinking of was ' + number)