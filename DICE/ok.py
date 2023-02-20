# Importing pygame module
from math import *
from tkinter import W
import pygame as pg
from pygame.locals import *
import sys
from constants import *
from random import *


# initiate pygame and give permission
# to use pygame's functionality.
pg.init()

# create the display surface object
# of specific dimension.
window = pg.display.set_mode((window_l, window_h))

# Fill the scree with white color
window.fill(windown_c)


pg.draw.rect(window, 'red',  # color of sqr
                                [X, Y, sqr_l, sqr_b], t)  # last 2 para - size of sqr
                                   # x and y co-ord
                                  # thickness

# pg.draw.circle(window, C_C, [C_X,C_Y], RADIUS, C_W)


class dot:
    def draw_123(self, num):
        if num != 2:
            W = 0
        else:
            W = 29

        for i in range(0, num):
            n = W*pow(-1, i)
            three = (X + sqr_l // 2), ((Y + sqr_l // 2) - n)
            pg.draw.circle(window, 'white', three, RADIUS, C_W)
            W = 29

    def draw_45(self, num):
        ofs = (sqr_l // 4)
        four1 = (X + ofs, Y + ofs)
        four2 = (X + (sqr_l - (ofs))), (Y + (ofs))
        four3 = (X + ofs), (Y + (sqr_l - ofs))
        four4 = (X + (sqr_l - (ofs))), (Y + (sqr_l - (ofs)))
        four5 = (X + sqr_l // 2), ((Y + sqr_l // 2))
        pg.draw.circle(window, 'white', four1,  RADIUS, C_W)
        pg.draw.circle(window, 'white', four2,  RADIUS, C_W)
        pg.draw.circle(window, 'white', four3,  RADIUS, C_W)
        pg.draw.circle(window, 'white', four4,  RADIUS, C_W)
        if num is 4:
            pass

        if num is 5:
            pg.draw.circle(window, 'white', four5,  RADIUS, C_W)

    def draw_6(self, num):
        for i in range(0, 3):
            ofss = sqr_l//4
            six = (X+(ofss)), (Y+(ofss)+25*i)
            six1 = (X+sqr_l-(ofss)), (Y+(ofss+25*i))
            pg.draw.circle(window, "white", six, RADIUS, C_W)
            pg.draw.circle(window, "white", six1, RADIUS, C_W)


# ---main func---
def main():
    d = dot()
    global func
    while True:

        for event in pg.event.get():
            if event.type == pg.MOUSEBUTTONDOWN:

                n = randint(1, 6)
                if n <= 3:
                    func = d.draw_123
                elif(n <=5):

                   func = d.draw_45
                else:
                    func = d.draw_6


            while True: 
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
                else:
                    func(n)

                   

        

        pg.display.update()


main()
