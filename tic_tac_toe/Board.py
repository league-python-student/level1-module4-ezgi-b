class Box:
    def __init__(self, x, y, side_length):
        self.x = x
        self.y = y
        self.side_length = side_length
        self.s = '-'
    def in_box(self, x, y, s):
        if x >= self.x and x <= self.x + self.side_length and y >= self.y and y <= self.y + self.side_length:
            if self.s == '-':
                self.s = s
                return True
        return False
            
    def change_shape(self, s):
        self.s = s
    def draw(self):
        push()
        fill(255)
        rect(self.x, self.y, self.side_length, self.side_length)
        fill(0)
        textSize(30)
        if self.s == 'X':
            text('X', self.x + 15, self.y + self.side_length - 10)
        if self.s == 'O':
            text('O', self.x + 15, self.y + self.side_length - 10)
        pop()

class Board:
    def __init__(self, x, y, side_length):
        self.x = x
        self.y = y
        self.side_length = side_length
        self.board = list()
        for j in range(3):
            layer = list()
            for i in range(3):
                layer.append(Box(self.x + side_length*i, y + side_length*j, side_length))
            self.board.append(layer)
    def draw(self):
        for layer in self.board:
            for b in layer:
                b.draw()
    def in_box(self, x, y, s):
        for layer in self.board:
            for b in layer:
                if b.in_box(x, y, s):
                    return True
        
    def check_horizontal(self):
        for layer in self.board:
            total = 0
            for b in layer:
                if b.s == 'X':
                    total += 1
                if b.s =='O':
                    total += -1
            if total == -3:
                return 'O'
            if total == 3:
                return 'X'
        return '-'
    
    def check_vertical(self):
        for i in range(3):
            total = 0
            for j in range(3):
                if self.board[j][i] == 'X':
                    total += 1
                if self.board[j][i] =='O':
                    total += -1
            if total == -3:
                return 'O'
            if total == 3:
                return 'X'
        return '-'
    
    def check_diagonal(self):
        total = 0
        for i in range(3):
            if self.board[i][i] == 'X':
                total += 1
            if self.board[i][i] =='O':
                total += -1
        if total == -3:
            return 'O'
        if total == 3:
            return 'X'
        total = 0
        for i in range(3):
            if self.board[2-i][2-i] == 'X':
                total += 1
            if self.board[2-i][2-i] =='O':
                total += -1
        if total == -3:
            return 'O'
        if total == 3:
            return 'X'
        return '-'
        
    def check_winner(self):
        if check_horizontal() == 'X' or check_vertical() == 'X' or check_diagonal() == 'X':
            return "X"
        if check_horizontal() == 'O' or check_vertical() == 'O' or check_diagonal() == 'O':
            return "O"
        return '-'
