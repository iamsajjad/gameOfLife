
import time
import random
import pygame
from copy import deepcopy

class GameOfLife:

    def __init__(self, gridSize=50):
        
        self.grid = []
        self.newGen = []
        self.gridSize = gridSize
        
        x, y = self.gridSize, self.gridSize
        for i in range(x):
            self.grid.append([])
            for j in range(y):
                self.grid[-1].append(random.randint(0, 1))
        
    def countNeighbours(self, x, y):
        
        counter = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                col = (x + i + self.gridSize) % self.gridSize
                row = (y + j + self.gridSize) % self.gridSize
                counter += self.grid[col][row]
        counter -= self.grid[x][y]
        
        return counter

    def liveOrDie(self, x, y):
        
        state = self.grid[x][y]
        neighbours = self.countNeighbours(x,y)

        if state == 0 and neighbours == 3:
            return 1 
        elif state == 1 and (neighbours < 2 or neighbours > 3):
            return 0
        else:
            return state

    def engine(self):
        
        self.newGen = deepcopy(self.grid)
        for x in range(1, self.gridSize):
            for y in range(1, self.gridSize):
                # cell live or die
                self.newGen[x][y] = self.liveOrDie(x, y)
        self.grid = deepcopy(self.newGen)

    def draw(self):
        
        # PyGame1
        pygame.init()
        screen = pygame.display.set_mode((self.gridSize * 10 , self.gridSize * 10), 0, 32)

        #Colour
        gray  = [20, 20, 20]
        white = [255, 255, 255]
        black = [0, 0, 0]

        #Display
        pygame.display.set_caption("Game Of Life")
        screen.fill(gray)
        pygame.display.flip()

        while True: 

            #run engine
            self.engine()

            #update screen
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            
            for i, y in enumerate(range(0, self.gridSize * 10, 10)):
                for j, x in enumerate(range(0, self.gridSize * 10, 10)):
                    if self.newGen[i][j] == 1:
                        pygame.draw.rect(screen, white, [x, y, 8, 8])
                    else:
                        pygame.draw.rect(screen, black, [x, y, 8, 8])
    
GameOfLife().draw()

