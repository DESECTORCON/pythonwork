import random
HANGMANPICS = ['''

  +---+
  |   |
      |
      |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
words = 'ant word swan bat wolf'.split()

def getRandomWord(wordList):
    wordIndex = random.randint(0, len(wordList) - 1)
    return wordList[wordIndex]

def displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord):
    print(HANGMANPICS[len(missedLetters)])
    print()

    print('missed letters:', end=' ')
    for letter in missedLetters:
        print(letter, end=' ')
    print()

    blanks = '_' * len(secretWord)

    for i in range(len(secretWord)):
        if secretWord[i] in correctLetters:
            blanks = blanks[:i] + secretWord[i] + blanks[i+1:]

    for letter in blanks:
        print(letter, end=' ')
    print()

def getGuess(alreadyGuessed):
    while True:
        print('guess a letter.')
        guess = input()
        guess = guess.lower()

        if len(guess) != 1:
            print('Pease enter a senge leter.')

        elif guess in alreadyGuessed:
            print('You have already guessed that letter. Choose again.')

        elif guess not in 'abcdefghijklmnopqrstuvwsyg':

            print('Please enter a LETTER.')

        else:
            return guess

def playAgain():
    print('Do you want to play agan? (yes or no)')
    return input().lower().startswith('y')

print('H A G M A N')

missedLetters = ''
correctLetters = ''
secretWord = getRandomWord(words)
gameIsDone = False
displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord)

while not gameIsDone:
    displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord)
    guess = getGuess(missedLetters + correctLetters)
    if guess in secretWord:

        correctLetters = correctLetters + guess

        foundAllLetters = True

        for i in range(len(secretWord)):

            if secretWord[i] not in correctLetters:
                foundAllLetters = False
                break

        if foundAllLetters:
            print('Yes! The secret word is "' + secretWord + '"! You have won!')

            gameIsDone = True

    else:
        missedLetters = missedLetters + guess


        if len(missedLetters) == len(HANGMANPICS) - 1:
            displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord)
            print('You have run out of guesses!\nAfter '+ str(len(missedLetters)) +
                  ' missed guesses and ' + str(len(correctLetters)) + ' correct guesses, the word was  "'
                  + secretWord + '".')
            gameIsDone = True

    if gameIsDone:
        if playAgain():
            missedLetters = ''
            correctLetters = ''
            gameIsDone = False
            secretWord = getRandomWord(words)

        else:
            break


