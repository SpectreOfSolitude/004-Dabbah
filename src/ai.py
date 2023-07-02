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
        self.DFSdepth = 1
        
    def getBestMove(self):
        return self.engine(None, 1)

    
    def eval(self, board, color):
        
        Pieces = self.getmoves(board, color)
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
        def BFS(value, MoveNames, NewBoard, color, depth):
            #print("GOING FOR BFS")
            NewPiece = self.getmoves(NewBoard, color)
            print(depth)
            self.BFSdepth = depth
            while (self.BFSdepth <= self.maxDepth):
                i= 0
                while (i< len(MoveNames)):
                    while (MoveNames != []):
                        print(i)
                        if(MoveNames[0] not in self.exploredBoards):
                            value = self.eval(NewBoard, color)
                            self.exploredBoards.append(MoveNames[0])
                            self.tree.add_child(value, MoveNames[0])
                            #elif(value < self.scoreMaterial and color == 'white'):
                            #    self.tree.add_child(value, MoveNames)
                            self.NumberOfBoards =+ 1
                            
                            if (NewPiece[i].moves !=[]):
                                print(f"All movenames left:{MoveNames}")
                                NewPiece[i].moves.pop(0)
                                MoveNames.pop(0)
                            print("Aman")
                            print(f"Explored Boards:{self.exploredBoards}")
                        i= i+1
                    else:
                        i=i+1
                    
                self.BFSdepth = self.BFSdepth + 1
                # print(self.BFSdepth)
                # print("Mau masuk minimax lagi")
            
                # depth = depth+1
                
                # if (color == 'white'):
                #     NewColor = 'black'
                # else:
                #     NewColor = 'white'
                # # if(depth < self.maxDepth):
                # #     print("masuk")
                # #     NewBoard.move(NewPiece[0], NewPiece[0].moves[0]) 
                # #     self.minimax(NewBoard, NewColor,depth)

                    
        def DFS(depth, value, MoveNames, NewBoard, color):
            print("GOING FOR DFS")
            NewPiece = self.getmoves(NewBoard, color)
            print(depth)
            self.DFSdepth = depth
            while (self.DFSdepth <= self.maxDepth):
                i= 0
                while (i< len(MoveNames)):
                    while (MoveNames != []):
                        print(i)
                        if(MoveNames[0] not in self.exploredBoards):
                            value = self.eval(NewBoard, color)
                            self.exploredBoards.append(MoveNames[0])
                            self.tree.add_child(value, MoveNames[0])
                            #elif(value < self.scoreMaterial and color == 'white'):
                            #    self.tree.add_child(value, MoveNames)
                            self.NumberOfBoards =+ 1
                            
                            if (NewPiece[i].moves !=[]):
                                print(f"All movenames left:{MoveNames}")
                                NewPiece[i].moves.pop(0)
                                MoveNames.pop(0)
                            print("Aman")
                            print(f"Explored Boards:{self.exploredBoards}")
                        i= i+1
                    else:
                        i=i+1
            
            # def DFS(depth, value, MoveNames, NewBoard, color):
            # NewPiece = self.getmoves(NewBoard, color)
            # while (depth != self.maxDepth):
            #     print("GOING FOR DFS")
            #     if(MoveNames not in self.exploredBoards):
            #         value = self.eval(NewBoard, color)
            #         self.exploredBoards.append(MoveNames)
            #         self.tree.add_child(value, MoveNames)
            #         self.NumberOfBoards =+ 1
            #         NewBoard.move(NewPiece[0], NewPiece[0].moves[0]) 
            #         self.minimax(NewBoard, NewColor, newdepth)
                
            #     depth = depth + 1
            #     newdepth = newdepth + 1
            #     if (color == 'white'):
            #         NewColor = 'black'
            #     else:
            #         NewColor = 'white'
                
            # NewPiece[0].moves.pop()
            # MoveNames.pop()

        # Root Node
        if (newDepth == 0):
            print("THIS IS ROOT")
            init_value = self.eval(SourceBoard, color)
            self.tree = Node(init_value, "Current Pos.") # Rooting
            temp_board = copy.deepcopy(SourceBoard) 
            temp_MoveStrings = copy.deepcopy(self.FreshMoveStrings)
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
            
            # minimizing (black)
            if(color == 'black'):
                temp_MoveStrings = copy.deepcopy(self.FreshMoveStrings)
                temp_board = copy.deepcopy(SourceBoard)
                
                BFS(value, temp_MoveStrings, temp_board, "white", newDepth)
                # multiprocessing(BFS(temp_totalMoves, value, temp_MoveStrings, temp_board.move, temp_piece), 
                # DFS(temp_totalMoves, depth, value, temp_MoveStrings, temp_board.move, temp_piece))
                DFS(self.depth, value, temp_MoveStrings, temp_board, "white")

                #depth = depth + 1
                #self.minimax(temp_board, "white")
        
            # maximizing (white)
            elif( color == 'white'):
                temp_MoveStrings = copy.deepcopy(self.FreshMoveStrings)
                temp_board = copy.deepcopy(SourceBoard)
            
                BFS(value, temp_MoveStrings, temp_board , "black", newDepth)
                
                DFS(self.depth, value, temp_MoveStrings, temp_board, "black")
                self.depth = self.depth + 1
                #depth = depth + 1
                #self.minimax(temp_board, "black")
            
        if(newDepth >5):
            print("DONE.")
            print(f'total Board explored: {self.exploredBoards.len()}')
            print(self.tree.children.len())
            

                
    def getmoves(self, board, pieceColor):
        self.FreshMoveStrings.clear()
        #print("")
        #print("Available Moves: ")
        for row in range(Ranks):
            for col in range(Files):
                if(board.squares[row][col].has_piece()):
                    if(board.squares[row][col].piece.color == pieceColor):
                        board.calc_moves(board.squares[row][col].piece, row, col, bool=True)
                        if(board.squares[row][col].piece.moves != []):
                            self.FreshPiece.append(board.squares[row][col].piece)
                            self.FreshMoveStrings.append(board.squares[row][col].piece.moveString)
                        #print(board.squares[row][col].piece.moveString)
        return self.FreshPiece
        # print(self.FreshMoves)
        # print(self.FreshPiece)
        # print(self.FreshMoveStrings)
                        