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
            if piece.color == "white":
                possible_moves =[
                    (col-1, row-2),
                    (col+1, row-2)
                ]
            else:
                possible_moves =[
                    (col-1, row+2),
                    (col+1, row+2)
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
            
        def pawn_moves():
            steps =1
            
            #vertical moves
            start = row + piece.dir
            end = row + (piece.dir *(1 + steps))
            for move_row in range(start, end, piece.dir):
                if Square.in_range(move_row):
                    if self.squares [move_row][col].isempty_or_rival(piece.color):
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
                        
        def straightline_moves(incrs):
            if piece.color == "white":
                for incr in incrs:
                    row_incr, col_incr = incr
                    possible_move_row = row + row_incr
                    possible_move_col = col + col_incr
            else:
                for incr in incrs:
                    row_incr, col_incr = incr
                    possible_move_row = row + row_incr
                    possible_move_col = col + col_incr
                        
                
            while True:
                # while true
                    if Square.in_range(possible_move_row, possible_move_col):
                        
                        initial = Square(row, col)
                        final_piece = self.squares[possible_move_row] [possible_move_col].piece
                        final = Square(possible_move_row, possible_move_col, final_piece)
                        move = Move(initial, final)
                        
                        # empty
                        if self.squares[possible_move_col][possible_move_row].isempty():
                            if bool:
                                # if not self.in_check(piece, move):
                                    # append new move
                                piece.add_moves(move)
                            else:
                                #append new move
                                piece.add_moves(move)
                            
                        # has enemy piece
                        elif self.squares[possible_move_col][possible_move_row].has_rival_piece(piece.color):
                            # append new move
                            piece.add_moves(move)
                            break
                            
                    # if not in range
                    else: break
                    
                    # incrementing incrs
                    possible_move_row = possible_move_row + row_incr
                    possible_move_col = possible_move_col + col_incr
                                            
        def silver_moves():
            if piece.color == "white":
                possible_moves =[
                    (col-1,row-1),
                    (col,row-1),
                    (col+1,row-1),
                    (col-1,row+1),
                    (col+1,row+1)              
                ]
            else:
                possible_moves =[
                    (col-1,row+1),
                    (col,row+1),
                    (col+1,row+1),
                    (col-1,row-1),
                    (col+1,row-1)              
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
        
        def gold_moves():
            if piece.color == "white":
                adjs =[
                    (col, row+1),
                    (col-1, row),
                    (col+1, row),
                    (col-1, row-1),
                    (col, row-1),
                    (col+1, row-1)
                ]
            else:
                adjs =[
                    (col, row-1),
                    (col-1, row),
                    (col+1, row),
                    (col-1, row+1),
                    (col, row+1),
                    (col+1, row+1)
                ]
            
            for possible_move in adjs:
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
                    if self.squares[possible_move_row][possible_move_col].has_team_piece(piece.color):
                        break
                            
                          
        def king_moves():
            possible_moves =[
                (col-1, row-1),
                (col-1, row),
                (col-1, row+1),
                (col+1, row-1),
                (col+1, row),
                (col+1, row+1),
                (col+1, row-1),
                (col, row-1),
                (col-1, row-1),
                (col+1, row+1),
                (col, row+1),
                (col-1, row+1)
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
                    
                    if self.squares[possible_move_row][possible_move_col].has_team_piece(piece.color):
                        break
                
                        
        if isinstance(piece, Pawn):
            pawn_moves()
        
        elif isinstance(piece, Knight):
            knight_moves()
            
        elif isinstance(piece, Silver):
            silver_moves()
            
        elif isinstance(piece, Gold):
            gold_moves()
            
            
        elif isinstance(piece, Lance):
            straightline_moves([
            (0, -1), # up
            ])
            
        elif isinstance(piece, Bishop):
            straightline_moves([
            (-1, 1), #up-right
            (-1, -1), #up-left
            (1, 1), #down-right
            (1, -1) #down-left
            ])
            
        elif isinstance(piece, Rook):
            straightline_moves([
            (-1, 0), #up
            (0, -1), #left
            (1, 0), #down
            (0, 1), #right
            ])
            
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
        #for col in range(Ranks):
         #   self.squares[row_pawn][col] = Square(row_pawn, col, Pawn(color))
            
        #lances
        self.squares[row_other][0] = Square(row_other, 0, Lance(color))
        self.squares[5][5] = Square(5, 5, Lance("white"))
        self.squares[1][8] = Square(1, 8, Lance("white"))
        self.squares[1][8] = Square(1, 8, Lance("white"))

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
        self.squares[2][3] = Square(2, 3, Rook("white"))

            
        # bishops
        if(color == 'white'):
            self.squares[row_elite][1] = Square(row_elite, 1, Bishop(color))
        else:
            self.squares[row_elite][7] = Square(row_elite, 7, Bishop(color))
        self.squares[4][5] = Square(4, 5, Bishop("white"))
            
        # king
        self.squares[row_other][4] = Square(row_other, 1, King(color))