import random

# Define the board as a list of 9 spaces
board = [' ' for _ in range(9)]

# Function to display the board
def display_board():
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("--+---+--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--+---+--")
    print(f"{board[6]} | {board[7]} | {board[8]}")
    print()

# Function to reset the board
def reset_board():
    global board
    board = [' ' for _ in range(9)]

# Function to check if a player has won
def check_winner(player):
    win_conditions = [
        [0, 1, 2],  # Horizontal
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],  # Vertical
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],  # Diagonal
        [2, 4, 6]
    ]
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] == player:
            return True
    return False

# Function to check if the board is full (for detecting a draw)
def is_board_full():
    return ' ' not in board

# Function for player's move
def player_move(player):
    while True:
        try:
            position = int(input(f"Player {player}, enter your move (1-9): ")) - 1
            if 0 <= position < 9 and board[position] == ' ':
                board[position] = player
                break
            else:
                print("Position already taken or invalid. Choose another.")
        except ValueError:
            print("Invalid input. Enter a number between 1 and 9.")

# Minimax algorithm for optimal move
def minimax(board, depth, is_maximizing):
    if check_winner('O'):
        return 10 - depth
    if check_winner('X'):
        return depth - 10
    if is_board_full():
        return 0

    if is_maximizing:
        best_score = -float('inf')
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O'
                score = minimax(board, depth + 1, False)
                board[i] = ' '
                best_score = max(best_score, score)
        return best_score
    else:
        best_score = float('inf')
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'X'
                score = minimax(board, depth + 1, True)
                board[i] = ' '
                best_score = min(best_score, score)
        return best_score

# Function for bot's move with adjustable difficulty
def bot_move(difficulty=0.7):
    """
    Bot makes a move. Difficulty is the probability of choosing the optimal move.
    """
    if random.random() < difficulty:
        # Optimal move using Minimax
        best_move = -1
        best_score = -float('inf')
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O'
                score = minimax(board, 0, False)
                board[i] = ' '
                if score > best_score:
                    best_score = score
                    best_move = i
        board[best_move] = 'O'
    else:
        # Random move
        available_moves = [i for i in range(9) if board[i] == ' ']
        bot_choice = random.choice(available_moves)
        board[bot_choice] = 'O'

# Main game function
def play_game():
    reset_board()
    current_player = 'X'

    # Ask for bot difficulty level
    while True:
        try:
            difficulty = float(input("Enter bot difficulty level (0.0 - 1.0, where 1.0 is hardest): "))
            if 0.0 <= difficulty <= 1.0:
                break
            else:
                print("Difficulty must be between 0.0 and 1.0.")
        except ValueError:
            print("Invalid input. Enter a decimal number between 0.0 and 1.0.")

    while True:
        display_board()

        if current_player == 'X':
            player_move(current_player)  # Human player move
        else:
            print("Bot is making its move...")
            bot_move(difficulty)

        if check_winner(current_player):
            display_board()
            if current_player == 'X':
                print("Player X wins!")
            else:
                print("Bot wins!")
            break
        elif is_board_full():
            display_board()
            print("It's a draw!")
            break

        # Switch player
        current_player = 'O' if current_player == 'X' else 'X'

# Run the game
if __name__ == "__main__":
    while True:
        play_game()
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing!")
            break
