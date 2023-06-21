from const import *
from square import Square
from piece import *
from move import Move 
import copy

class Board:
    
    def __init__(self):
        self.squares = [[0, 0, 0, 0, 0, 0, 0, 0, 0,] for col in range (Ranks)]
        self.last_move = None
        self._create()
        self._add_pieces("white")
        self._add_pieces("black")
        
    def move(self, piece, move):
        initial = move.initial
        final = move.final
        
        # console board move update
        self.squares[initial.row][initial.col].piece = None
        self.squares[final.row][final.col].piece = piece
        
        # promotion
        if isinstance(piece,Pawn):
            self.check_promotion(piece, final)
        
        if isinstance(piece,Lance):
            self.check_promotion(piece, final)
        
        if isinstance(piece,Knight):
            self.check_promotion(piece, final)
        
        if isinstance(piece,Silver):
            self.check_promotion(piece, final)
        
        if isinstance(piece,Rook):
            self.check_promotion(piece, final)
        
        if isinstance(piece,Bishop):
            self.check_promotion(piece, final)
        
        # move and clear valid moves
        piece.moved = True
        piece.clear_moves()
        
        # set last move
        self.last_move = move
    
    def valid_move(self, piece, move):
        return move in piece.moves
    
    
        # def getvalidMoves(self):
        # moves = self.getAllPossibleMoves()
        # for i in range(len(moves)-1, -1, -1): 
        #     self .makeMove(moves[i])
        #     self.whiteToMove = not self.whiteToMove
        #     if self.inCheck():
        #         moves.remove(moves[i]) 
        #         self.whiteToMove = not self.whiteToMove
        #         self.undoMove()
        #     if len(moves) == 0:     
        #         # ini ngecek apakah checkmate atau ga
        #         if self.inCheck():
        #             self.checkMate = True
        #         else:
        #             self.staleMate = True
        #     else:
        #         self.checkMate = False
        #         self.staleMate = False
        
    def in_check(self, piece, move):
        temp_piece = copy.deepcopy(piece)
        temp_board = copy.deepcopy(self)
        temp_board.move(temp_piece, move)
        
        for row in range(Files):
            for col in range(Ranks):
                if temp_board.squares[row][col].has_rival_piece(piece.color):
                    p = temp_board.squares[row][col].piece
                    temp_board.calc_moves(p, row, col, bool=False)
                    for m in p.moves:
                        if isinstance(m.final.piece, King):
                            return True
        return False
        

    def check_promotion(self, piece, final):
        if(piece.name == "pawn"):
            if(piece.color == "white"):
                if final.row <= 2:
                    self.squares[final.row][final.col].piece = PromotedPawn(piece.color)
            else:
                if final.row >= 6:
                    self.squares[final.row][final.col].piece = PromotedPawn(piece.color)
                    
        elif(piece.name == "knight"):
            if(piece.color == "white"):
                if final.row <= 2:
                    self.squares[final.row][final.col].piece = PromotedKnight(piece.color)
            else:
                if final.row >= 6:
                    self.squares[final.row][final.col].piece = PromotedKnight(piece.color)
                    
        elif(piece.name == "silver"):
            if(piece.color == "white"):
                if final.row <= 2:
                    self.squares[final.row][final.col].piece = PromotedSilver(piece.color)
            else:
                if final.row >= 6:
                    self.squares[final.row][final.col].piece = PromotedSilver(piece.color)
        
        elif(piece.name == "rook"):
            if(piece.color == "white"):
                if final.row <= 2:
                    self.squares[final.row][final.col].piece = Dragon(piece.color)
            else:
                if final.row >= 6:
                    self.squares[final.row][final.col].piece = Dragon(piece.color)
        
        elif(piece.name == "bishop"):
            if(piece.color == "white"):
                if final.row <= 2:
                    self.squares[final.row][final.col].piece = Horse(piece.color)
            else:
                if final.row >= 6:
                    self.squares[final.row][final.col].piece = Horse(piece.color)
        
    def calc_moves(self, piece, row, col, bool=True):
        '''
            Calculate all the possible valid moves of a specific piece on a specific position
        '''
        def knight_moves():
            if piece.color == "white":
                possible_moves =[
                    (row-2, col-1),
                    (row-2, col+1)
                ]
            else:
                possible_moves =[
                    (row+2, col-1),
                    (row+2, col+1)
                ]
                        
            for possible_move in possible_moves:
                possible_move_row, possible_move_col = possible_move
                
                if Square.in_range(possible_move_row, possible_move_col):
                    if self.squares[possible_move_row][possible_move_col].isempty_or_rival(piece.color):
                        # create new squares of the move
                        initial = Square(row, col)
                        final_piece = self.squares[possible_move_row][possible_move_col].piece
                        final = Square(possible_move_row, possible_move_col, final_piece)
                        #create new move
                        move = Move(initial, final)
                        if bool:
                            # check check
                            if not self.in_check(piece, move):
                                piece.add_moves(move)
                            else: break
                        else:
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
                        final_piece = self.squares[move_row][col].piece
                        final = Square (move_row, col, final_piece)
                        #create a new move
                        move = Move(initial, final)
                        
                        if bool:
                            # check check
                            if not self.in_check(piece, move):
                                piece.add_moves(move)
                        else:
                            piece.add_moves(move)

                    else:
                        break
                else:
                    break
                        
        def straightline_moves(incrs):
            # if piece.color == "white":
                for incr in incrs:
                    row_incr, col_incr = incr
                    possible_move_row = row + row_incr
                    possible_move_col = col + col_incr
                    
                    while True:
                        if Square.in_range(possible_move_row, possible_move_col):
                            
                            initial = Square(row, col)
                            final_piece = self.squares[possible_move_row] [possible_move_col].piece
                            final = Square(possible_move_row, possible_move_col, final_piece)
                            move = Move(initial, final)
                            
                            # empty
                            if self.squares[possible_move_row][possible_move_col].isempty():
                                if bool:
                            # check check
                                    if not self.in_check(piece, move):
                                        piece.add_moves(move)
                                    else: break
                                else:
                                    piece.add_moves(move)
                                
                            # has enemy piece
                            elif self.squares[possible_move_row][possible_move_col].has_rival_piece(piece.color):
                                # append new move
                                if bool:
                            # check check
                                    if not self.in_check(piece, move):
                                        piece.add_moves(move)
                                    else: break
                                else:
                                    piece.add_moves(move)
                                break
                            
                            # has friendly piece
                            elif self.squares[possible_move_row][possible_move_col].has_team_piece(piece.color):
                                break
                                
                        # if not in range
                        else: 
                            break
                        
                        # incrementing incrs
                        possible_move_row = possible_move_row + row_incr
                        possible_move_col = possible_move_col + col_incr
                                            
        def silver_moves():
            if piece.color == "white":
                possible_moves =[
                    (row+1,col+1),
                    (row+1,col-1),
                    (row-1,col-1),
                    (row-1,col),
                    (row-1,col+1)              
                ]
            else:
                possible_moves =[
                    (row-1,col+1),
                    (row-1,col-1),
                    (row+1,col-1),
                    (row+1,col),
                    (row+1,col+1)                  
                ]    
            
            for possible_move in possible_moves:
                possible_move_row, possible_move_col = possible_move
                
                if Square.in_range(possible_move_row, possible_move_col):
                    if self.squares[possible_move_row][possible_move_col].isempty_or_rival(piece.color):
                        # create new squares of the move
                        initial = Square(row, col)
                        final_piece = self.squares[possible_move_row][possible_move_col].piece
                        final = Square(possible_move_row, possible_move_col, final_piece)
                        #create new move
                        move = Move(initial, final)
                        # append new valid move
                        if bool:
                            # check check
                            if not self.in_check(piece, move):
                                piece.add_moves(move)
                            else: break
                        else:
                            piece.add_moves(move)
        
        def gold_moves():
            if piece.color == "white":
                adjs =[
                    (row+1, col),
                    (row, col+1),
                    (row, col-1),
                    (row-1, col-1),
                    (row-1, col),
                    (row-1, col+1)
                ]
            else:
                adjs =[
                    (row-1, col),
                    (row, col+1),
                    (row, col-1),
                    (row+1, col-1),
                    (row+1, col),
                    (row+1, col+1)
                ]
            
            for possible_move in adjs:
                possible_move_row, possible_move_col = possible_move
                
                if Square.in_range(possible_move_row, possible_move_col):
                    if self.squares[possible_move_row][possible_move_col].isempty_or_rival(piece.color):
                        # create new squares of the move
                        initial = Square(row, col)
                        final_piece = self.squares[possible_move_row][possible_move_col].piece
                        final = Square(possible_move_row, possible_move_col, final_piece)
                        #create new move
                        move = Move(initial, final)
                        # append new valid move
                        if bool:
                            # check check
                            if not self.in_check(piece, move):
                                piece.add_moves(move)
                            else: break
                        else:
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
                        if bool:
                            # check check
                            if not self.in_check(piece, move):
                                piece.add_moves(move)
                            else: break
                        else:
                            piece.add_moves(move)
                        
        if isinstance(piece, Pawn):
            pawn_moves()
        
        elif isinstance(piece, PromotedPawn):
            gold_moves()
            
        elif isinstance(piece, PromotedLance):
            gold_moves()
            
        elif isinstance(piece, PromotedKnight):
            gold_moves()
            
        elif isinstance(piece, PromotedSilver):
            gold_moves()
            
        elif isinstance(piece, Knight):
            knight_moves()
            
        elif isinstance(piece, Silver):
            silver_moves()
            
        elif isinstance(piece, Gold):
            gold_moves()
            
            
        elif isinstance(piece, Lance):
            if piece.color == "white":
                straightline_moves([
                    (-1, 0), # up
                ])
            else:
                straightline_moves([
                    (1, 0), # up
                ])
            
        elif isinstance(piece, Bishop):
            straightline_moves([
            (-1, 1), #up-right
            (-1, -1), #up-left
            (1, 1), #down-right
            (1, -1) #down-left
            ])
            
        elif isinstance(piece, Horse):
            straightline_moves([
            (-1, 1), #up-right
            (-1, -1), #up-left
            (1, 1), #down-right
            (1, -1) #down-left
            ])
            king_moves()
            
        elif isinstance(piece, Rook):
            straightline_moves([
            (-1, 0), #up
            (0, -1), #left
            (1, 0), #down
            (0, 1), #right
            ])
            
        elif isinstance(piece, Dragon):
            straightline_moves([
            (-1, 0), #up
            (0, -1), #left
            (1, 0), #down
            (0, 1), #right
            ])
            king_moves()
            
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