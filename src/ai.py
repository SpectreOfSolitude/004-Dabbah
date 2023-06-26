from node import Node
from piece import Piece
from const import *
from board import Board
import copy
import multiprocessing
import time

class AI:
    
    def __init__(self, game):
        self.engine = ""
        self.depth = 0
        self.FreshPiece = []
        self.FreshMoves = []
        self.FreshMoveStrings = []
        self.color = "white"
        self.exploredBoards = []
        self.NumberOfBoards = 0
        self.Checkmate = 10000*game.next_player
        self.Stalemate = 0
        self.scoreMaterial = 0
        self.maxDepth = 5
        self.tree = None
        self.BFSdepth = 1
        
    def getBestMove(self):
        return self.engine(None, 1)

    
    def eval(self, board, color, bool=True):
        
        self.getmoves(board, color)
        # print(self.FreshMoveStrings)
        print("")
        
        # Reset First
        self.scoreMaterial = 0
        
        for row in range(Ranks):
            for col in range(Files):
                if(board.squares[row][col].has_piece()):
                    self.scoreMaterial = self.scoreMaterial + board.squares[row][col].piece.value
                    print(board.squares[row][col].piece.value)
        print("")
        print(f"Current Position Evaluation: {self.scoreMaterial}")
        
        if bool == True:
            self.minimax(self.depth, self.scoreMaterial, board, color)
    
    
    def minimax(self, depth, value, candidate, color):
        # Tree Making
    
        def BFS(nextMoves, value, MoveNames, NewBoard, NewPiece):
            while (nextMoves != []):
                if(MoveNames in self.exploredBoards):
                    temp_value = eval()
                    self.exploredBoards.append(MoveNames)
                    tree.add_child(value, MoveNames)
                    self.NumberOfBoards =+ 1
                
                nextMoves.pop()
                MoveNames.pop()
            BFSdepth = BFSdepth + 1
                    
        def DFS(nextMoves, depth, value, MoveNames, NewBoard, NewPiece):
            while (depth != self.maxDepth):
                if(MoveNames in self.exploredBoards):
                    self.exploredBoards.append(MoveNames)
                    tree.add_child(value, MoveNames)
                    self.NumberOfBoards =+ 1
                
                NewBoard.move(NewPiece, nextMoves) 
                depth = depth + 1
                #eval(NewBoard, depth, ) NEEDS TO BE EDITED
                    
    
        # Root Node
        if (depth == 0):
            tree = Node(value,"Current Pos.") # Rooting
            
            temp_totalMoves = copy.deepcopy(self.FreshMoves)
            temp_MoveStrings = copy.deepcopy(self.FreshMoveStrings)
            temp_piece = copy.deepcopy(self.FreshPiece)
            temp_board = copy.deepcopy(candidate) 
            temp_board.move(temp_piece, temp_totalMoves)
            
            depth = depth + 1
            if (color == 'white'):
                ColorSwap = 'black'
            else:
                ColorSwap = 'white'
                
            self.eval(temp_board, ColorSwap)

            
        else:                
                    
            # minimizing (black)
            if(self.scoreMaterial > value and color == 'black'):
                temp_totalMoves = copy.deepcopy(self.FreshMoves)
                temp_MoveStrings = copy.deepcopy(self.FreshMoveStrings)
                temp_piece = copy.deepcopy(self.FreshPiece)
                temp_board = copy.deepcopy(candidate)
                temp_board.move(temp_piece, temp_totalMoves)
                
                depth = depth + 1
                self.eval(temp_board, "white")
                multiprocessing()
        
            # maximizing (white)
            elif(value < candidate and color == 'white'):
                temp_totalMoves = copy.deepcopy(self.FreshMoves)
                temp_MoveStrings = copy.deepcopy(self.FreshMoveStrings)
                temp_piece = copy.deepcopy(self.FreshPiece)
                temp_board = copy.deepcopy(candidate)
                
            
                BFS(temp_totalMoves, value, temp_MoveStrings, temp_board.move, temp_piece)
                
                if(bool == True):
                    DFS(temp_totalMoves, depth, value, temp_MoveStrings, temp_board.move, temp_piece)
                    depth = depth + 1
                    self.eval(temp_board, "black")
            
        # alpha beta pruning
    
        # #(black)
        # if (candidate != None and value < candidate and depth % 2 == 0):
        #     pass
        
        # #(white)
        # if (candidate != None and value > candidate and depth % 2 != 0):
        #     pass
        # # alpha beta pruning
    
        # #(black)
        # if (candidate != None and value < candidate and depth % 2 == 0):
        #     pass
        
        # #(white)
        # if (candidate != None and value > candidate and depth % 2 != 0):
        #     pass
                
    def getmoves(self, board, pieceColor):
        self.FreshMoves.clear()
        self.FreshMoveStrings.clear()
        print("")
        print("Available Moves: ")
        for row in range(Ranks):
            for col in range(Files):
                if(board.squares[row][col].has_piece()):
                    if(board.squares[row][col].piece.color == pieceColor):
                        board.calc_moves(board.squares[row][col].piece, row, col, bool=True)
                        if(board.squares[row][col].piece.moves != []):
                            self.FreshPiece.append(board.squares[row][col].piece)
                            self.FreshMoves.append(board.squares[row][col].piece.moves)
                            self.FreshMoveStrings.append(board.squares[row][col].piece.moveString)
                            
                            print(board.squares[row][col].piece.moveString)
                            
                            board.squares[row][col].piece.moves.clear()
                            board.squares[row][col].piece.moveString.clear()
                        