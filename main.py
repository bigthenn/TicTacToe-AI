# Define the tic tac toe board
#Big was here
board = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]

# Define the possible winning combinations
win_combinations = [
    [(0, 0), (0, 1), (0, 2)],
    [(1, 0), (1, 1), (1, 2)],
    [(2, 0), (2, 1), (2, 2)],
    [(0, 0), (1, 0), (2, 0)],
    [(0, 1), (1, 1), (2, 1)],
    [(0, 2), (1, 2), (2, 2)],
    [(0, 0), (1, 1), (2, 2)],
    [(0, 2), (1, 1), (2, 0)]
]

# Define the player's marker
player_marker = "X"

# Define the computer's marker
computer_marker = "O"

# Define the current player
current_player = player_marker

# Define the game state
game_over = False

# Define the function to print the tic tac toe board
def print_board():
    print("\n".join(" ".join(row) for row in board))

# Define the function to check if a player has won
def check_win(marker):
    for combination in win_combinations:
        if all(board[x][y] == marker for x, y in combination):
            return True
    return False

# Define the function to make a move for the player
def player_move():
    # Prompt the user for their move
    row = input("Enter the row: ")
    column = input("Enter the column: ")

    # Validate the input
    if not (0 <= int(row) <= 2) or not (0 <= int(column) <= 2):
        print("Invalid move")
        return player_move()

    # Place the player's marker on the board
    if board[int(row)][int(column)] == " ":
        board[int(row)][int(column)] = player_marker
    else:
        print("Invalid move")
        return player_move
