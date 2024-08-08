print( "Welcome to my game of Tic Tac Toe!" )
input("Press the Enter key to continue: ") 

def gameturn (turn):
    q = "1"
    w = "2"
    e = "3"
    r = "4"
    t = "5"
    y = "6"
    u = "7"
    i = "8"
    o = "9"

    print ( q + "|" + w + "|" + e )
    print ( r + "|" + t + "|" + y )
    print ( u + "|" + i + "|" + o )
    
x = True
while x:
    print(" ")
    turn = input ( "enter 1 to go first or 2 to go second \n" )
    
    if turn == "1":
        print( "\nYou are X, you will go first" )
        x = False
    elif turn == "2":
        print ( "\nYou are O, you will go second")
        x = False
        gameturn(turn)

