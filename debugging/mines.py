#!/usr/bin/python3
import random
import os

def clear_screen():
    """Clear the console screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

class Minesweeper:
    def __init__(self, width=10, height=10, mines=10):
        """
        Initialize the Minesweeper game.
        
        :param width: Width of the game board (default: 10)
        :param height: Height of the game board (default: 10)
        :param mines: Number of mines to place on the board (default: 10)
        """
        self.width = width  # Width of the game board
        self.height = height  # Height of the game board
        # Create a set of mine positions
        self.mines = set(random.sample(range(width * height), mines))
        # Initialize the game field
        self.field = [[' ' for _ in range(width)] for _ in range(height)]
        # Keep track of revealed cells
        self.revealed = [[False for _ in range(width)] for _ in range(height)]

    def print_board(self, reveal=False):
        """
        Print the current state of the game board.
        
        :param reveal: If True, show all mines (used for game over) (default: False)
        """
        clear_screen()
        # Print column numbers
        print('  ' + ' '.join(str(i) for i in range(self.width)))
        for y in range(self.height):
            print(y, end=' ')  # Print row numbers
            for x in range(self.width):
                if reveal or self.revealed[y][x]:
                    if (y * self.width + x) in self.mines:
                        print('*', end=' ')  # Show mine
                    else:
                        count = self.count_mines_nearby(x, y)
                        print(count if count > 0 else ' ', end=' ')
                else:
                    print('.', end=' ')  # Unrevealed cell
            print()

    def count_mines_nearby(self, x, y):
        """
        Count the number of mines in the 8 cells surrounding (x, y).
        
        :param x: X-coordinate of the cell
        :param y: Y-coordinate of the cell
        :return: Number of mines in neighboring cells
        """
        count = 0
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < self.width and 0 <= ny < self.height:
                    if (ny * self.width + nx) in self.mines:
                        count += 1
        return count

    def reveal(self, x, y):
        """
        Reveal a cell and its neighbors if it's empty.
        
        :param x: X-coordinate of the cell to reveal
        :param y: Y-coordinate of the cell to reveal
        :return: False if the cell contains a mine, True otherwise
        """
        if (y * self.width + x) in self.mines:
            return False
        self.revealed[y][x] = True
        if self.count_mines_nearby(x, y) == 0:
            # If the cell is empty, reveal its neighbors
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < self.width and 0 <= ny < self.height and not self.revealed[ny][nx]:
                        self.reveal(nx, ny)
        return True

    def is_game_won(self):
        """
        Check if the game is won (all non-mine cells are revealed).
        
        :return: True if the game is won, False otherwise
        """
        for y in range(self.height):
            for x in range(self.width):
                if not self.revealed[y][x] and (y * self.width + x) not in self.mines:
                    return False
        return True

    def play(self):
        """Main game loop."""
        while True:
            self.print_board()
            try:
                # Get user input for the next move
                x = int(input("Enter x coordinate: "))
                y = int(input("Enter y coordinate: "))
                if not self.reveal(x, y):
                    # Game over if a mine is hit
                    self.print_board(reveal=True)
                    print("Game Over! You hit a mine.")
                    break
                if self.is_game_won():
                    # Win condition
                    self.print_board(reveal=True)
                    print("Congratulations! You've won the game.")
                    break
            except ValueError:
                # Handle invalid input
                print("Invalid input. Please enter numbers only.")

if __name__ == "__main__":
    # Create and start a new game when the script is run
    game = Minesweeper()
    game.play()
