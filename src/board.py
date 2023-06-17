from const import *
from square import Square
from piece import *
from move import Move 
class Board:
    
    def __init__(self):
        self.squares = [[0, 0, 0, 0, 0, 0, 0, 0, 0,] for col in range (Ranks)]
        
        self._create()
        self._add_pieces("white")
        self._add_pieces("black")
        
    def calc_moves(self, piece, row, col):
        '''
            Calculate all the possible valid moves of a specific piece on a specific position
        '''
        def knight_moves():
            possible_moves =[
                (row-2, col-1),
                (row-2, col+1)
            ]
            
            for possible_move in possible_moves:
                possible_move_row, possible_move_col = possible_move
                
                if Square.in_range(possible_move_row, possible_move_col):
                    if self.squares[possible_move_row][possible_move_col].isempty_or_rival(piece.color):
                        # create new squares of the move
                        inital = Square(row, col)
                        final = Square(possible_move_row, possible_move_col)
                        #create new move
                        move = Move(inital, final)
                        # append new valid move
                        piece.add_moves(move)
            
        def pawn_moves():
            steps =1
            
            #vertical moves
            start = row + piece.dir
            end = row + (piece.dir *(1 + steps))
            for move_row in range(start, end, piece.dir):
                if Square.in_range(move_row):
                    if self.squares [move_row][col].isempty():
                        #create initial and final move squares
                        initial = Square(row, col)
                        final = Square (col, move_row)
                        #create a new move
                        move = Move(initial, final)
                        piece.add_moves(move)
                    else:
                        break
                else:
                    break
            
            # for possible_move in possible_moves:
            #     possible_move_row, possible_move_col = possible_move
                
            #     if Square.in_range(possible_move_row, possible_move_col):
            #         if self.squares[possible_move_row][possible_move_col].isempty_or_rival(piece.color):
            #             # create new squares of the move
            #             inital = Square(row, col)
            #             final = Square(possible_move_row, possible_move_col)
            #             #create new move
            #             move = Move(inital, final)
            #             # append new valid move
            #             piece.add_moves(move)
                        
        def lance_moves():
            possible_moves =[
                (col, row-1),
                (col, row-2),
                (col, row-3),
                (col, row-4),
                (col, row-5),
                (col, row-6),
                (col, row-7),
                (col, row-8)
            ]
            
            for possible_move in possible_moves:
                possible_move_row, possible_move_col = possible_move
                
                if Square.in_range(possible_move_row, possible_move_col):
                    if self.squares[possible_move_row][possible_move_col].isempty_or_rival(piece.color):
                        # create new squares of the move
                        initial = Square(row, col)
                        final = Square(possible_move_row, possible_move_col)
                        #create new move
                        move = Move(initial, final)
                        # append new valid move
                        piece.add_moves(move)
                                            
        def silver_moves():
            possible_moves =[
                (row-1, col-1),
                (row-1, col),
                (row-1, col+1),
                (row+1, col-1),
                (row+1, col+1)              
            ]
            
            for possible_move in possible_moves:
                possible_move_row, possible_move_col = possible_move
                
                if Square.in_range(possible_move_row, possible_move_col):
                    if self.squares[possible_move_row][possible_move_col].isempty_or_rival(piece.color):
                        # create new squares of the move
                        inital = Square(row, col)
                        final = Square(possible_move_row, possible_move_col)
                        #create new move
                        move = Move(inital, final)
                        # append new valid move
                        piece.add_moves(move)
        
        def gold_moves():
            possible_moves =[
                (row-1, col-1),
                (row-1, col),
                (row-1, col+1),
                (row, col-1),
                (row, col+1),
                (row+1, col)
            ]
            
            for possible_move in possible_moves:
                possible_move_row, possible_move_col = possible_move
                
                if Square.in_range(possible_move_row, possible_move_col):
                    if self.squares[possible_move_row][possible_move_col].isempty_or_rival(piece.color):
                        # create new squares of the move
                        inital = Square(row, col)
                        final = Square(possible_move_row, possible_move_col)
                        #create new move
                        move = Move(inital, final)
                        # append new valid move
                        piece.add_moves(move)
                            
        def bishop_moves():
            possible_moves =[
                (row-1, col-1),
                (row-1, col+1),
                (row+1, col+1),
                (row+1, col-1),
                (row-2, col-2),
                (row-2, col+2),
                (row+2, col+2),
                (row+2, col-2),
                (row-3, col-3),
                (row-3, col+3),
                (row+3, col+3),
                (row+3, col-3),
                (row-4, col-4),
                (row-4, col+4),
                (row+4, col+4),
                (row+4, col-4),
                (row-5, col-5),
                (row-5, col+5),
                (row+5, col+5),
                (row+5, col-5),
                (row-6, col-6),
                (row-6, col+6),
                (row+6, col+6),
                (row+6, col-6),
                (row-7, col-7),
                (row-7, col+7),
                (row+7, col+7),
                (row+7, col-7),
                (row+8, col-8),
                (row-8, col+8),
                (row+8, col+8),
                (row+8, col-8),
            ]
            
            for possible_move in possible_moves:
                possible_move_row, possible_move_col = possible_move
                
                if Square.in_range(possible_move_row, possible_move_col):
                    if self.squares[possible_move_row][possible_move_col].isempty_or_rival(piece.color):
                        # create new squares of the move
                        inital = Square(row, col)
                        final = Square(possible_move_row, possible_move_col)
                        #create new move
                        move = Move(inital, final)
                        # append new valid move
                        piece.add_moves(move)
                                             
        def rook_moves():
            possible_moves =[
                (row-1, col),
                (row-2, col),
                (row-3, col),
                (row-4, col),
                (row-5, col),
                (row-6, col),
                (row-7, col),
                (row-8, col),
                (row+1, col),
                (row+2, col),
                (row+3, col),
                (row+4, col),
                (row+5, col),
                (row+6, col),
                (row+7, col),
                (row+8, col),
                (row, col-1),
                (row, col-2),
                (row, col-3),
                (row, col-4),
                (row, col-5),
                (row, col-6),
                (row, col-7),
                (row, col-8),
                (row, col+1),
                (row, col+2),
                (row, col+3),
                (row, col+4),
                (row, col+5),
                (row, col+6),
                (row, col+7),
                (row, col+8),
            ]
            
            for possible_move in possible_moves:
                possible_move_row, possible_move_col = possible_move
                
                if Square.in_range(possible_move_row, possible_move_col):
                    if self.squares[possible_move_row][possible_move_col].isempty_or_rival(piece.color):
                        # create new squares of the move
                        inital = Square(row, col)
                        final = Square(possible_move_row, possible_move_col)
                        #create new move
                        move = Move(inital, final)
                        # append new valid move
                        piece.add_moves(move)
                          
        def king_moves():
            possible_moves =[
                (row-1, col-1),
                (row-1, col),
                (row-1, col+1),
                (row+1, col-1),
                (row+1, col),
                (row+1, col+1),
                (row+1, col-1),
                (row, col-1),
                (row-1, col-1),
                (row+1, col+1),
                (row, col+1),
                (row-1, col+1)
            ]
            
            for possible_move in possible_moves:
                possible_move_row, possible_move_col = possible_move
                
                if Square.in_range(possible_move_row, possible_move_col):
                    if self.squares[possible_move_row][possible_move_col].isempty_or_rival(piece.color):
                        # create new squares of the move
                        inital = Square(row, col)
                        final = Square(possible_move_row, possible_move_col)
                        #create new move
                        move = Move(inital, final)
                        # append new valid move
                        piece.add_moves(move)
                        
        if isinstance(piece, Pawn):
            pawn_moves()
        elif isinstance(piece, Lance):
            lance_moves()
        elif isinstance(piece, Knight):
            knight_moves()
        elif isinstance(piece, Silver):
            silver_moves()
        elif isinstance(piece, Gold):
            gold_moves()
        elif isinstance(piece, Bishop):
            bishop_moves()
        elif isinstance(piece, Rook):
            rook_moves()
        elif isinstance(piece, King):
            king_moves()
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