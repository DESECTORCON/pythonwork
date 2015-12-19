import random
# 기본 모듈 만들기

def drawBoard(board):
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')


def inputPlayerLetter():
    letter = ''
    while not (letter == 'X' or letter == 'O'):
        print('Do you want to be X or O?')
        letter = input().upper()

    if letter == 'X':
        return ['X', 'O']
    if letter == 'O':
        return ['O', 'X']


def whoGoesFirst():
    if random.randint(0, 1) == 0:
        return 'computer'
    else:
        return 'player'


def playAgain():
    print('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')


def makeMove(board, letter, move):
    board[move] = letter


def isWinner(bo, le):
    return ((bo[7] == le and bo[8] == le and bo[9] == le )or
            (bo[4] == le and bo[5] == le and bo[6] == le)or
            (bo[1] == le and bo[2] == le and bo[3] == le)or
            (bo[7] == le and bo[4] == le and bo[1] == le)or
            (bo[8] == le and bo[5] == le and bo[2] == le)or
            (bo[9] == le and bo[6] == le and bo[3] == le)or
            (bo[7] == le and bo[5] == le and bo[3] == le)or
            (bo[9] == le and bo[5] == le and bo[1] == le))


def getBoardCopy(board):
    dupeBoard = []

    for i in board:
        dupeBoard.append(i)

    return dupeBoard


def isSpaceFree(board, move):

    return board[move] == ' '

def getPlayerMove(board):
    move = ' '

    while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, int(move)):
        print('What is your next move? (1-9)')
        move = input()
    return int(move)


def chooseRandomMoveFromList(board, movesList):
    posseblemoves = []

    for i in movesList:
        if isSpaceFree(board, i):
            posseblemoves.append(i)

    if len(posseblemoves) != 0:
        return random.choice(posseblemoves)
    else:
        return None


def getComputerMove(board, computerLetter):
    if computerLetter == 'X':
        playerLetter = 'O'

    else:
        playerLetter = 'X'

    for i in range(1, 10):
        copy = getBoardCopy(board)
        if isSpaceFree(copy, i):
            makeMove(copy, computerLetter, i)
            if isWinner(copy, playerLetter):
                return i

    for i in range(1, 10):
        copy = getBoardCopy(board)
        if isSpaceFree(copy, i):
            makeMove(copy, playerLetter, i)
            if isWinner(copy, playerLetter):
                return i
    move = chooseRandomMoveFromList(board, [1, 3, 7, 9])

    if move != None:
        return move

    if isSpaceFree(board, 5):
        return 5

    return  chooseRandomMoveFromList(board, [2, 4, 6, 8])


def isBoardFull(board):

    for i in range(1, 10):
        if isSpaceFree(board, i):
            return False
    return True


# 프로그램 시작
print('Welcom to Tic Tac Toe!!')

while True:
    theBorad = [' '] * 10
    playerLetter, computerLetter = inputPlayerLetter()
    turn = whoGoesFirst()
    print('The ' + turn + ' will go first.')
    gameIsPlaying = True

    while gameIsPlaying:

        if turn == 'player':
            drawBoard(theBorad)
            move = getPlayerMove(theBorad)
            makeMove(theBorad, playerLetter, move)

            if isWinner(theBorad, playerLetter):
                drawBoard(theBorad)
                print('Hooray! You won the game!!!')
                gameIsPlaying = False

            else:
                if isBoardFull(theBorad):
                    drawBoard(theBorad)
                    print('The game is a tie!')
                    break

                else:
                    turn = 'computer'
        else:
            move = getComputerMove(theBorad, computerLetter)
            makeMove(theBorad, computerLetter, move)
            if isWinner(theBorad, computerLetter):
                drawBoard(theBorad)
                print('The computer has beaten you! You lose.')
                gameIsPlaying = False
            else:
                if isBoardFull(theBorad):
                    drawBoard(theBorad)
                    print('The game is a tie!')
                    break
                else:
                    turn = 'player'
    if not playAgain():
        break