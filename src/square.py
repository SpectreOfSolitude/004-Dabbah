
class Square:
    
    def __init__(self, horizontal, vertical, piece = None):
        self.horizontal = horizontal
        self.vertical = vertical
        self.piece = piece
        
    def has_piece(self):
        return self.piece != None