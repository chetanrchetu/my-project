#import speech_recognition
import copy

import sys
import pygame
from constant import *
import numpy as np

#pygame
pygame.init()
screen = pygame.display.set_mode( (WIDTH,HEIGHT))
pygame.display.set_caption('TIC TAC TOE AI')
screen.fill(BG_COLOR)

class Board():
    



    def __init__(self):
        self.squares = np.zeros((ROWS,COLS))
        #print(self.squares)
        self.empty_sqrs = self.squares # [ squares]
        self.markedsqr=0
        
    def final_s(self , show = False):
        """
        @return 0 , is there is not win yet
        @return 1 , if p1 wins
        @return 2 , if p2 wins
        
        """

        #vertical wins
        for col in range (COLS):
            if self.squares[0][col] == self.squares[1][col] == self.squares[2][col] != 0:
                if show:
                    
                    color = C_C if self.squares[0][col] == 2 else CR_C
                    iPos = (col* SQSIZE + SQSIZE // 2 , 20) 
                    fPos = (col * SQSIZE + SQSIZE // 2 ,HEIGHT - 20)
                    pygame.draw.line(screen ,color , iPos , fPos , LINE_WIDTH)
                return self.squares[0][col]
                
        #horizontal wins
        for row in range (ROWS):
            if self.squares[row][0] == self.squares[row][1] == self.squares[row][2] != 0:
                
                if show:
                    color = C_C if self.squares[0][row] == 2 else CR_C
                    iPos = (20 , row * SQSIZE + SQSIZE // 2)
                    fPos = (WIDTH - 20 , row* SQSIZE + SQSIZE // 2) 
                    pygame.draw.line(screen ,color , iPos , fPos , LINE_WIDTH)
                return self.squares[row][0]

        #diag wins(desc)
        if self.squares[0][0] == self.squares[1][1] == self.squares[2][2] != 0:
            if show:
                color = C_C if self.squares[1][1] == 2 else CR_C
                iPos = (20 , 20)
                fPos = (WIDTH - 20 , HEIGHT - 20 ) 
                pygame.draw.line(screen ,color , iPos , fPos , CR_W)
            return self.squares[1][1]

        #diag wins(asc)
        if self.squares[2][0] == self.squares[1][1] == self.squares[0][2] != 0:
            if show:
                color = C_C if self.squares[1][1] == 2 else CR_C
                iPos = (20,HEIGHT-20)
                fPos = (WIDTH - 20 , 20) 
                pygame.draw.line(screen ,color , iPos , fPos , CR_W)
            return self.squares[1][1]
        
        #no win 
        return 0

    def marksquare(self, row , col , player):
        self.squares[row][col] = player
        self.markedsqr += 1


    def empty_sqr(self,row,col):
        return self.squares[row][col]==0

    def get_empty_sqrs(self):
        empty_sqrs = []
        for row in range (ROWS):
            for col in range (COLS):
                if self.empty_sqr(row,col):
                    empty_sqrs.append( (row,col) )
        return empty_sqrs


    def isfull(self):
        return self.markedsqr == 9

    def isempty(self):
        return self.markedsqr == 0

class AI:

    def __init__(self , level = 1,player = 2):
        self.level = level
        self.player = player
    
    #def rnd(self,board):
       # empty_sqrs = board.get_empty_sqrs()
        #idx = random.randrange(0 ,  len(empty_sqrs))

        #return empty_sqrs[idx]

    def minmax(self,board,maximizing):
        case= board.final_s()  
        #none = -3 
        
        if case == 1:
            return 1, (-3,-3)

        if case ==2:
            return -1 , (-3,-3)

        elif board.isfull():
            return 0 , (0,0)

        if maximizing:
            max_eval = -2
            best_move = -3
            empty_sqrs = board.get_empty_sqrs()

            for (row,col) in empty_sqrs:
                temp_board = copy.deepcopy(board)
                temp_board.marksquare(row,col,1)
                eval = self.minmax(temp_board, False)[0]
                if eval > max_eval:
                    max_eval = eval
                    best_move = (row,col)
                    # print("i am in if")
            return max_eval , best_move

        elif not maximizing:
            min_eval = 1
            best_move = None
            empty_sqrs = board.get_empty_sqrs()

            for (row,col) in empty_sqrs:
                temp_board = copy.deepcopy(board)
                temp_board.marksquare(row,col,self.player)
                eval = self.minmax(temp_board, True)[0]
                if eval< min_eval:
                    min_eval = eval
                    best_move = (row,col)
                    # print('im in elif')
            return min_eval , best_move




    def eval(self,main_board):
      
        # else:
        eval = 'random'
        eval,move = self.minmax(main_board , False)
        # print(f'{move}')
        print(f'AI has chosen to mark square in position {move} with a eval of {eval}')
        print(move)
        return move            




class Game:

    def __init__(self) -> None:
        
        self.board = Board()
        self.ai=AI()
        self.player= 1
        self.gamemode = 'ai' #pvp or ai
        self.running = True
        self.show_lines()

    def make_move(self, row,col):
        self.board.marksquare(row,col,self .player)
        self.draw_fig(row,col)
        self.next_turn()



    def show_lines(self): 
        #BG
        screen.fill(BG_COLOR)
        
        #VERTICAL
        pygame.draw.line(screen , LINE_COLOR , (SQSIZE,0),(SQSIZE,HEIGHT),LINE_WIDTH)
        pygame.draw.line(screen , LINE_COLOR , (WIDTH - SQSIZE,0),( WIDTH - SQSIZE , HEIGHT),LINE_WIDTH)

        #horizontal
        pygame.draw.line(screen , LINE_COLOR , (0,SQSIZE),(WIDTH,SQSIZE),LINE_WIDTH)
        pygame.draw.line(screen , LINE_COLOR , (0,HEIGHT-SQSIZE),(WIDTH,HEIGHT-SQSIZE),LINE_WIDTH)

    def draw_fig(self,row,col):
        if self.player == 1:
            #DESCENDING LINE
            start_des=( col * SQSIZE + OFFSET , row * SQSIZE + OFFSET)
            end_des = (col * SQSIZE + SQSIZE - OFFSET , row * SQSIZE + SQSIZE - OFFSET)
            pygame.draw.line(screen , CR_C , start_des , end_des , CR_W)
            
            #ascend                 
            start_asc=( col * SQSIZE + OFFSET , row * SQSIZE + SQSIZE - OFFSET)
            end_asc = (col * SQSIZE + SQSIZE - OFFSET , row * SQSIZE + OFFSET)
            pygame.draw.line(screen , CR_C , start_asc , end_asc , CR_W)
        
        
        
        elif self.player == 2:
            #draw circle
            center = (col * SQSIZE + SQSIZE // 2 , row * SQSIZE + SQSIZE //2 )
            pygame.draw.circle(screen , C_C , center , RADIUS ,C_W )
    
    
    
    
    def next_turn(self):
        self.player = self.player %2 + 1

    def change_gamemode(self):
        self.gamemode = 'ai' if self.gamemode == 'pvp' else 'pvp'

    def isover(self):
        return self.board.final_s(show=True) != 0 or self.board.isfull() 
      
    def reset(self):
        self.__init__() 

#main loop
def main():
    

    #object
    game = Game()
    board = game.board
    ai = game.ai
    
    while True:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:

                pygame.quit()
                sys.exit()
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = event.pos
                row = pos[1] //SQSIZE
                col = pos[0] //SQSIZE

                if board.empty_sqr(row,col):
                    game.make_move(row,col)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_g:
                    game.change_gamemode()
                
                if event.key == pygame.K_r:
                    game.reset() 
                    board = game.board
                    ai = game.ai

                if event.key == pygame.K_1:
                    ai.level  = 1


            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = event.pos
                row = pos[1] //SQSIZE
                col = pos[0] //SQSIZE

                if board.empty_sqr(row,col):
                    game.make_move(row,col)

                    if game.isover():
                        game.running= False
                
                    game.next_turn()
        if game.gamemode == 'ai' and game.player == ai.player and game.running:
            pygame.display.update()

            row,col= ai.eval(board)
            game.make_move(row,col)
            
            #print(row, col)

            

                    
                     
                    
                    #print(board.squares)

        pygame.display.update()

main()
