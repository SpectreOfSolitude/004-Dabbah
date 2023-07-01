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
        self.maxDepth = 3
        self.tree = None
        self.BFSdepth = 1
        
    def getBestMove(self):
        return self.engine(None, 1)

    
    def eval(self, board, color):
        
        self.getmoves(board, color)
        # print(self.FreshMoveStrings)
       # print("")
        # Reset First
        self.scoreMaterial = 0
        
        for row in range(Ranks):
            for col in range(Files):
                if(board.squares[row][col].has_piece()):
                    self.scoreMaterial = self.scoreMaterial + board.squares[row][col].piece.value
                    #print(board.squares[row][col].piece.value)
       # print("")
        #print(f"Current Position Evaluation: {self.scoreMaterial}")
        
        return self.scoreMaterial
    
    def minimax(self, SourceBoard, color, newDepth):
        # Tree Making Searching Algorithms
        #print("THIS IS MINIMAX")
        def BFS(nextMoves, value, MoveNames, NewBoard, NewPiece, color, depth):
            #print("GOING FOR BFS")
            print(depth)
            print(self.BFSdepth)
            while (self.BFSdepth <= depth):
                print("got in")
                while (nextMoves != []):
                    if(MoveNames not in self.exploredBoards):
                        value = eval(NewBoard, color)
                        self.exploredBoards.append(MoveNames)
                        self.tree.add_child(value, MoveNames)
                        #elif(value < self.scoreMaterial and color == 'white'):
                        #    self.tree.add_child(value, MoveNames)
                        self.NumberOfBoards =+ 1
                        NewBoard.move(NewPiece, nextMoves)

                    nextMoves.pop()
                    MoveNames.pop()
                self.BFSdepth = self.BFSdepth + 1
            depth = depth+1
            if (color == 'white'):
                NewColor = 'black'
            else:
                NewColor = 'white'
            if(depth > self.maxDepth):
                size=len(self.tree.children)
                print(size)
                self.minimax(NewBoard, NewColor,newDepth)

                    
        def DFS(nextMoves, depth, value, MoveNames, NewBoard, NewPiece, color):
            while (depth != self.maxDepth):
                print("GOING FOR DFS")
                if(MoveNames not in self.exploredBoards):
                    value = eval(NewBoard, color)
                    self.exploredBoards.append(MoveNames)
                    if (self.scoreMaterial > value and color == 'black'):
                        self.tree.add_child(value, MoveNames)
                    elif(value < self.scoreMaterial and color == 'white'):
                        self.tree.add_child(value, MoveNames)
                    self.NumberOfBoards =+ 1
                    NewBoard.move(NewPiece, nextMoves) 
                
                depth = depth + 1
                newdepth = newdepth + 1
                if (color == 'white'):
                    NewColor = 'black'
                else:
                    NewColor = 'white'
                self.minimax(NewBoard, NewColor, newdepth)
                
            nextMoves.pop()
            MoveNames.pop()

        # Root Node
        if (newDepth == 0):

            print("THIS IS ROOT")
            init_value = self.eval(SourceBoard, color)
            self.tree = Node(init_value, "Current Pos.") # Rooting
            temp_board = copy.deepcopy(SourceBoard) 
            temp_totalMoves = copy.deepcopy(self.FreshMoves)
            temp_MoveStrings = copy.deepcopy(self.FreshMoveStrings)
            temp_piece = copy.deepcopy(self.FreshPiece)
            #print("ttoal piece")
            #print(temp_totalMoves)
            #print("temp piece")
            #print(temp_piece)
            
            # self.eval(temp_board, color)
            # temp_board.move(temp_piece[0], temp_piece[0].moves)
            
            newDepth = newDepth + 1
            if (color == 'white'):
                ColorSwap = 'black'
            else:
                ColorSwap = 'white'
                
            self.minimax(temp_board, ColorSwap,newDepth)
           
        # Not root node     
        else:                
            value = self.eval(SourceBoard, color)
          #  print("NOT GOING FOR ROOT")
            # minimizing (black)
            if(color == 'black'):
                temp_totalMoves = copy.deepcopy(self.FreshMoves)
                temp_MoveStrings = copy.deepcopy(self.FreshMoveStrings)
                temp_piece = copy.deepcopy(self.FreshPiece)
                temp_board = copy.deepcopy(SourceBoard)
                
                BFS(temp_totalMoves, value, temp_MoveStrings, temp_board, temp_piece, "white", newDepth)
                # multiprocessing(BFS(temp_totalMoves, value, temp_MoveStrings, temp_board.move, temp_piece), 
                # DFS(temp_totalMoves, depth, value, temp_MoveStrings, temp_board.move, temp_piece))
                DFS(temp_totalMoves, self.depth, value, temp_MoveStrings, temp_board, temp_piece, "white")

                #depth = depth + 1
                #self.minimax(temp_board, "white")
        
            # maximizing (white)
            elif( color == 'white'):
                temp_totalMoves = copy.deepcopy(self.FreshMoves)
                temp_MoveStrings = copy.deepcopy(self.FreshMoveStrings)
                temp_piece = copy.deepcopy(self.FreshPiece)
                temp_board = copy.deepcopy(SourceBoard)
            
                BFS(temp_totalMoves, value, temp_MoveStrings, temp_board, temp_piece, "black", newDepth)
                
                DFS(temp_totalMoves, self.depth, value, temp_MoveStrings, temp_board, temp_piece, "black")
                self.depth = self.depth + 1
                #depth = depth + 1
                #self.minimax(temp_board, "black")
            
        if(newDepth >5):
            print("DONE.")
            print(f'total Board explored: {self.exploredBoards.len()}')
            print(self.tree.children.len())
            
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
        #print("")
        #print("Available Moves: ")
        for row in range(Ranks):
            for col in range(Files):
                if(board.squares[row][col].has_piece()):
                    if(board.squares[row][col].piece.color == pieceColor):
                        board.calc_moves(board.squares[row][col].piece, row, col, bool=True)
                        #if(board.squares[row][col].piece.moves != []):
                        self.FreshPiece.append(board.squares[row][col].piece)
                        self.FreshMoves.append(board.squares[row][col].piece.moves)
                        self.FreshMoveStrings.append(board.squares[row][col].piece.moveString)
                        #print(board.squares[row][col].piece.moveString)
                        
                        board.squares[row][col].piece.moves.clear()
                        board.squares[row][col].piece.moveString.clear()
    
        # print(self.FreshMoves)
        # print(self.FreshPiece)
        # print(self.FreshMoveStrings)
                        