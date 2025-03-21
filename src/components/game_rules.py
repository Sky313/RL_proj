from src.components.MDP import State
from src.utils.utils import ai_symbol


def get_reward(state):
    """Calculate immediate reward for terminal (final) states"""
    board = state.board
    
    """Possible winning configurations within TicTacToe board and the numbers represent the indices of the board
    For example:0 | 1 | 2
                3 | 4 | 5
                6 | 7 | 8 """
    lines = [(0,1,2), (3,4,5), (6,7,8), 
            (0,3,6), (1,4,7), (2,5,8),
            (0,4,8), (2,4,6)]
    for line in lines:
        a, b, c = line
        if board[a] and board[a] == board[b] == board[c]:
            return 1 if board[a] == ai_symbol else -1
    return 0

def is_terminal(state):
    """ To check if the game has ended or not"""
    if None not in state.board:
        return True
    return get_reward(state) != 0

def get_actions(state):
    """Valid moves for the current player"""
    return [i for i, cell in enumerate(state.board) if cell is None]

def apply_action(state, action):
    """To generate next state"""
    new_board = list(state.board)
    new_board[action] = state.player
    next_player = 'O' if state.player == 'X' else 'X'
    return State(tuple(new_board), next_player)