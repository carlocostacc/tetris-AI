
from re import T
import pygame as py
from blocks import Tetrominos
from variables import *
import random as rand



class Canvas:
    def __init__(self):
        self.widht = 10
        self.height = 24
        self.block_speed = 1
        self.level = 1
        self.score = 0
        self.active_block  = Tetrominos(0,[80,40],self.level)
        self.block_previous_pos = []
        self.next_block = Tetrominos(0,[80,80],self.level)

        #adding a shadow of where the block would end up if it kept falling
        #self.block_shadow = 0

        self.grid =[[0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0]]

    def level_up(self):
        if (self.score >= (self.level * 240)):
            self.level += 1

    def score_increase(self):
        self.score += 40

    def check_for_game_over(self):
        #TODO find a way to check for a game over
        pass

    def delete_completed_line(self):
        # make a copy if the original grid 
        # check if there is a row full of non 0 integers
        
        temp =  self.grid
        rows = len(self.grid)
        cols = len(self.grid[0])
        counter = 0
        for i in range(rows):
            counter = 0
            for j in range(cols):
                
                if(temp[i][j] !=0):
                    counter +=1
            if(counter == 10):
                # delete the line and bring all the other lines down by 1
                temp.pop(i)
                temp.insert(0,[0,0,0,0,0,0,0,0,0,0])
                self.grid = temp
                self.score_increase()
                self.level_up()
        

                
    def draw(self):
        
        #grid
        rows = len(self.grid)
        cols = len(self.grid[0])
        
        for x in range(1,rows + 1):
            for y in range(1,cols + 1):
                linev = py.draw.line(win, py.Color(60, 60, 60, 255), (y * blocksize - 2,0),(y* blocksize -2,winHeiht), 2)
                lineh = py.draw.line(win, py.Color(60, 60, 60, 255), (0,x * blocksize -2),(winWight - information,x*blocksize -2),2)

        #edges of the game board
        for x in range (26):
            for y in range(12):
                if y == 0 or y== 11 or x == 0 or x == 25:
                    
                    if y!=11 and x!=25:
                        s = py.Surface((blocksize,blocksize))
                        s.set_alpha(128)
                        s.fill(pinkish)
                        win.blit(s,[y*blocksize,x*blocksize])
                        s2 = py.Surface((38,38))
                        s2.fill(grey_border)
                        win.blit(s2,[y*blocksize,x*blocksize])

                    else:
                        s = py.Surface((blocksize,blocksize))
                        s.set_alpha(128)
                        s.fill(pinkish)
                        win.blit(s,[y*blocksize -2,x*blocksize -2])
                        s2 = py.Surface((38,38))
                        s2.fill(grey_border)
                        win.blit(s2,[y*blocksize,x*blocksize])
        s = py.Surface((2, winHeiht))
        s.set_alpha(128)
        s.fill(pinkish)
        win.blit(s,[ winWight - information - 2, 0])

        # write the score, highscore and level 
        font = py.font.SysFont(None, 48)
        img = font.render('Score', True, text_color)
        win.blit(img, (winWight - information/2 -50, 20))
        img2 = font.render(str(self.score), True, text_color)
        win.blit(img2, (winWight - information/2 -20, 55))

        img = font.render('level', True, text_color)
        win.blit(img, (winWight - information/2 -50, 120))
        img2 = font.render(str(self.level), True, text_color)
        win.blit(img2, (winWight - information/2 -20, 155))

        img = font.render('high score', True, text_color)
        win.blit(img, (winWight - information/2 -80, 220))
        img2 = font.render("0", True, text_color)
        win.blit(img2, (winWight - information/2 -20, 255))




    def draw_blocks(self):
        #go throught the grid and draw the squares represented by non 0 integers
        rows = len(self.grid)
        cols = len(self.grid[0])
        for i in range(rows):
            zeros = 0
            for j in range(cols):
                if(self.grid[rows - 1 - i][j] != 0):
                    color = self.grid[rows - 1 - i][j] - 1
                    pos =  (j + 1) *blocksize,(rows - i)*blocksize
                    py.draw.rect(win,black,[pos[0],pos[1],blocksize,blocksize])
                    py.draw.rect(win,colors[color],[pos[0],pos[1],blocksize - 2,blocksize -2])
                    
                else: 
                    zeros += 1
                if(zeros == 10):
                    break
            if(zeros == 10):
                    break

    def get_grid(self):
        return self.grid

    def spawn_block(self):
        del self.active_block
        self.active_block = self.next_block
        del self.next_block
        self.next_block = self.next_block = Tetrominos(rand.randrange(0,7,1),[80,80],self.level)

    def update_block_grid(self):
        block = self.active_block.get_grid()
        rows = len(block)
        cols = len(block[0])
        grid_position = self.active_block.get_grid_position()
        placed  = self.active_block.get_placed_status()
        
        if ( placed == True):
            
            #copy the position of the block and delete the block afterward
            for i in range(rows):
                for j in range(cols):
                    if(block[i][j] != 0):
                        if(grid_position[1] + i > 23):

                            self.grid[23][grid_position[0] + j] = block[i][j]
                        else:
                            self.grid[grid_position[1] + i][grid_position[0] + j] = block[i][j]
            self.delete_completed_line()
            self.spawn_block()
            
                        


    def update(self):
        # update the array with the actual position of the falling blocks 
        # delete lines that are completed
        # check if the falling block has touched the blocks that are already placed 
        
        self.draw()
        self.update_block_grid()
        self.draw_blocks()
        self.active_block.update(self.level, self.grid)
        
        