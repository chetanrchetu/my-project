from tkinter import W
import pygame as pg
import os
import time
import random
import sys
pg.init()
#width and hei
W=500
H=500
#load image
WIN=pg.display.set_mode((W,H))
pg.display.set_caption("space game")



#loading ships imge
res_s=pg.image.load(os.path.join("assets","pixel_ship_red_small.png"))
green_s=pg.image.load(os.path.join("assets","pixel_ship_green_small.png"))
blue_s=pg.image.load(os.path.join("assets","pixel_ship_blue_small.png"))
#main player
yellow_s=pg.image.load(os.path.join("assets","pixel_ship_yellow.png"))

#laser
red_l=pg.image.load(os.path.join("assets","pixel_laser_red.png"))
green_l=pg.image.load(os.path.join("assets","pixel_laser_green.png"))
blue_l=pg.image.load(os.path.join("assets","pixel_laser_blue.png"))
yellow_l=pg.image.load(os.path.join("assets","pixel_laser_yellow.png"))

bg=pg.image.load("D:\\AI and ML\\projects\\space wader\\assets\\background-black.png")
bg=pg.transform.scale(bg,(W,H))

class Ship:
    def __init__(self,x,y,health=100):
        self.x=x
        self.y=y
        self.health=health
    
    def draw(self,win):
        pg.draw.rect(win,"red",(self.x,self.y,20,20))



def main():
    fps=60
    clock=pg.time.Clock()
    lev=1
    liv=5   #to show level and lives we have create a font object
    m_f=pg.font.SysFont("comcicsans",50)
    ship=Ship(200,340)

   
    def redraw():
        WIN.blit(bg,(0,0))
        #draw 
        #now we turn m_f to surface then only we can blit it or else it cant be displayed
        liv_lab=m_f.render(f"level:{lev}",1,"white")
        lev_lab=m_f.render(f"lives:{liv}",1,"white")
        # print(lev_lab.get_size())  use this to determin the width and height 
        WIN.blit(liv_lab,(0,0))
        WIN.blit(lev_lab,(500-107,0))
        ship.draw(WIN)
        pg.display.update()





    while True:
        clock.tick(fps)

        redraw()
        for event in pg.event.get():
            if event.type==pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type==pg.KEYDOWN:
                if event.key==pg.K_LEFT:
                    ship.x-=10
                if event.key==pg.K_RIGHT:
                    ship.x+=10
                if event.key==pg.K_UP:
                    ship.y-=10
                if event.key==pg.K_DOWN:
                    ship.y+=10

        
        


main()