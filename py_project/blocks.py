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
        grid_position = int((self.position[0])/40 - 2), int((self.position[1])/40 - 2)
        hit_buttom = False

        for i in range(rows):
            for j in range(cols):
                if(self.block_type[rows- i -1][j] != 0 and (grid_position[1] + rows - i) >= grid_rows):
                    hit_buttom = True
                    self.placed = True
    
                
        if (int((temp[1] + speed))%40 == 0) and hit_buttom == False:
            
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
                            pos[1] = self.position[1] - (center[0] - i)*40
                    else:
                        pos[1] = self.position[1] + (i - center[0])*40
                    pos[0] = self.position[0]
                    py.draw.rect(variables.win,variables.black,[pos[0],pos[1],40,40])
                    py.draw.rect(variables.win,variables.colors[self.type],[pos[0],pos[1],38,38])
                 
            else :
                #I block is the horizontal position
                for i in range(cols):
                    #postition [1][1] is considered as the center
                    if (i < center[0]):
                            pos[0] = self.position[0] - (center[0] - i)*40
                    else:
                        pos[0] = self.position[0] + (i - center[0])*40
                    pos[1] = self.position[1]
                    py.draw.rect(variables.win,variables.black,[pos[0],pos[1],40,40])
                    py.draw.rect(variables.win,variables.colors[self.type],[pos[0],pos[1],38,38])
                     
        elif (self.type != 0):
            for i in range(rows):
                for j in range(cols):
                        if(self.block_type[i][j] != 0):
                            #the center is the center of the block matrix self.position of the block drawing is calculated from the center
                            #calculate the where to draw the squares with the given self.position in the argument and the center of the matrix
                            if (i < center[0]):
                                pos[0] = self.position[0] - (center[0] - j)*40
                            else:
                                pos[0] = self.position[0] + (j - center[0])*40
                            if(j < center[1]):
                                pos[1] = self.position[1] - (center[1] - i) * 40
                            else :
                                pos[1] = self.position[1] + (i - center[1]) * 40
                            
                            py.draw.rect(variables.win,variables.black,[pos[0],pos[1],40,40])
                            py.draw.rect(variables.win,variables.colors[self.type],[pos[0],pos[1],38,38])


    def rotate_block(self):
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
        #position of the top left corner of block matrix in the grid 
        grid_position = int((position[0])/40 - 2), int((position[1])/40 - 2)
        print(grid_position)
        for i in range(rows):
            for j in range(cols):
                #print(block[i][j])
                #print(grid[grid_position[1] +i][grid_position[0] + j])
                if ((grid_position[1]) > 0 and (grid_position[0] < 10)):
                    if(block[i][j] != 0 and grid[grid_position[1] +i][grid_position[0] + j] != 0):
                        #there is already a block there cannot be moved 
                        print("1")
                        return False
                # check for attempting too move out of the play area to the left 
                if(block[j][i] != 0 and (grid_position[0] + i) < 0):
                    print("2")
                    return False
                # check for attempting too move out of the play area to the right
                if (block[j][cols - i - 1] !=0 and (grid_position[0] + (cols - i)) > grid_cols):
                    print("3")
                    print((grid_position[0] + (cols - i)))
                    print(grid_cols)
                    return False
                # check for attempting too move out of the play area to the buttom 
                if(block[rows- i -1][j] != 0 and (grid_position[1] + rows - i -1) >= grid_rows):
                    print(grid_position[1] + rows - i)
                    print(grid_rows)
                    print("4")
                    return False 
                
        return True


    def move(self, grid):
        #check for side mouvement rotations and lowering the block
        events = py.event.get()
        for event in events:
            if event.type == py.QUIT: sys.exit()
            if event.type == py.KEYDOWN:
                if event.key == py.K_LEFT:
                    if(self.is_move_legal(self.block_type, [self.position[0] - 40, self.position[1]], grid)):
                        self.position[0] -= 40

                if event.key == py.K_RIGHT:
                    if(self.is_move_legal(self.block_type, [self.position[0] + 40, self.position[1]], grid)):
                        self.position[0] += 40

                if event.key == py.K_UP:

                    self.rotation = 1
                    temp = self.rotate_block()
                    if(self.is_move_legal(temp, [self.position[0], self.position[1]], grid)):
                        self.block_type = temp
                    

                if event.key == py.K_DOWN:
                    if(self.is_move_legal(self.block_type, [self.position[0], self.position[1] + 40], grid)):
                        self.position[1] += 40
                        self.temp_position[1] = self.position[1]
                    

                if event.key == py.K_x:
                    self.rotation = 2
                    temp = self.rotate_block()
                    if(self.is_move_legal(temp, [self.position[0], self.position[1]], grid)):
                        self.block_type = temp

                if event.key == py.K_SPACE:
                    #the block must be placed immidiately
                    pass
                if event.key == py.K_c:
                    #hold the block
                    pass
        self.update_postion(grid)
        
    
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
        return int((self.position[0])/40 - 2), int((self.position[1])/40 - 2)

    def update(self, level, grid):
        self.level = level
        self.move(grid)
        self.draw()
        
        
        
        