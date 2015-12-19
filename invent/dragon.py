import random
import time
def displayIntro():
    print('You are in a land full of dragons. In front of you,')
    print('you see tow caves. In one cave, the dragon is friendly.')
    print('and will share his treasure with you. The orher dragon')
    print('is greedy and hungry, and will eat you on sight.')
def chooseCave():
    cave = ''
    while cave != '1' and cave != '2':
        print('which cave will you go into? (1 or 2)')
        cave = input()
    return cave
def checkCave(chosenCave):
    print('You approach the cave...')
    time.sleep(2)
    print('It is dark and sooky...')
    time.sleep(2)
    print('A large dragon jumps out in front of you! He opems his jaws and...')
    print()
    time.sleep(2)
    friendlyCave = random.randint(1, 2)
    if chooseCave == str(friendlyCave):
        print('Gives you his treasure!')
    else:
        print('Gobbles you down in one bite!')
playAgain = 'yes'
while playAgain == 'yes' or playAgain == 'y':
    displayIntro()
    caveNumder = chooseCave()
    checkCave(caveNumder)
    print('Do you want to play again? (yes or no)')
    playAgain = input()