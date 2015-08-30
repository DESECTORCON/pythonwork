import pygame
pygame.init()
screen = pygame.display.set_mode([600, 600])
keep_going = True
pic = pygame.image.load("CrazySmile.bmp")
colorkey = pic.get_at((0, 0))
pic.set_colorkey(colorkey)
picx = 0
picy = 0
while keep_going:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            keep_going = False
    picx += 0.2
    picy += 0.2
    screen.blit(pic, (picx, picy))
    pygame.display.update()
pygame.quit()