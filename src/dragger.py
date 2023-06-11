import pygame
from const import *

class Dragger:
    
    def __init__ (self):
        self.piece = None
        self.dragging = False
        self.mouseX = 0
        self.mouseY = 0
        self.intiial_horizontal = 0
        self.initial_vertical = 0
        
        
        # blit method
    def update_blit(self, surface):
        self.piece.set_texture(size=80)
        texture = self.piece.texture
        
        img = pygame.image.load(texture)
        img_center = (self.mouseX, self.mouseY)
        self.piece.texture_rect = img.get_rect(center = img_center)
        
        # blit
        surface.blit(img, self.piece.texture_rect)

        
    def update_mouse(self, pos):
        self.mouseX, self.mouseY = pos
    
    def save_initial(self, pos):
        self.initial_horizontal = pos[1] // SquareSize
        self.initial_vertical = pos[0] //SquareSize
        
    def drag_piece(self, piece):
        self.piece = piece
        self.dragging = True
        
    def undrag_piece(self):
        self.piece = None
        self.dragging = False