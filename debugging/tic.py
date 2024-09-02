#!/usr/bin/python3

def print_board(board):
    print("\n")
    for i, row in enumerate(board):
        print(" | ".join(row))
        if i < 2:
            print("-" * 9)
    print("\n")

def check_winner(board):
    # Check rows and columns
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != " " or \
           board[0][i] == board[1][i] == board[2][i] != " ":
            return True
    
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != " " or \
       board[0][2] == board[1][1] == board[2][0] != " ":
        return True
    
    return False

def is_board_full(board):
    return all(cell != " " for row in board for cell in row)

def get_valid_input(prompt, valid_range):
    while True:
        try:
            value = int(input(prompt))
            if value in valid_range:
                return value
            else:
                print(f"Invalid input. Please enter a number between {valid_range[0]} and {valid_range[-1]}.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def tic_tac_toe():
    board = [[" "]*3 for _ in range(3)]
    player = "X"
    
    while True:
        print_board(board)
        print(f"Player {player}'s turn")
        
        while True:
            row = get_valid_input("Enter row (1, 2, or 3): ", range(1, 4)) - 1
            col = get_valid_input("Enter column (1, 2, or 3): ", range(1, 4)) - 1
            
            if board[row][col] == " ":
                board[row][col] = player
                break
            else:
                print("That spot is already taken! Try again.")
        
        if check_winner(board):
            print_board(board)
            print(f"Player {player} wins!")
            break
        elif is_board_full(board):
            print_board(board)
            print("It's a tie!")
            break
        
        player = "O" if player == "X" else "X"

if __name__ == "__main__":
    tic_tac_toe()
