from Board import Board

def setup():
    global board, turn, winner
    board = Board(50, 50, 50)
    size(250, 250)
    turn = "O"
    winner = '-'
    
def draw():
    global board, turn, winner
    background(255, 28, 85)
    board.draw()
    textSize(15)
    text("It is " + turn + "'s turn. \nClick on a box to fill it.", 10, 20)
    if winner != '-':
        fill(255)
        textSize(15)
        text("The winner is " + winner + "!", 20, 220)
    
def mousePressed():
    global board, turn, winner
    if board.in_box(mouseX, mouseY, turn):
        if turn == 'X':
            turn = 'O'
        elif turn == 'O':
            turn = 'X'
        
    winner = board.check_winner()
    
