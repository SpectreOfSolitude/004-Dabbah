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
        
        playerWhite = True # False kalau AI yang main putih
        playerBlack = False
        screen = self.screen
        gameOver = False
        game = self.game
        dragger = self.game.dragger
        board = self.game.board
        
        while True:
            # HumanTurn = (GameState.whiteToMove and playerWhite) or (not gs.whiteToMove and playerBlack)
            
            game.show_bg(screen)
            game.show_moves(screen)
            game.show_pieces(screen)
            
            if dragger.dragging:
                dragger.update_blit(screen)
            
            for event in pygame.event.get():
                
                #click pencet
                if event.type == pygame.MOUSEBUTTONDOWN:
                    #if not gameOver and HumanTurn:
                        dragger.update_mouse(event.pos)
                        
                        clicked_row = dragger.mouseY // SquareSize
                        clicked_col = dragger.mouseX // SquareSize
                        
                        # clicked square has a piece?
                        if board.squares[clicked_row][clicked_col].has_piece():
                            piece = board.squares[clicked_row][clicked_col].piece
                            board.calc_moves(piece, clicked_row, clicked_col)
                            dragger.save_initial(event.pos)
                            dragger.drag_piece(piece)
                            #show methods
                            game.show_bg(screen)
                            game.show_moves(screen)
                            game.show_pieces(screen)
                
                # mouse motion
                elif event.type == pygame.MOUSEMOTION:
                    if dragger.dragging:
                        dragger.update_mouse(event.pos)
                        #show methods
                        game.show_bg(screen)
                        game.show_moves(screen)
                        game.show_pieces(screen)
                        dragger.update_blit(screen)
                
                # click lepas
                elif event.type == pygame.MOUSEBUTTONUP:
                    dragger.undrag_piece()
                
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                    
                    
                    
            pygame.display.update()
    
main = Main()
main.mainloop()