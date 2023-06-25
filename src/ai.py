from node import Node
from piece import Piece
import copy
from const import *
from board import Board

class AI:
    
    def __init__(self):
        self.board = Board()
        self.FreshMoves = []
        self.FreshMoveStrings = []
        self.engine = ""
        self.depth = 0
        self.color = "white"
        self.boards_explored = 0
        pass
    
    def eval(self, board):
        
        self.getmoves(board)
        print(self.FreshMoveStrings)
        
        for row in range(Ranks):
            for col in range(Files):
                if(board.squares[row][col].has_piece()):
                    if(board.squares[row][col].piece.color == 'white'):
                        pass
                    else:
                        pass
            
    
    def minimax(self, depth, value, candidate, node):
        # Basic minimax algorithm:
        
        # minimizing (black)
        if(value > newCandidate and depth % 2 != 0):
            newCandidate = value
            if(depth==1):
                move = 0
        
        # maximizing (white)
        elif(value < newCandidate and depth % 2 == 0):
            newCandidate = value
            
        # alpha beta pruning
    
        #(black)
        if (candidate != None and value < candidate and depth % 2 == 0):
            pass
        
        #(white)
        if (candidate != None and value > candidate and depth % 2 != 0):
            pass
            
    def clearmoves(self):
        print("Ping\n")

                
    def getmoves(self, board):

        for row in range(Ranks):
            for col in range(Files):
                if(board.squares[row][col].has_piece()):
                    board.calc_moves(board.squares[row][col].piece, row, col, bool=True)
                    self.FreshMoves.append(board.squares[row][col].piece.moves)
                    self.FreshMoveStrings.append(board.squares[row][col].piece.moveString)