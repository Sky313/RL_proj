class State:
    def __init__(self, board, player):
        self.board = tuple(board)
        self.player = player
        
    def __hash__(self):
        """Creates a unique hash based upon the board configuration"""
        return hash((self.board, self.player))
    
    def __eq__(self, other):
        return self.board == other.board and self.player == other.player
    
    def __repr__(self):
        """For string representation of board and player"""
        return f"State({self.board}, {self.player})"