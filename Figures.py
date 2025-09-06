class Figure:
    def __init__(self, color: str, position: tuple):
        self.color = color
        self.position = position

class Pawn(Figure):
    def __init__(self, color: str, position: tuple):
        super().__init__(color, position)
        self.symbol = 'P' if color == 'white' else 'p'

class Knight(Figure):
    def __init__(self, color: str, position: tuple):
        super().__init__(color, position)
        self.symbol = 'N' if color == 'white' else 'n'

class Bishop(Figure):
    def __init__(self, color: str, position: tuple):
        super().__init__(color, position)
        self.symbol = 'B' if color == 'white' else 'b'

class Rook(Figure):
    def __init__(self, color: str, position: tuple):
        super().__init__(color, position)
        self.symbol = 'R' if color == 'white' else 'r'

class Queen(Figure):
    def __init__(self, color: str, position: tuple):
        super().__init__(color, position)
        self.symbol = 'Q' if color == 'white' else 'q'

class King(Figure):
    def __init__(self, color: str, position: tuple):
        super().__init__(color, position)
        self.symbol = 'K' if color == 'white' else 'k'