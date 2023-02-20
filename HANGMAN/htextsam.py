import pygame as pg
import sys
pg.init()
chetan=pg.display.set_mode((400,400))
chetan.fill("white")
FONT = pg.font.Font(pg.font.get_default_font(), 20)
previousWidth = 0
def getSurfaces(word, pos):
    global previousWidth
    
    surfaces = []
    positions  = []
    for i in range(len(word)):
        surf = FONT.render(f"{word[i]}", True, "black")
        surfaces.append(surf)
    for i in range(len(surfaces)):
        previousWidth += surfaces[i-1].get_rect().width
        positions.append([previousWidth + pos[0], pos[1]])
    return surfaces, positions
while True:
    pg.display.update()
    
    getSurfaces("chetan",200 )
    for event in pg.event.get():
        if event.type==pg.QUIT:
            pg.quit()
            sys.exit()

    