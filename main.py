from src.logging import logger
from src.exception.exception import ProjectException
import sys
import random

from src.components.MDP import State
from src.components.game_rules import *
from src.components.value_iteration import ValueIterationSolver
from src.utils.utils import initialize_symbols, ai_symbol


def generate_states():
    """Generate all reachable states through BFS algorithm"""
    seen = set()
    queue = [State((None,)*9, 'X')]
    
    while queue:
        current = queue.pop(0)
        if current in seen:
            continue
        seen.add(current)
        
        if is_terminal(current):
            continue
            
        for a in get_actions(current):
            next_state = apply_action(current, a)
            queue.append(next_state)
            
    return seen

def print_state(state):
    symbols = {None: '-', 'X': 'X', 'O': 'O'}
    board = [symbols[c] for c in state.board]
    print(f"Current board:")
    
    for i in range(0, 9, 3):
        print(' '.join(board[i:i+3]))
    print()

def get_user_move(state):
    while True:
        try:
            move = int(input("Enter your move (1-9): ")) - 1
            
            if move in get_actions(state):
                return move
            else:
                print("Invalid move. Try again.")
        
        except ValueError as e:
            raise ProjectException(e,sys)
            print("Invalid input. Please enter a number:")

# def get_ai_move(state, solver):
#     best_value = float('-inf') if state.player == 'X' else float('inf')
#     best_actions = []
    
#     for action in get_actions(state):
#         next_state = apply_action(state, action)
#         value = solver.values[next_state]
        
#         if state.player == 'X':
#             if value > best_value:
#                 best_value = value
#                 best_actions = [action]
#             elif value == best_value:
#                 best_actions.append(action)
#         else:  # 'O' player
#             if value < best_value:
#                 best_value = value
#                 best_actions = [action]
#             elif value == best_value:
#                 best_actions.append(action)
    
#     return random.choice(best_actions)  

def get_ai_move(state, solver):
    best_value = float('-inf') if state.player == 'X' else float('inf')
    best_action = None

    for action in get_actions(state):
        next_state = apply_action(state, action)
        value = solver.values[next_state]

        if state.player == 'X' and value > best_value:
            best_value = value
            best_action = action
        elif state.player == 'O' and value < best_value:
            best_value = value
            best_action = action

    return best_action

if __name__ == "__main__":
    states = generate_states()
    solver = ValueIterationSolver()
    solver.solve(states)
    solver.derive_policy(states)
    user_symbol, ai_symbol = initialize_symbols()
    
    # Initializing the game with 'X' since X starts the game
    current_state = State((None,)*9, 'X')
    
    while not is_terminal(current_state):
        print_state(current_state)
        
        if current_state.player == ai_symbol:
            action = get_ai_move(current_state, solver)
            print(f"AI places {ai_symbol} at position {action+1}")
        else:
            action = get_user_move(current_state)
            print(f"You place {user_symbol} at position {action+1}")
        
        current_state = apply_action(current_state, action)
    
    print("Final state:")
    print_state(current_state)
    result = get_reward(current_state)
    
    if result == 0:
        print("It's a draw!")
    elif (result == 1 and user_symbol == 'X') or (result == -1 and user_symbol == 'O'):
        print("AI wins!")
    else:
        print("You win!")