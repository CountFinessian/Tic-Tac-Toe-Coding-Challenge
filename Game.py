# Run this file as the main to play Tic Tac Toe.
from Mechanics import playgame

print( "Welcome to my game of Tic Tac Toe!" )
input("Press the Enter key to continue: ") 


x = True
while x:
    
    turn = input ( "\nPlease enter 0 to go first or 1 to go second: " )
    
    if turn == "0":
        print( "You are X, you will go first\n" )
        playgame(0)
    elif turn == "1":
        print ( "You are O, you will go second\n")
        playgame(1)
    
    # end of game to delcare a winner or ask to play again.
    print( "\nPlay Again?" )
    again = input ( "Enter 0 to Quit Game: ")
    
    if again == "0":
        x = False