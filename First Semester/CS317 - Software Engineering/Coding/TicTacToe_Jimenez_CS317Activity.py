# Pair Activity — Tic Tac Toe ( Jimenez and Dacapio )

# Initialize the board as a 3x3 grid
board = [' ' for _ in range (9)]

def print_board():
    "Display the current state of the board."
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("--+---+--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--+---+--")
    print(f"{board[6]} | {board[7]} | {board[8]}")
    print()

def check_win(symbol):
    "Check for a win condition."
    # Winning combinations (row, columns, diagonal)
    win_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],   # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],   # Column
        [0, 4, 8], [2, 4, 6]             # Diagonal
    ]
    return any(all(board[pos] == symbol for pos in combo) for combo in win_combinations)
    
def check_draw():
    "Check for a draw condition (no empty spaces left)."
    return ' ' not in board

def is_valid_move(position):
    "Check if the move is valid (within range and unoccupied)."
    return position in range(9) and board[position] == ' '

def play_game():
    "Main function to play the Tic-Tac-Toe game."
    current_player = 'X'           # X always starts
    game_over = False
    
    print("Welcome to Tic-Tac-Toe!")
    print_board()
    
    while not game_over:
        try:
            # Get the player's move
            position = int(input(f"Player {current_player}, choose your position (0 - 8): "))

            # Validate the move
            if is_valid_move(position):
                board[position] = current_player
                print_board()
               
                # Check for a win or draw
                if check_win(current_player):
                    print(f"Player {current_player} wins!")
                    game_over = True         
                elif check_draw():
                    print("It's a draw!")
                    game_over = True
                else:
                    # Switch players
                    current_player = 'O' if current_player == 'X' else 'X' 
            else:
                print("Invalid move, please try again.")

        except ValueError:
            print("Please enter a valid number between 0 and 8.")

#Run the Game
play_game()