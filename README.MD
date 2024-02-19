# Tic Tac Toe Game in Pygame
![image](https://github.com/oscarNCC/Tic-Tac-Toe-Game-w-Minimax-algorithm/blob/main/Screenshot.png)---
This project is a simple implementation of the classic game Tic Tac Toe using Pygame. The game allows for a single player to play against an AI, which makes its moves based on the minimax algorithm with alpha-beta pruning for optimization. The GUI is created using Pygame, providing a visual interface for the game board and handling user interactions through mouse clicks.

## Features

- Single player gameplay against an AI opponent.
- Graphical user interface to display the game board and results.
- AI uses minimax algorithm with alpha-beta pruning to determine its moves.

## Requirements

- Python 3.x
- Pygame library

## Installation

1. Ensure Python 3.x is installed on your system.
2. Install Pygame by running `pip install pygame` in your terminal or command prompt.
3. Clone or download this repository to your local machine.
4. Run the script to start the game: `python tic_tac_toe.py`

## How to Play

- Run the script to start the game.
- Click on a square to place your 'X'.
- The AI will make its move, placing an 'O'.
- The first player to align three of their marks vertically, horizontally, or diagonally wins.
- If all squares are filled and no player has won, the game ends in a draw.
- Click the "Restart" button to start a new game after a game is completed.

## Code Overview

### Setup

- Initializes the Pygame library and sets up the game window.
- Defines the size of the game board, colors, and other constants used in the game.

### Game Functions

- `draw_lines()`: Draws the Tic Tac Toe grid.
- `draw_figures()`: Draws the 'X's and 'O's on the board.
- `mark_square()`: Marks a square on the board with the player's symbol.
- `check_winner()`: Checks if there is a winner.
- `available_square()`: Checks if a square is available to be marked.
- `is_board_full()`: Checks if the board is full.
- `display_winner()`: Displays the game result (winner or draw).
- `draw_restart_button()`: Draws the restart button on the screen.
- `minimax()`: Implements the minimax algorithm with alpha-beta pruning to find the best move.
- `best_move()`: Determines the best move for the AI.

### Game Loop

- Handles game events, such as quitting the game, mouse clicks for player moves, and AI moves.
- Updates the game state and displays the current state of the game board.
- Checks for game over conditions and displays the result.
- Allows restarting the game after it's finished.

## Closing

To exit the game, simply close the game window or press the quit button.

Enjoy playing Tic Tac Toe!
