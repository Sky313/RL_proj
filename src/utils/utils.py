def get_user_symbol():
    while True:
        choice = input("Do you want to play as X or O? ").upper()
        if choice in ['X', 'O']:
            return choice
        print("Invalid choice. Please enter X or O.")

def initialize_symbols():
    user_symbol = get_user_symbol()
    ai_symbol = 'O' if user_symbol == 'X' else 'X'
    return user_symbol, ai_symbol