import pygame, sys
from pygame.locals import *
from time import sleep

def startDraw():
    fps = 60
    timer = pygame.time.Clock()
    width = 800
    height = 600
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('show ur skills')
    global run
    global t
    run = True
    activeSize = 15
    activeColor = "black"
    painting = []
    screen.fill("white")
    while run:
        mouse = pygame.mouse.get_pos()
        timer.tick(180)
        #getRun()
        #pygame.draw.circle(screen, activeColor, mouse, activeSize)
        for event in pygame.event.get():
            if event.type == pygame.QUIT : ##must check in here
                run = False
            if pygame.mouse.get_pressed()[0]:
                painting.append((activeColor, mouse, activeSize))
                for i in range(len(painting)):
                    pygame.draw.circle(screen, painting[i][0], painting[i][1], painting[i][2])
        pygame.display.flip()

    pygame.quit()

startDraw()