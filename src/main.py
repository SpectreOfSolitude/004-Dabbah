import pygame
import sys

from const import *
from game import Game
from dragger import Dragger

class Main:
    
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((Width, Height))
        pygame.display.set_caption("Chess Beast")
        self.game = Game()
    
    def mainloop(self):
        
        screen = self.screen
        game = self.game
        dragger = self.game.dragger
        board = self.game.board
        
        while True:
            game.show_bg(screen)
            game.show_pieces(screen)
            
            for event in pygame.event.get():
                
                #click pencet
                if event.type == pygame.MOUSEBUTTONDOWN:
                    dragger.update_mouse(event.pos)
                    
                    clicked_row = dragger.mouseX // SquareSize
                    clicked_col = dragger.mouseY // SquareSize
                    
                    if board.squares[clicked_row][clicked_col].has_piece():
                        pass
                
                # dragger
                elif event.type == pygame.MOUSEMOTION:
                    pass 
                
                # click lepas
                elif event.type == pygame.MOUSEBUTTONUP:
                    pass
                
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                    
                    
                    
            pygame.display.update()
    
main = Main()
main.mainloop()