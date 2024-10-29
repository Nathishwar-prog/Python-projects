import random

COMPUTER = 1
HUMAN = 2

SIDE = 3  # Length of the board

# Computer will move with 'O' and human with 'X'
COMPUTERMOVE = 'O'
HUMANMOVE = 'X'

# Function to show the current board status
def show_board(board):
    print("\n")
    for row in board:
        print("\t\t\t", " | ".join(row))
        print("\t\t\t--------------")

# Function to show the instructions
def show_instructions():
    print("\t\t\t Tic-Tac-Toe\n")
    print("Choose a cell numbered from 1 to 9 as below and play\n")
    print("\t\t\t 1 | 2 | 3 ")
    print("\t\t\t--------------")
    print("\t\t\t 4 | 5 | 6 ")
    print("\t\t\t--------------")
    print("\t\t\t 7 | 8 | 9 \n")

# Function to initialize the game
def initialise():
    board = [[' ' for _ in range(SIDE)] for _ in range(SIDE)]
    moves = list(range(SIDE * SIDE))
    random.shuffle(moves)
    return board, moves

# Function to declare the winner of the game
def declare_winner(whose_turn):
    if whose_turn == COMPUTER:
        print("COMPUTER has won")
    else:
        print("HUMAN has won")

# Function that returns true if any row is crossed with the same player's move
def row_crossed(board):
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != ' ':
            return True
    return False

# Function that returns true if any column is crossed with the same player's move
def column_crossed(board):
    for col in range(SIDE):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != ' ':
            return True
    return False

# Function that returns true if any diagonal is crossed with the same player's move
def diagonal_crossed(board):
    if (board[0][0] == board[1][1] == board[2][2] and board[0][0] != ' ') or \
       (board[0][2] == board[1][1] == board[2][0] and board[0][2] != ' '):
        return True
    return False

# Function that returns true if the game is over
def game_over(board):
    return row_crossed(board) or column_crossed(board) or diagonal_crossed(board)

# Function to play Tic-Tac-Toe
def play_tic_tac_toe(whose_turn):
    board, moves = initialise()
    show_instructions()

    move_index = 0

    # Keep playing till the game is over or it is a draw
    while not game_over(board) and move_index < SIDE * SIDE:
        x = moves[move_index] // SIDE
        y = moves[move_index] % SIDE

        if whose_turn == COMPUTER:
            board[x][y] = COMPUTERMOVE
            print(f"COMPUTER has put a {COMPUTERMOVE} in cell {moves[move_index] + 1}")
        else:
            board[x][y] = HUMANMOVE
            print(f"HUMAN has put a {HUMANMOVE} in cell {moves[move_index] + 1}")

        show_board(board)
        move_index += 1
        whose_turn = HUMAN if whose_turn == COMPUTER else COMPUTER

    # If the game has drawn
    if not game_over(board) and move_index == SIDE * SIDE:
        print("It's a draw")
    else:
        # Toggle the user to declare the actual winner
        whose_turn = HUMAN if whose_turn == COMPUTER else COMPUTER
        declare_winner(whose_turn)

# Driver program
if __name__ == "__main__":
    # Let us play the game with COMPUTER starting first
    play_tic_tac_toe(COMPUTER)
