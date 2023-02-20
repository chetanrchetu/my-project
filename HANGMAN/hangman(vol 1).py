import pygame as pg
import sys
from values import *




screen = pg.display.set_mode((S_L,S_W))
screen.fill(S_C)

class word:
    l=[(200,50)],[(200,90) , (200,200)],[(200,90) , (200,200)],[(150,120),(200,100)] , [(250,120),(200,100)] , [(250,225),(200,200)], [(150,225),(200,200)]
    # print(l[1])
    try:
        func1=lambda self,li:li[0]
        func2 = lambda self,li:li[1]
    except:
        pass
    def man(self):
        
     
        pg.draw.circle(screen, "black" , (200,50) , 40 , 4 )
        pg.draw.line(screen , "black" , (200,90) , (200,200), 4 )    
        pg.draw.line(screen , "black" , (150,120),(200,100), 4 )
        pg.draw.line(screen , "black" , (250,120),(200,100), 4 )
        pg.draw.line(screen , "black" , (250,225),(200,200), 4 )
        pg.draw.line(screen , "black" , (150,225),(200,200), 4 )
        
    def erase(self,i):
            if i == 1:
                pg.draw.circle(screen, "white" , (200,50) , 40 , 4 )
            else:

                pg.draw.line(screen , "white" , self.func1(self.l[i]) , self.func2(self.l[i]) , 4 )  

def main():
    wrd = word()
    num = 6
    wrd.man()
    while True:

        for event in pg.event.get():
           
            
            if event.type == pg.QUIT:

                
                pg.quit()
                sys.exit()
            if event.type == pg.MOUSEBUTTONDOWN:
                if num > 0 :
               
                    wrd.erase(num)
                    num-=1   
                else:
                    pg.quit()
                    sys.exit() 
       
            
        pg.display.update()

main()