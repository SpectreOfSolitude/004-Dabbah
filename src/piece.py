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
        self.moveString = []
        self.moved = False
        self.texture = texture
        self.set_texture()
        self.texture_rect = texture_rect
    
    def set_texture(self, size = 80):
        self.texture = os.path.join(f'assets/{self.color}_{self.name}.png')
        
    def add_moves(self, move):
        if (move.final.col == 0):
            PieceFile = "A"
        elif (move.final.col == 1):
            PieceFile = "B"
        elif (move.final.col == 2):
            PieceFile = "C"
        elif (move.final.col == 3):
            PieceFile = "D"
        elif (move.final.col == 4):
            PieceFile = "E"
        elif (move.final.col == 5):
            PieceFile = "F"
        elif (move.final.col == 6):
            PieceFile = "G"
        elif (move.final.col == 7):
            PieceFile = "H"
        elif (move.final.col == 8):
            PieceFile = "I"
            
        if (move.final.row == 0):
            PieceRank = "9"
        elif (move.final.row == 1):
            PieceRank = "8"
        elif (move.final.row == 2):
            PieceRank = "7"
        elif (move.final.row == 3):
            PieceRank = "6"
        elif (move.final.row == 4):
            PieceRank = "5"
        elif (move.final.row == 5):
            PieceRank = "4"
        elif (move.final.row == 6):
            PieceRank = "3"
        elif (move.final.row == 7):
            PieceRank = "2"
        elif (move.final.row == 8):
            PieceRank = "1"
                
        self.moves.append(move)
        str = ''
        str += f'{self.name}'
        str += f" -> ({PieceFile}{PieceRank})"
        self.moveString.append(str)
        
    def clear_moves(self):
        self.moves = []
        self.moveString = []

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
        super().__init__("king", color, 10000.00)