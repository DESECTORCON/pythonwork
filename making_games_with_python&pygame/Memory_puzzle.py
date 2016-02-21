
import random, pygame, sys
from pygame.locals import *

FPS = 30
WINDOWWIDTH = 640
WINDOWHIGHT = 480
REVEALSPEED = 8
BOXSIZE = 40
GAPSIZE = 10
BOARDWIDTH = 10
BOARDHIGHT = 7
assert (BOARDWIDTH * BOARDHIGHT) % 2 == 0, 'Board needs to have an even ' \
                                           'number of boxes for pairs of matchs.'
XMARGIN = int((WINDOWWIDTH - (BOARDWIDTH * (BOXSIZE + GAPSIZE))) / 2)
YMARGIN = int((WINDOWHIGHT - (BOARDHIGHT * (BOXSIZE + GAPSIZE))) / 2)

#            R    G    B
GRAY     = (100, 100, 100)
NAVYBLUE = ( 60,  60, 100)
WHITE    = (255, 255, 255)
RED      = (255,   0,   0)
GREEN    = (  0, 255,   0)
BLUE     = (  0,   0, 255)
YELLOW   = (255, 255,   0)
ORANGE   = (255, 128,   0)
PURPLE   = (255,   0, 255)
CYAN     = (  0, 255, 255)

BGCOLOR = NAVYBLUE
LIGHTBGCOLOR = GRAY
BOXCOLOR = WHITE
HIGHLIGHTCOLOR = BLUE

DONUT = 'donut'
SQUARE = 'square'
DIAMOND = 'diamond'
LINES = 'lines'
OVAL = 'oval'

ALLCOLORS = (RED, GREEN, BLUE, YELLOW, ORANGE, PURPLE, CYAN)
ALLSHAPES = (DONUT, SQUARE, DIAMOND, LINES, OVAL)
assert len(ALLCOLORS) * len(ALLSHAPES) * 2 >= BOARDWIDTH * BOARDHIGHT, "board is too big for the number of shapes/colors defined."

def main():
    global FPSCLOCK, DISPLAYSURF
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHIGHT))

    mousex = 0
    mousey = 0
    pygame.display.set_caption('Memory Game')

    mainBoard = getRandomizedBoard()
    revealedBoxes = generateRevealedBoxesData(False)

    firstSelextion = None

    DISPLAYSURF.fill(BGCOLOR)
    startGameAnimation(mainBoard)

    while True:
        mouseClicked = False

        DISPLAYSURF.fill(BGCOLOR)
        drawBoard(mainBoard, revealedBoxes)

        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEMOTION:
                mousex, mousey = event.pos
            elif event.type == MOUSEBUTTONUP:
                mousex, mousey = event.pos
                mouseClicked = True

        boxx, boxy = getBoxAtPixel(mousex, mousey)
        if boxx != None and boxy != None:

            if not revealedBoxes[boxx][boxy]:
                drawHighlightBox(boxx, boxy)
            if not revealedBoxes[boxx][boxy] and mouseClicked:
                revealedBoxesAnimation(mainBoard, [(boxx, boxy)])
                revealedBoxes[boxx][boxy] = True

            if firstSelection == None:
                firstSelextion = (boxx, boxy)

            else:
                icon1shape, icon1color = getShapeAndColor(mainBoard, firstSelextion[0], firstSelextion[1])
                icon2shape, icon2color = getShapeAndColor(mainBoard, boxx, boxy)


                if icon1shape != icon2shape or icon1color != icon2color:

                    pygame.time.wait(1000)
                    coverBoxesAnimation(mainBoard, [(firstSelextion[0], firstSelextion[1]), (boxx, boxy)])
                    revealedBoxes[firstSelextion[0]][firstSelextion[1]] = False

                    revealedBoxes[boxx][boxy] = False
                elif hasWon(revealedBoxes):
                    gameWonAnimation(mainBoard)
                    pygame.time.wait(2000)

                    mainBoard = getRandomizedBoard()
                    revealedBoxes = generateRevealedBoxesData(False)


                    drawBoard(mainBoard, revealedBoxes)
                    pygame.display.update()
                    pygame.time.wait(1000)


                    strtGameAnimation(mainBoard)
                firstSelextion = None
        pygame.display.update()
        FPSCLOCK.tick(FPS)


def generateRevealedBoxesData(val):
    revealedboxes = []
    for i in range(BOARDWIDTH):
        revealedboxes.append([val] * BOARDHIGHT)
    return revealedboxes


def getRandomizedBoard():

    icons = []
    for color in ALLCOLORS:
        for shape in ALLSHAPES:
            icons.append( (shape, color) )

    random.shuffle(icons)
    numIconsUsed = int(BOARDWIDTH * BOARDHIGHT / 2)

    icons = icons[:numIconsUsed] * 2
    random.shuffle(icons)


    board = []
    for x in range(BOARDWIDTH):
        column = []
        for y in range(BOARDHIGHT):
            column.append(icons[0])
            del icons[0]
        board.append(column)
    return board


def splitIntoGroupsOf(groupSize, theList):


    result = []
    for i in range(0, len(Listt), groupSize):
        result.append(theList[i:i + groupSize])

    return result


def leftTopCoordsOfBox(boxx, boxy):

    left = boxx * (BOXSIZE + GAPSIZE) + XMARGIN
    top = boxy * (BOXSIZE + GAPSIZE) + YMARGIN
    return (left, top)


