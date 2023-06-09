import pygame
from const import *
from board import Board
from dragger import Dragger

class Game:
    
    def __init__(self):
        self.board = Board()
        self.dragger = Dragger()
    
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
                pygame.draw.line(surface,borders,(((file)*SquareSize, (rank)*SquareSize)), ((file)*SquareSize, (rank+1)*SquareSize), 3)
                pygame.draw.line(surface,borders,(((file)*SquareSize, (rank)*SquareSize)), ((file+1)*SquareSize, (rank)*SquareSize), 3)
                if(file >0):
                    if(rank >0):
                        if(file%3 == 0):
                            if(rank%3 == 0):
                                pygame.draw.circle(surface, borders, ((file*SquareSize), (rank*SquareSize)),7)
                                
    def show_pieces(self, surface):
        for row in range(Files):
            for col in range(Ranks):
                # piece ?
                if self.board.squares[row][col].has_piece():
                    piece = self.board.squares[row][col].piece
                    
                    img = pygame.image.load(piece.texture)
                    img_center = col*SquareSize+SquareSize //2, row*SquareSize+SquareSize//2
                    piece.texture_rect = img.get_rect(center=img_center)
                    surface.blit(img, piece.texture_rect)