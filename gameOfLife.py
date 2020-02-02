
import time
import random
import pygame

# grid info
grid = []
gridSize = 100

def gridGen():
    
    x, y = gridSize, gridSize
    for i in range(x):
        grid.append([])
        for j in range(y):
            grid[-1].append(random.randint(0, 1))
    
    #edge
    #for i in range(gridSize):
    #    for j in range(gridSize):
            #if (i == 0 or i == gridSize) or (j == 0 or j == gridSize):
            #    grid[i][j] = 0
    #        pass
    return grid

def neighbours(x, y):
    
    return [grid[x][y + 1], grid[x][y - 1],
            grid[x + 1][y], grid[x - 1][y],
            grid[x + 1][y + 1], grid[x - 1][y - 1],
            grid[x + 1][y - 1], grid[x - 1][y + 1]]

def liveOrDie(cell, x, y):
    
    nb = sum(neighbours(x,y))
    if cell == 1 and nb < 2: return 0
    elif cell == 1 and nb in range(2, 4): return 1
    elif cell == 1 and nb > 3: return 0
    elif cell == 0 and nb == 3: return 1
    else: return 0

gridGen()
def engine():
    
    newGen = grid
    for x in range(1, gridSize - 1):
        for y in range(1, gridSize - 1):
            # cell live or die
            newGen[x][y] = liveOrDie(grid[x][y], x, y)

# PyGame
pygame.init()
screen = pygame.display.set_mode((gridSize * 10 , gridSize * 10), 0, 32)

#Colour
gray  = [20, 20, 20]
white = [255, 255, 255]
black = [0, 0, 0]

#Display
pygame.display.set_caption("Game Of Life")
screen.fill(gray)
pygame.display.flip()


while True:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    #run engine
    engine()
    #update screen
    pygame.display.update()
    i, j = 0, 0
    for y in range(0, gridSize * 10, 10):
        for x in range(0, gridSize * 10, 10):
            if grid[i][j] == 1:
                pygame.draw.rect(screen, white, [x, y, 8, 8])
            else:
                pygame.draw.rect(screen, black, [x, y, 8, 8])
            j += 1
        i += 1
        j = 0
