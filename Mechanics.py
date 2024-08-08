import random

# have a board which is just an array
movesToMake = [ 1, 2, 3, 4, 5, 6, 7, 8, 9 ]
gameBoard = [ "1", "2", "3", "4", "5", "6", "7", "8", "9" ]

def printboard ( gameBoard ):
    print ( gameBoard[0] + "|" + gameBoard[1] + "|" + gameBoard[2] )
    print ( gameBoard[3] + "|" + gameBoard[4] + "|" + gameBoard[5] )
    print ( gameBoard[6] + "|" + gameBoard[7] + "|" + gameBoard[8] + "\n" )


def computer( player ):
    # randomly choose a move inside of movesToMake
    # remove it from the movesToMake and add it to the gameBoard
    randomMove = random.choice( movesToMake )
    movesToMake.remove( randomMove )
    gameBoard[ randomMove - 1 ] = player
    print ( "\nThe computer made its move, Look Below" )

def maketurn ( player ):
    x = True
    while x:
        printboard ( gameBoard )
        print( "You are player " + player )
        position = input ( "Please enter your move corresponding to the number on the board: " )

        try:
            position = int( position )
            if position in movesToMake:
                movesToMake.remove( position )
                gameBoard[ position - 1 ] = player
                x = False
            else:
                print ( "Place is already taken, try again.\n" )

        except ValueError:
            print( "Error: Cannot convert " + position + " to an integer\n" )
            

def EOG( player ):
    # checks for three in a row (displays you win or you lose) returns false
    # checks if the board is full (catsgame) returns false
    # returns the winner (player X or player O) and if you won or lost

    def winner ( Y ):
        if ( ( gameBoard[0] == Y and gameBoard[1] == Y and gameBoard[2] == Y ) 
        or  gameBoard[3] == Y and gameBoard[4] == Y and gameBoard[5] == Y
        or gameBoard[6] == Y and gameBoard[7] == Y and gameBoard[8] == Y
        or gameBoard[0] == Y and gameBoard[3] == Y and gameBoard[6] == Y
        or gameBoard[1] == Y and gameBoard[4] == Y and gameBoard[7] == Y
        or gameBoard[2] == Y and gameBoard[5] == Y and gameBoard[8] == Y
        or gameBoard[0] == Y and gameBoard[4] == Y and gameBoard[8] == Y
        or gameBoard[6] == Y and gameBoard[4] == Y and gameBoard[2] == Y ):
            return True
    
    if winner( "X" ):
        printboard ( gameBoard )
        if player == "X":
            print ( "You Win!" )
        else:
            print( "You Lose!" )

        print ( "GAME OVER" )
        return True
    
    if winner( "O" ):
        printboard ( gameBoard )
        if player == "O":
            print ( "You Win!" )
        else:
            print( "You Lose!" )

        print ( "GAME OVER" )
        return True

    if len( movesToMake ) == 0:
        printboard ( gameBoard )
        print ( "Cat's Game!" )
        print ( "GAME OVER" )
        return True
    
    else:
        return False
    
def playgame ( turn ):
    # mechanics to make the turn happen
    while True:
        if turn == 0:
            if EOG( "X" ):
                return
            else:
                maketurn ( "X" )
            if EOG( "X" ):
                return
            else:
                computer ( "O" )

        elif turn == 1:
            if EOG( "O" ):
                return
            else:
                computer ( "X" )
            if EOG( "O" ):
                return
            else:
                maketurn ( "O" )