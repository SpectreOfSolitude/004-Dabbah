import pygame
import sys
import time

from const import *
from game import Game
from dragger import Dragger
from square import Square
from move import Move

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
        self.ai = self.game.AI
        
        while True:
            # HumanTurn = (GameState.whiteToMove and playerWhite) or (not gs.whiteToMove and playerBlack)
            
            game.show_bg(screen)
            game.show_moves(screen)
            game.show_last_move(screen)
            game.show_borders(screen)
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
                            # valid piece (color)?
                            if piece.color == game.next_player:
                                board.calc_moves(piece, clicked_row, clicked_col, bool=True)
                                dragger.save_initial(event.pos)
                                dragger.drag_piece(piece)
                                #show methods
                                game.show_bg(screen)
                                game.show_moves(screen)
                                game.show_borders(screen)
                                game.show_pieces(screen)
                
                # mouse motion
                elif event.type == pygame.MOUSEMOTION:
                    if dragger.dragging:
                        dragger.update_mouse(event.pos)
                        #show methods
                        game.show_bg(screen)
                        game.show_moves(screen)
                        game.show_borders(screen)
                        game.show_pieces(screen)
                        dragger.update_blit(screen)
                
                # click lepas
                elif event.type == pygame.MOUSEBUTTONUP:
                    
                    if dragger.dragging:
                        dragger.update_mouse(event.pos)
                        
                        released_row = dragger.mouseY // SquareSize
                        released_col = dragger.mouseX // SquareSize
                        
                        # create possible move
                        initial = Square(dragger.initial_row, dragger.initial_col)
                        final = Square(released_row, released_col)
                        move = Move(initial, final)
                        
                        # valid move ?
                        if board.valid_move(dragger.piece, move):
                            print("valid.")
                            #print(move)
                            board.move(dragger.piece, move)
                            # show methods
                            game.show_bg(screen)
                            game.show_last_move(screen)
                            game.show_borders(screen)
                            game.show_pieces(screen)
                            # next turn
                            game.next_turn()
                            
                            t1_start = time.perf_counter()
                            game.AI.minimax(board, game.next_player, 0)
                            t1_stop = time.perf_counter()
                            print(f"Time Taken: {t1_stop-t1_start} ")
                            
                        else:
                            print("invalid!")
                            print(move)
                            print(dragger.piece)
                    
                    dragger.undrag_piece()
                
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                    
            pygame.display.update()
    
main = Main()
main.mainloop()