from operator import ne
from turtle import screensize
import pygame, sys


def main():
    #init pygame variables
    pygame.init()
    white = (0,0,0)
    black = (255,255,255)
    blockSize = 20
    numOfRows = 25
    numOfColumns = 25
    windowSize = width, height = numOfRows * (blockSize +1), numOfColumns * (blockSize + 1)
    screen = pygame.display.set_mode(windowSize)
    screen.fill(white)

    drawBoardScreen(blockSize, windowSize[1], windowSize[0], screen, black)
    pygame.display.update()



    #init board values

    board = initBoard(numOfRows, numOfColumns)
    changedBoard = board
    userInput = ""
    
    #game loop
    while userInput != "n":    
        drawBoard(board,numOfRows,numOfColumns)
        updateBoard(board, numOfRows, numOfColumns, changedBoard)

        board = changedBoard
        userInput = input("type n to stop")

def drawBoard(board, rows, columns):
    for row in range(rows):
        for column in range(columns):
            if column == 0:
                print("|" + str(board[row][column]), end="|")
            else:
                print(board[row][column], end="|")
        print()

def updateBoard(board, rows, columns, changedBoard):
    for row in range(rows):
        for column in range(columns):
            neighbors = getNeighbors(board, row, column,columns, rows)
            numOfAlive = 0
            numOfDead = 0
            for i in range(len(neighbors)):
                if neighbors[i] == 1:
                    numOfAlive += 1
                elif neighbors[i] == 0:
                    numOfDead += 1

            if board[row][column] == 1:
                if numOfAlive < 2:
                    changedBoard[row][column] = 0
                elif numOfAlive > 3:
                    changedBoard[row][column] = 0
            else:
                if numOfAlive == 3:
                    changedBoard[row][column] = 1

            #print(str(row) + str(column) + "| " + str(numOfDead) + " | " + str(numOfAlive))
    
def getNeighbors(board, row, column, numOfColumns, numOfRows):
    #0 = Dead
    #1 = Alive
    #2 = Out of bounds
    #3 not checked 

    #neighbors index postions
    #0 1 2
    #3 * 4
    #5 6 7
    neighbors = [3, 3, 3, 3, 3, 3, 3, 3]
    
    #check for out of bounds

    #check if cell is in top row
    if row == 0:
        neighbors[0] = 2
        neighbors[1] = 2
        neighbors[2] = 2
    
    if row == numOfRows -1:
        neighbors[5] = 2
        neighbors[6] = 2
        neighbors[7] = 2

    if column == 0:
        neighbors[0] = 2
        neighbors[3] = 2
        neighbors[5] = 2

    if column == numOfColumns -1:
        neighbors[2] = 2
        neighbors[4] = 2
        neighbors[7] = 2

    #-1 -1 | -1  0 | -1 +1
    #0  -1 |    *  | 0 +1
    #+1 -1 | +1  0 | +1 +1

    if neighbors[0] != 2:
        neighbors[0] = board[row -1] [column -1]

    if neighbors[1] != 2:
        neighbors[1] = board[row -1] [column]

    if neighbors[2] != 2:
        neighbors[2] = board[row -1] [column + 1]

    if neighbors[3] != 2:
        neighbors[3] = board[row] [column -1]

    if neighbors[4] != 2:
        neighbors[4] = board[row] [column + 1]

    if neighbors[5] != 2:
        neighbors[5] = board[row +1] [column -1]

    if neighbors[6] != 2:
        neighbors[6] = board[row +1] [column]

    if neighbors[7] != 2:
        neighbors[7] = board[row +1] [column+1]

    return neighbors

def initBoard(numOfRows, numOfColumns):
    board = [[1 for x in range(numOfRows)] for y in range(numOfColumns)]
    return board

def drawBoardScreen(blockSize, height, width, window, color):
    for y in range(height):
        for x in range(width):
            rect = pygame.Rect(x*(blockSize +1) , y*(blockSize +1), blockSize, blockSize)
            pygame.draw.rect(window, color, rect)        
    pygame.display.update()
            
    


if __name__ == "__main__":
    main()

