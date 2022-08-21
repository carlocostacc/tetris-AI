
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

    def check_for_line_completion(self):
        occupied = 0
        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                if(self.grid[i][j] != 0):
                    occupied += 1
                if(j == 9 and occupied == 10):
                    return i
        return -1

    def delete_completed_line(self):
        line =  self.check_for_line_completion()
        if(line != -1):
            for i in range(len(self.grid[0])):
                self.grid[line][i] = 0
            temp = []
            temp2 = []
            for i in range(line + 1):
                if(i == 0):
                    temp = self.grid[i]
                    self.grid[i] = [0,0,0,0,0,0,0,0,0,0]
                else: 
                    self.grid[i] = temp2
                    self.grid[i]  = temp
                    temp = temp2
            self.score_increase
            print("lines were deleted")

                
    def draw(self):
        
        #grid
        rows = len(self.grid)
        cols = len(self.grid[0])
        
        for x in range(1,rows + 1):
            for y in range(1,cols + 1):
                linev = py.draw.line(win, py.Color(60, 60, 60, 255), (y * 40 - 2,0),(y* 40 -2,winHeiht), 2)
                lineh = py.draw.line(win, py.Color(60, 60, 60, 255), (0,x * 40 -2),(winWight,x*40 -2),2)

        #edges of the game board
        for x in range (26):
            for y in range(12):
                if y == 0 or y== 11 or x == 0 or x == 25:
                    
                    if y!=11 and x!=25:
                        s = py.Surface((40,40))
                        s.set_alpha(128)
                        s.fill(pinkish)
                        win.blit(s,[y*40,x*40])
                        s2 = py.Surface((38,38))
                        s2.fill(grey_border)
                        win.blit(s2,[y*40,x*40])

                    else:
                        s = py.Surface((40,40))
                        s.set_alpha(128)
                        s.fill(pinkish)
                        win.blit(s,[y*40 -2,x*40 -2])
                        s2 = py.Surface((38,38))
                        s2.fill(grey_border)
                        win.blit(s2,[y*40,x*40])

    def draw_blocks(self):
        #go throught the grid and draw the squares represented by non 0 integers
        rows = len(self.grid)
        cols = len(self.grid[0])
        
        for i in range(rows):
            zeros = 0
            for j in range(cols):
                if(self.grid[rows - 1 - i][j] != 0):
                    color = self.grid[rows - 1 - i][j] - 1
                    pos =  (j + 1) *40,(rows - i)*40
                    py.draw.rect(win,black,[pos[0],pos[1],40,40])
                    py.draw.rect(win,colors[color],[pos[0],pos[1],38,38])
                    
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
                        self.grid[grid_position[1] + i][grid_position[0] + j] = block[i][j]
            self.delete_completed_line()
            self.spawn_block()
            print(self.grid)
            
                        


    def update(self):
        # update the array with the actual position of the falling blocks 
        # delete lines that are completed
        # check if the falling block has touched the blocks that are already placed 
        
        self.draw()
        self.update_block_grid()
        self.draw_blocks()
        self.active_block.update(self.level, self.grid)
        
        