import random

# have a board which is just an array
movesToMake = [1, 2, 3, 4, 5, 6, 7, 8, 9]
gameBoard = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

def printboard ( gameBoard ):
    print ( gameBoard[0] + "|" + gameBoard[1] + "|" + gameBoard[2] )
    print ( gameBoard[3] + "|" + gameBoard[4] + "|" + gameBoard[5] )
    print ( gameBoard[6] + "|" + gameBoard[7] + "|" + gameBoard[8] + "\n")


def computer( player ):
    # randomly choose a move inside of movesToMake
    # remove it from the movesToMake and add it to the gameBoard
    randomMove = random.choice(movesToMake)
    movesToMake.remove(randomMove)
    gameBoard[randomMove - 1] = player
    print ("The computer made its move\n")

def maketurn ( player ):
    x = True
    while x:
        printboard (gameBoard)
        position = input ( "Please enter the move corresponding to the number on the board: " )

        try:
            position = int(position)
            if position in movesToMake:
                movesToMake.remove(position)
                gameBoard[position - 1] = player
                x = False
            else:
                print ("Place is already taken, try again.")

        except ValueError:
            print("Error: Cannot convert", position, "to an integer")
            
def playgame (turn):
    # mechanics to make the turn happen
    x = True
    while x:
    
        if turn == 0:
            maketurn ( "X" )
            computer ( "O" )

        elif turn == 1:
            computer ( "X" )
            maketurn ( "O" )
    
    # needs to check at the end of one of the critera to end the game is met 
    # returns the neccessary winner (player X or player O)
