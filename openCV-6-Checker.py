import cv2
print (cv2.__version__)
import numpy as np

boardSize= int(input('what size is the board?  '))
numSquares = int (input('How many squars?  '))
squareSize = int(boardSize/numSquares)

darkColor = (0,0,0)
lightColor = (0,0,255)
nowColor= darkColor

while True:
    gameBoard =np.zeros([boardSize,boardSize,3],dtype=np.uint8)
    for row in range (0,numSquares):
        for column in range (0,numSquares):
            gameBoard[squareSize*row:squareSize*(row+1),squareSize*column:squareSize*(column+1)] = nowColor
            if nowColor == darkColor:
                nowColor=lightColor
            else:
                nowColor=darkColor

        if nowColor == darkColor:
                nowColor=lightColor
        else:
            nowColor=darkColor


    cv2.imshow('CheckerBoard', gameBoard)
    if cv2.waitKey(1) & 0xff==ord('q'):
        break