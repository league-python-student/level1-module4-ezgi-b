from Board import Board

def setup():
    global board, turn
    board = Board(50, 50, 50)
    size(250, 250)
    turn = "O"
    
def draw():
    global board, turn
    background(255, 28, 85)
    board.draw()
    textSize(15)
    text("It is " + turn + "'s turn. \nClick on a box to fill it.", 10, 20)
    
def mousePressed():
    global board, turn
    if board.in_box(mouseX, mouseY, turn):
        if turn == 'X':
            turn = 'O'
        elif turn == 'O':
            turn = 'X'
        
    ##winner = board.check_winner()
    ##if winner != '-':
        ##textSize(15)
        ##text("The winner is " + winner + "!", 220, 20)
