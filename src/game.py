import pygame
from const import *
from board import Board
from dragger import Dragger
from ai import AI

class Game:
    
    def __init__(self):
        self.next_player = "white"
        self.board = Board()
        self.dragger = Dragger()
        self.AI = AI(self)
    
    #Show Methods
    
    def show_bg(self, surface):
        borders = (0,0,0)
        color = (204, 153, 102)
        for file in range(Files):
            for rank in range(Ranks):
                # if (rank + file) % 2 == 0:
                #     color = (234, 235, 200) # Light Green
                # else:
                #     color = (119,154,88) # Dark Green
                    
                SegiEmpat = (file*SquareSize, rank*SquareSize, SquareSize, SquareSize)
                
                pygame.draw.rect(surface, color, SegiEmpat)
                                
    def show_pieces(self, surface):
        for row in range(Files):
            for col in range(Ranks):
                # piece ?
                if self.board.squares[row][col].has_piece():
                    piece = self.board.squares[row][col].piece
                    
                    
                    # all pieces except dragged piece
                    if piece is not self.dragger.piece:
                        img = pygame.image.load(piece.texture)
                        img_center = col*SquareSize+SquareSize //2, row*SquareSize+SquareSize//2
                        piece.texture_rect = img.get_rect(center=img_center)
                        surface.blit(img, piece.texture_rect)

    def show_moves(self, surface):
        if self.dragger.dragging:
            piece = self.dragger.piece
            
            #loop all valid moves
            for move in piece.moves:
                # color
                color = '#C86464' if(move.final.row + move.final.col) % 2 == 0 else '#C86464'
                # rect
                rect = (move.final.col * SquareSize, move.final.row * SquareSize, SquareSize, SquareSize)
                # blit
                pygame.draw.rect(surface, color, rect)
                
    def show_borders(self, surface):
        borders = (0,0,0)

        for file in range(Files):
            for rank in range(Ranks):
                pygame.draw.line(surface,borders,(((file)*SquareSize, (rank)*SquareSize)), ((file)*SquareSize, (rank+1)*SquareSize), 3)
                pygame.draw.line(surface,borders,(((file)*SquareSize, (rank)*SquareSize)), ((file+1)*SquareSize, (rank)*SquareSize), 3)
                if(file >0):
                    if(rank >0):
                        if(file%3 == 0):
                            if(rank%3 == 0):
                                pygame.draw.circle(surface, borders, ((file*SquareSize), (rank*SquareSize)),7)
    
    # other methods
    
    def show_last_move(self, surface):
        if self.board.last_move:
            initial = self.board.last_move.initial
            final = self.board.last_move.final
            
            for pos in [initial, final]:
                # color
                color = (244, 247, 116) if (pos.row + pos.col) % 2 == 0 else (172, 195, 51)
                # rect
                rect = (pos.col * SquareSize, pos.row *SquareSize, SquareSize, SquareSize)
                # blit
                pygame.draw.rect(surface, color, rect)
    
    def next_turn(self):
        self.next_player = "white" if self.next_player == "black" else "black"