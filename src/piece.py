# PIECE DI SINI DIADAPTASI MENJADI PIECE YANG ADA DI SHOGI

# == PIECE VALUES ==
# pawn = 1
# lance, knight = 3
# silver, gold = 5
# bishop = 8
# rook = 9
# promoted bishop = 12
# promoted rook = 13

import os

class Piece:
    
    def __init__(self, name, color, value, texture = None, texture_rect = None):
        self.name = name
        self.color = color
        value_sign = 1 if color == "white" else -1
        self.value = value * value_sign
        self.moves = []
        self.moved = False
        self.texture = texture
        self.set_texture()
        self.texture_rect = texture_rect
    
    def set_texture(self, size = 80):
        self.texture = os.path.join(f'assets/{self.color}_{self.name}.png')
        
    def add_moves(self, move):
        self.moves.append(move)
        
    def clear_moves(self):
        self.moves = []

class Pawn(Piece):
    def __init__(self, color):
        if color == 'white': # PERSPEKTIF PLAYER 1 KALAU DI CATUR
            self.dir = -1
        else:
            self.dir = 1
            
        super().__init__("pawn", color, 1.0)
        
class PromotedPawn(Piece):
    def __init__(self, color):            
        super().__init__("promoted_pawn", color, 4.20)
        
class Lance(Piece):
    def __init__(self, color):            
        super().__init__("lance", color, 4.30)
        
class PromotedLance(Piece):
    def __init__(self, color):            
        super().__init__("promoted_lance", color, 6.30)
        
class Knight(Piece):
    def __init__(self, color):            
        super().__init__("knight", color, 4.50)
        
class PromotedKnight(Piece):
    def __init__(self, color):            
        super().__init__("promoted_knight", color, 6.40)
        
class Silver(Piece):
    def __init__(self, color):            
        super().__init__("silver", color, 6.40)
        
class PromotedSilver(Piece):
    def __init__(self, color):            
        super().__init__("promoted_silver", color, 6.70)
        
class Gold(Piece):
    def __init__(self, color):            
        super().__init__("gold", color, 6.90)
        
class Bishop(Piece):
    def __init__(self, color):            
        super().__init__("bishop", color, 8.90)
        
class Rook(Piece):
    def __init__(self, color):            
        super().__init__("rook", color, 10.40)
        
class Dragon(Piece):
    def __init__(self, color):            
        super().__init__("dragon", color, 13.00)
        
class Horse(Piece):
    def __init__(self, color):            
        super().__init__("horse", color, 11.50)
        
class King(Piece):
    def __init__(self, color):            
        super().__init__("king", color, 1000000.00)