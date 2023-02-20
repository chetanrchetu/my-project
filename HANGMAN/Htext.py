from cmath import rect
import sys
import pygame as pg
pg.init()
game = pg.display.set_mode((400, 400))


# to display blanks
# class dis:
word = "heyyyy"
font = pg.font.SysFont(None, 30)
a = font.render(word, True, "brown")  # so this has to be sent to blit function


for num in range(1, 4*2):
    if num % 2 == 0:
        word += " "
    else:
        word += "_"
a = font.render(word, True, 'black')
rec = a.get_rect()
rec.centery = 200
size=rec.size
print(size)
    



rec.topleft=(0,100)
post=rec.topright



while True:
   
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
        if event.type==pg.MOUSEBUTTONDOWN:
                # print(event.pos)
                post=(event.pos)
                if event.type==pg.KEYDOWN:
                    if event.key==pg.K_BACKSPACE:
                        pass
                        
        
        cursor=pg.Rect(post,(3,rec.height))
    
    game.fill("white")
    pg.draw.rect(game,"black",cursor)
    game.blit(a, rec)
    pg.display.update()
