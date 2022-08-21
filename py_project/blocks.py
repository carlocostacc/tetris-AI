import pygame as py
import variables
import sys

class Tetrominos:
    def __init__(self, type, position, level):
        self.level = level
        self.rotation = 0
        self.position = position
        self.temp_position = [self.position[0], self.position[1]]
        self.placed = False

        type_I = [  [0,1,0],
                    [0,1,0],
                    [0,1,0],
                    [0,1,0]]

        type_J = [  [0,2,0],
                    [0,2,0],
                    [2,2,0]]

        type_L = [  [0,3,0],
                    [0,3,0],
                    [0,3,3]]

        type_O = [[4,4,0],
                  [4,4,0],
                  [0,0,0]]

        type_S = [[0,5,5],
                  [5,5,0],
                  [0,0,0]]

        type_Z = [[6,6,0],
                  [0,6,6],
                  [0,0,0]]

        type_T = [[0,7,0],
                  [7,7,7],
                  [0,0,0]]

        self.type = type
        self.types = [type_I, type_J, type_L, type_O, type_S,type_Z, type_T]
        self.block_type = self.types[type]



    def update_postion(self, grid):
        temp = self.temp_position
        speed = self.level * 0.2
        rows = len(self.block_type)
        cols = len(self.block_type[0])
        grid_rows = len(grid)
        grid_cols = len(grid[0])
        grid_position = int((self.position[0])/variables.blocksize - 2), int((self.position[1])/variables.blocksize - 2)
        hit_buttom = False

        if(self.placed == False):
            for i in range(rows):
                for j in range(cols):
                    # checks if the block has touched the buttom of the grid
                    if(self.block_type[rows- i -1][j] != 0 and (grid_position[1] + rows - i) >= grid_rows):
                        hit_buttom = True
                        self.placed = True
                    #check if the block underneath is a occupied or not
                    if((grid_position[1] + rows - i) < 24 and (grid_position[0] + j) < 10):
                        if(self.block_type[rows- i -1][j] != 0 and grid[grid_position[1] + rows - i][grid_position[0] + j] != 0):
                            self.placed = True

            if (int((temp[1] + speed))%variables.blocksize == 0) and hit_buttom == False:
                
                self.position [1]= temp[1]
                self.temp_position[1] = (temp[1] + speed)
            else: 
                self.temp_position[1] = (temp[1] + speed)
                
            
    def draw(self):
        
        rows = len(self.block_type)
        cols = len(self.block_type[0])
        pos = [0,0]
        center = rows//2, cols//2
        if (self.type == 0):
            #for the I block it is different because the matrix is not square
            center = 1,1
            if(rows == 4):
                # I block is in the vertical position
                for i in range(rows):
                    #postition [1][1] is considered as the center
                    if (i < center[0]):
                            pos[1] = self.position[1] - (center[0] - i)*variables.blocksize
                    else:
                        pos[1] = self.position[1] + (i - center[0])*variables.blocksize
                    pos[0] = self.position[0]
                    py.draw.rect(variables.win,variables.black,[pos[0],pos[1],variables.blocksize,variables.blocksize])
                    py.draw.rect(variables.win,variables.colors[self.type],[pos[0],pos[1],variables.blocksize - 2,variables.blocksize - 2])
                 
            else :
                #I block is the horizontal position
                for i in range(cols):
                    #postition [1][1] is considered as the center
                    if (i < center[0]):
                            pos[0] = self.position[0] - (center[0] - i)*variables.blocksize
                    else:
                        pos[0] = self.position[0] + (i - center[0])*variables.blocksize
                    pos[1] = self.position[1]
                    py.draw.rect(variables.win,variables.black,[pos[0],pos[1],variables.blocksize,variables.blocksize])
                    py.draw.rect(variables.win,variables.colors[self.type],[pos[0],pos[1],variables.blocksize - 2,variables.blocksize - 2])
                     
        elif (self.type != 0):
            for i in range(rows):
                for j in range(cols):
                        if(self.block_type[i][j] != 0):
                            #the center is the center of the block matrix self.position of the block drawing is calculated from the center
                            #calculate the where to draw the squares with the given self.position in the argument and the center of the matrix
                            if (i < center[0]):
                                pos[0] = self.position[0] - (center[0] - j)*variables.blocksize
                            else:
                                pos[0] = self.position[0] + (j - center[0])*variables.blocksize
                            if(j < center[1]):
                                pos[1] = self.position[1] - (center[1] - i) * variables.blocksize
                            else :
                                pos[1] = self.position[1] + (i - center[1]) * variables.blocksize
                            
                            py.draw.rect(variables.win,variables.black,[pos[0],pos[1],variables.blocksize,variables.blocksize])
                            py.draw.rect(variables.win,variables.colors[self.type],[pos[0],pos[1],variables.blocksize - 2,variables.blocksize - 2])


    def rotate_block(self):
        #TODO  fix the error when rotating the I block

        rows = len(self.block_type)
        cols = len(self.block_type[0])
        temp = [x[:] for x in [[0] * rows] * cols]
        if(self.type == 0):
            if(rows == 4):
                
                self.rotation = self.rotation = 0
                return [[0,0,0,0],[1,1,1,1],[0,0,0,0]]
            else :
                
                self.rotation = 0
                return [[0,1,0],
                        [0,1,0],
                        [0,1,0],
                        [0,1,0]]
        else:
            if self.rotation == 1:
                for x in range(rows):
                    for y in range(cols):
                        temp[cols - y -1][x] = self.block_type[x][y]

            if self.rotation == 2:
                for x in range(rows):
                    for y in range(cols):
                        temp[x][cols - y -1] = self.block_type[y][x]

            
            self.rotation = 0
            return temp

    def is_move_legal(self,block, position, grid):

        #checks if the moove is legal
        rows = len(block)
        cols = len(block[0])
        grid_rows = len(grid)
        grid_cols = len(grid[0])
        
        if(self.type != 0):
            #position of the top left corner of block matrix in the grid 
            grid_position = int((position[0])/variables.blocksize - 2), int((position[1])/variables.blocksize - 2)
        else:
            #change the position calculation for the I block
            grid_position = int((position[0])/variables.blocksize -1), int((position[1])/variables.blocksize - 2)
        
        for i in range(rows):
            for j in range(cols):

                if ((grid_position[1] + i) < 24 and (grid_position[0] + j < 9)):
                    if(block[i][j] != 0 and grid[grid_position[1] +i][grid_position[0] + j] != 0):
                        #there is already a block there cannot be moved 
                        return False
                # check for attempting too move out of the play area to the left 
                if(self.type != 0):
                    if(block[j][i] != 0 and (grid_position[0] + i) < 0):
                        return False
                else:
                    if(block[i][j] != 0 and (grid_position[0] + i) < 0 and len(self.block_type) == 4):
                        return False
                    else:
                        if (block[i][j] != 0 and (grid_position[0] - i) < 0 and len(self.block_type) == 3):
                            return False

                # check for attempting too move out of the play area to the right
                if(self.type != 0):
                    if (block[j][cols - i - 1] !=0 and (grid_position[0] + (cols - i)) > grid_cols):
                        return False
                else:
                    if (block[i][j] !=0 and (grid_position[0] + (j)) > grid_cols):
                        return False
                # check for attempting too move out of the play area to the buttom 
                if(block[rows- i -1][j] != 0 and (grid_position[1] + rows - i -1) >= grid_rows):
                    return False 
                
        return True


    def move(self, grid):
        #check for side mouvement rotations and lowering the block
        events = py.event.get()
        for event in events:
            if event.type == py.QUIT: sys.exit()
            if event.type == py.KEYDOWN:
                if event.key == py.K_LEFT:
                    if(self.is_move_legal(self.block_type, [self.position[0] - variables.blocksize, self.position[1]], grid)):
                        self.position[0] -= variables.blocksize

                if event.key == py.K_RIGHT:
                    if(self.is_move_legal(self.block_type, [self.position[0] + variables.blocksize, self.position[1]], grid)):
                        self.position[0] += variables.blocksize

                if event.key == py.K_UP:

                    self.rotation = 1
                    temp = self.rotate_block()

                    if(self.is_move_legal(temp, [self.position[0], self.position[1]], grid) and self.type != 3):
                        self.block_type = temp
                    

                if event.key == py.K_DOWN:
                    if(self.is_move_legal(self.block_type, [self.position[0], self.position[1] + variables.blocksize], grid)):
                        self.position[1] += variables.blocksize
                        self.temp_position[1] = self.position[1]
                    

                if event.key == py.K_x:
                    self.rotation = 2
                    temp = self.rotate_block()
                    if(self.is_move_legal(temp, [self.position[0], self.position[1]], grid)):
                        self.block_type = temp

                if event.key == py.K_SPACE:
                    #the block must be placed immidiately
                    self.place_now(grid)
                    
                if event.key == py.K_c:
                    #hold the block
                    pass
        self.update_postion(grid)
        
    def place_now(self, grid):
        #place the block instantly, direclty underneath the current position of the block
        #called when pressing the space bar

            temp = self.position
            rows = len(self.block_type)
            cols = len(self.block_type[0])
            can_be_placed = True
            higher_block = False
            grid_rows = len(grid)
            grid_cols = len(grid[0])
            #grid position might cause some problems down the line
            grid_position = int((self.position[0])/variables.blocksize - 2), int((self.position[1])/variables.blocksize - 2)
            
            for i in range(grid_rows):
                can_be_placed = True
                higher_block = False
                for j in range(cols):
                    #start from the buttom of the grid
                    #only check the position direccly underneath the block
                    #place the block on the fist available poosition
                    if(grid_rows -i-1 ) < 24 and (grid_position[0] + j) < 10:
                        if (grid[grid_rows -i-1][grid_position[0] + j] == 0 and self.block_type[rows - 1][j] != 0):
                            
                            for x in range(rows):
                                for y in range(cols):
                                    for z in range(grid_rows - i):
                                            for y2 in range(cols):
                                            #check if there is a block way higher
                                                if(grid_rows -i- z -1 ) < 24 and (grid_position[0] + y2) < 10:
                                                    if(grid[grid_rows - i - z -1][grid_position[0]+y2] != 0 and self.block_type[rows - (z%3)- 1][y2] != 0):
                                                        higher_block = True
                                    #check if the position found is valid, if there are no blocks around,
                                    #  that would make it impossible to place it there
                                    if(grid_rows -i-1 - x) < 24 and (grid_position[0] + y) < 10:
                                        if(grid[grid_rows -i-1 - x][grid_position[0] + y] != 0 and self.block_type[rows - x- 1][y] != 0):
                                            can_be_placed = False
                                    
                            #checking the buttom of the block
                            #change the position of the block
                            if(can_be_placed and not(higher_block)):
                                if (self.type == 0):
                                    self.position[1] = int(self.position[1]) +((grid_rows - i - 2) - int(self.position[1]/variables.blocksize))*variables.blocksize
                                    self.placed = True
                                    break
                                else: 
                                    self.position[1] = int(self.position[1]) +((grid_rows - i - 1) - int(temp[1]/variables.blocksize))*variables.blocksize
                                    self.placed = True
                                    break
                        else: 
                            if (grid[grid_rows -i-1][grid_position[0] + j] == 0 and self.block_type[rows - 2][j] != 0 and self.block_type[2] == [0,0,0]):
                                for x in range(rows):
                                    for y in range(cols):
                                        for z in range(grid_rows - i):
                                                for y2 in range(cols):
                                                #check if there is a block way higher
                                                    if(grid_rows -i- z -1 ) < 24 and (grid_position[0] + y2) < 10:
                                                        if(grid[grid_rows - i - z -1][grid_position[0]+y2] != 0 and self.block_type[rows - (z%3)- 1][y2] != 0):
                                                            higher_block = True
                                        #check if the position found is valid, if there are no blocks around,
                                        #  that would make it impossible to place it there
                                        if(grid_rows -i-1 - x) < 24 and (grid_position[0] + y) < 10:
                                            if(grid[grid_rows -i-1 - x][grid_position[0] + y] != 0 and self.block_type[rows - x- 1][y] != 0):
                                                can_be_placed = False
                                        
                                #checking the buttom of the block
                                #change the position of the block
                                if(can_be_placed and not(higher_block)):
                                    if (self.type == 0):
                                        self.position[1] = int(self.position[1]) +((grid_rows - i ) - int(self.position[1]/variables.blocksize))*variables.blocksize
                                        self.placed = True
                                        break
                                    else: 
                                        self.position[1] = int(self.position[1]) +((grid_rows - i ) - int(temp[1]/variables.blocksize))*variables.blocksize
                                        self.placed = True
                                        break
                if(self.placed == True):
                    break    
                    


    def get_postion(self):
        return self.position

    def get_placed_status(self):
        if self.placed == True:
            return True
        else : 
            return False

    def get_type(self):
        return self.type

    def get_grid(self):
        return self.block_type

    def set_position(self, position):
        self.position = position

    def get_grid_position(self):
        return int((self.position[0])/variables.blocksize - 2), int((self.position[1])/variables.blocksize - 2)

    def update(self, level, grid):
        self.level = level
        self.draw()
        self.move(grid)
        