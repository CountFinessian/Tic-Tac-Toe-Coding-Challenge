from Mechanics import playgame

print( "Welcome to my game of Tic Tac Toe!" )
input("Press the Enter key to continue: ") 


x = True
while x:
    
    turn = input ( "enter 0 to go first or 1 to go second: " )
    
    if turn == "0":
        print( "\nYou are X, you will go first" )
        x = False
        playgame(0)
    elif turn == "1":
        print ( "\nYou are O, you will go second")
        x = False
        playgame(1)

# end of game to delcare a winner or ask to play again.