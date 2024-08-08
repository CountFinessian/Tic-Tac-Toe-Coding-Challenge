# have a board which is just an array
q = "1"
w = "2"
e = "3"
r = "4"
t = "5"
y = "6"
u = "7"
i = "8"
o = "9"

movesToMake = (1, 2, 3, 4, 5, 6, 7, 8, 9)
gameboard = (q, w, e, r, t, y, u, i, o)

def printboard ( gameboard ):
    print ( gameboard[0] + "|" + gameboard[1] + "|" + gameboard[2] )
    print ( gameboard[3] + "|" + gameboard[4] + "|" + gameboard[5] )
    print ( gameboard[6] + "|" + gameboard[7] + "|" + gameboard[8] )


def computer( movesToMake ):
    pass

def playgame (turn):
    # mechanics to make the turn happen

    if turn:
        computer ( turn )
    else:
        print ( " please enter the move you'd like to make (1-9)")
        printboard (gameboard)
        computer ( turn )
    
