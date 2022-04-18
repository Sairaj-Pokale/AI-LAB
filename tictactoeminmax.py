import random

Player = 'O'
AI = 'X'

Board = {1:' ', 2:' ',3:' ',
         4:' ', 5:' ', 6:' ',
         7:' ', 8:' ', 9:' ' }


def printBoard(Board):
    print(Board[1]+ '|' + Board[2]+ '|' + Board[3])
    print('-+-+-')
    print(Board[4]+ '|' + Board[5]+ '|' + Board[6])
    print('-+-+-')
    print(Board[7]+ '|' + Board[8]+ '|' + Board[9])
    print('\n')

def checkFree(position):
    if(Board[position]==' '):
        return True
    return False

def placeInput(move, position):
    if checkFree(position):
        Board[position] = move
        printBoard(Board)
        if checkDraw():
            print("\nDraw!!\n")
            exit()
        if checkWin():
            if move == 'X':
                print("\nI WON, YOU LOST, BETTER LUCK NEXT TIME :P\n")
                exit()
            else:
                print("\nYOU WON\n")
                exit
        return



    else:
        print("Space occupied, try again!!\n")
        position = int(input("Input Position: "))
        placeInput(move, position)
        return


def checkWin():
    if (Board[1] == Board[2] and Board[1] == Board[3] and Board[1] != ' '):
        return True
    elif (Board[4] == Board[5] and Board[4] == Board[6] and Board[4] != ' '):
        return True
    elif (Board[7] == Board[8] and Board[7] == Board[9] and Board[7] != ' '):
        return True
    elif (Board[1] == Board[4] and Board[1] == Board[7] and Board[1] != ' '):
        return True
    elif (Board[2] == Board[5] and Board[2] == Board[8] and Board[2] != ' '):
        return True
    elif (Board[3] == Board[6] and Board[3] == Board[9] and Board[3] != ' '):
        return True
    elif (Board[1] == Board[5] and Board[1] == Board[9] and Board[1] != ' '):
        return True
    elif (Board[7] == Board[5] and Board[7] == Board[3] and Board[7] != ' '):
        return True
    else:
        return False

def checkMarkWin(mark):
    if (Board[1] == Board[2] and Board[1] == Board[3] and Board[1] == mark):
        return True
    elif (Board[4] == Board[5] and Board[4] == Board[6] and Board[4] == mark):
        return True
    elif (Board[7] == Board[8] and Board[7] == Board[9] and Board[7] == mark):
        return True
    elif (Board[1] == Board[4] and Board[1] == Board[7] and Board[1] == mark):
        return True
    elif (Board[2] == Board[5] and Board[2] == Board[8] and Board[2] == mark):
        return True
    elif (Board[3] == Board[6] and Board[3] == Board[9] and Board[3] == mark):
        return True
    elif (Board[1] == Board[5] and Board[1] == Board[9] and Board[1] == mark):
        return True
    elif (Board[7] == Board[5] and Board[7] == Board[3] and Board[7] == mark):
        return True
    else:
        return False        

def checkDraw():
    for key in Board.keys():
        if Board[key] == ' ':
            return False       
    return True   

def compMove(firstMove):
    if firstMove:
        movelist = [1,2,3,4,5,6,7,8,9]
        m = random.choice(movelist)
        print("\nAI's Move\n")
        placeInput(AI, m)

    else:   
        bestScore = -800
        bestMove = 0

        for key in Board.keys():
            if Board[key] == ' ':
                Board[key] = AI
                score = minmax(Board, 0, False)
                Board[key] = ' '
                if score > bestScore:
                    bestScore = score
                    bestMove = key
        print("\nAI's Move\n")
        placeInput(AI, bestMove)
        return

def minmax(board, depth, isMaximizing):
    if checkMarkWin(AI):        #defining terminal states of the game
        return 1
    elif checkMarkWin(Player):
        return -1
    elif checkDraw():
        return 0

    if isMaximizing:          #to check the Maximizing score/move
        bestScore = -800
        for key in Board.keys():
            if Board[key] == ' ':
                Board[key] = AI
                score = minmax(Board, depth+1, False)
                Board[key] = ' '
                if score > bestScore:
                    bestScore = score
        return bestScore

    else:                   #to check the Minimizing score/move
        bestScore = 800
        for key in Board.keys():
            if Board[key] == ' ':
                Board[key] = Player
                score = minmax(Board, depth+1, True)
                Board[key] = ' '
                if score < bestScore:
                    bestScore = score
        return bestScore



def playerMove():
    position = int(input("Enter the position for your move, player : "))
    placeInput(Player, position)
    return

def player2Move():
    position = int(input("Enter the position for your move: "))
    placeInput(AI, position)
    return








printBoard(Board)
print("Positions are as follow:")
print("1, 2, 3 ")
print("4, 5, 6 ")
print("7, 8, 9 ")
print("\n")
flag = input("Would you like to go first ? Input yes or no : ")
print()
if(flag=="yes"):
    while not checkWin():
    #player2Move()
        
        playerMove()
        compMove(False)

elif(flag=="no"):
    compMove(True) 
    while not checkWin():
    #player2Move()
       
        playerMove()
        compMove(False)



"""
placeInput('X',1) DRAW MAT
placeInput('X',5)
placeInput('O',9)
placeInput('O',3)
placeInput('O',2)
placeInput('X',6)
placeInput('X',8)
placeInput('O',4)
placeInput('O',7)
"""
