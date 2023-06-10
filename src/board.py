from const import *
from square import Square
from piece import *

class Board:
    
    def __init__(self):
        self.squares = [[0, 0, 0, 0, 0, 0, 0, 0, 0,] for col in range (Ranks)]
        
        self._create()
        self._add_pieces("white")
        self._add_pieces("black")
        
    def _create(self):
        for row in range(Files):
            for col in range(Ranks):
                self.squares[row][col] = Square(row, col)
    
    def _add_pieces(self, color): 
        if color == 'white':
            row_pawn, row_elite, row_other = (6, 7, 8)
        else:
            row_pawn, row_elite, row_other = (2, 1, 0)
            
        # pawns
        for col in range(Ranks):
            self.squares[row_pawn][col] = Square(row_pawn, col, Pawn(color))
            
        #lances
        self.squares[row_other][0] = Square(row_other, 0, Lance(color))
        self.squares[row_other][8] = Square(row_other, 8, Lance(color))
                
        #knights
        self.squares[row_other][1] = Square(row_other, 1, Knight(color))
        self.squares[row_other][7] = Square(row_other, 7, Knight(color))
            
        #Silvers
        self.squares[row_other][2] = Square(row_other, 2, Silver(color))
        self.squares[row_other][6] = Square(row_other, 6, Silver(color))
        
        #Golds
        self.squares[row_other][3] = Square(row_other, 3, Gold(color))
        self.squares[row_other][5] = Square(row_other, 5, Gold(color))    
            
        #rooks
        if(color == 'white'):
            self.squares[row_elite][7] = Square(row_elite, 7, Rook(color))
        else:
            self.squares[row_elite][1] = Square(row_elite, 1, Rook(color))
            
        # bishops
        if(color == 'white'):
            self.squares[row_elite][1] = Square(row_elite, 1, Bishop(color))
        else:
            self.squares[row_elite][7] = Square(row_elite, 7, Bishop(color))
            
        # king
        self.squares[row_other][4] = Square(row_other, 1, King(color))