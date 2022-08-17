import sys, pygame as py
from blocks import Tetrominos
from variables import *
from canvas import Canvas 

size = width, height = 320, 240
speed = [0, 0]



screen = win


ball = py.image.load("intro_ball.gif")
ballrect = ball.get_rect()

canvas = Canvas()

#tetromino = Tetrominos(2,[80,80],1)

while True:
    for event in py.event.get():
        if event.type == py.QUIT: sys.exit()

    ballrect = ballrect.move(speed)
    screen.set_alpha(255)
    screen.fill(background)
    canvas.update()
    #tetromino.update(1)     
    py.display.flip()
    