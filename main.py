import pygame
import sys

pygame.init()
WIDTH, HEIGHT = 300, 300
LINE_WIDTH = 15
BOARD_ROWS, BOARD_COLS = 3, 3
SQUARE_SIZE = WIDTH // BOARD_COLS
CIRCLE_RADIUS = SQUARE_SIZE // 3
CIRCLE_WIDTH = 15
CROSS_WIDTH = 25
SPACE = SQUARE_SIZE // 4
# RGB Colors
BG_COLOR = (255, 255, 255)
LINE_COLOR = (0, 0, 0)
CIRCLE_COLOR = (255, 0, 0)
CROSS_COLOR = (0,0, 255)

# Screen setup
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Tic Tac Toe')
screen.fill(BG_COLOR)

# Board
board = [['.' for _ in range(BOARD_COLS)] for _ in range(BOARD_ROWS)]



def draw_lines():
    # Horizontal lines
    pygame.draw.line(screen, LINE_COLOR, (0, SQUARE_SIZE), (WIDTH, SQUARE_SIZE), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (0, 2 * SQUARE_SIZE), (WIDTH, 2 * SQUARE_SIZE), LINE_WIDTH)
    # Vertical lines
    pygame.draw.line(screen, LINE_COLOR, (SQUARE_SIZE, 0), (SQUARE_SIZE, HEIGHT), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (2 * SQUARE_SIZE, 0), (2 * SQUARE_SIZE, HEIGHT), LINE_WIDTH)

def draw_figures():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 'O':
                pygame.draw.circle(screen, CIRCLE_COLOR, (int(col * SQUARE_SIZE + SQUARE_SIZE // 2), int(row * SQUARE_SIZE + SQUARE_SIZE // 2)), CIRCLE_RADIUS, CIRCLE_WIDTH)
            elif board[row][col] == 'X':
                pygame.draw.line(screen, CROSS_COLOR, (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE), (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SPACE), CROSS_WIDTH)
                pygame.draw.line(screen, CROSS_COLOR, (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SPACE), (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE), CROSS_WIDTH)

def mark_square(row, col, player):
    board[row][col] = player
def check_winner(board):
    # Check rows, columns, and diagonals for a win
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != '.':
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != '.':
            return board[0][i]
    if board[0][0] == board[1][1] == board[2][2] != '.' or board[0][2] == board[1][1] == board[2][0] != '.':
        return board[1][1]
    return None

def available_square(row, col):
    return board[row][col] == '.'

def is_board_full():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == '.':
                return False
    return True

def display_winner(winner):
    font = pygame.font.Font(None, 40)
    # Determine the message based on the winner
    if winner == 'X':
        text = font.render('Human Wins!', True, (255, 255, 0))  # Human wins
    elif winner == 'O':
        text = font.render('AI Wins!', True, (255, 255, 0))  # AI wins
    else:
        text = font.render('Draw!', True, (255, 255, 0))  # It's a draw
    text_rect = text.get_rect(center=(WIDTH / 2, HEIGHT / 2))
    screen.fill(BG_COLOR)
    screen.blit(text, text_rect)
    pygame.display.flip()
    #pygame.time.wait(2000)  # Display the result for 2 seconds before showing the restart button




def draw_restart_button():
    font = pygame.font.Font(None, 30)
    text = font.render('Restart', True, (255, 255, 255))
    button_rect = pygame.Rect(WIDTH / 2 - 50, HEIGHT / 2 + 30, 100, 40)
    pygame.draw.rect(screen, (0, 0, 0), button_rect)
    text_rect = text.get_rect(center=button_rect.center)
    screen.blit(text, text_rect)
    pygame.display.flip()
    return button_rect  # Return the button's rectangle for click detection

#################################Core part of Homework#################################################
# This function implements the minimax algorithm with alpha-beta pruning to determine the best move for a given tic-tac-toe board state.
# Parameters:
# - board: A 2D list representing the current state of the tic-tac-toe board.
# - depth: The current depth of recursion. Starts at 0 and increases as we go deeper.
# - is_maximizing: A boolean indicating if the current function call aims to maximize or minimize the score.
# - alpha: The best value that the maximizer currently can guarantee at that level or above.
# - beta: The best value that the minimizer currently can guarantee at that level or above.
# Returns:
# - The best score that can be achieved from the current board state, given optimal play by both players.

def minimax(board, depth, is_maximizing, alpha, beta):
    winner = check_winner(board)  # Check if there's a winner or if the game is a draw.
    if winner or is_board_full():  # Base case: if the game is over (win or draw).
        if winner == 'X':
            return -10  # Score for X winning.
        elif winner == 'O':
            return 10   # Score for O winning.
        else:
            return 0   # Score for a draw.

    if is_maximizing:  # If it's the maximizing player's turn (O in this case).
        best_score = float('-inf')  # Initialize the best score to negative infinity.
        for row in range(BOARD_ROWS):
            for col in range(BOARD_COLS):
                if board[row][col] == '.':  # If the cell is empty.
                    board[row][col] = 'O'  # Make a move.
                    score = minimax(board, depth + 1, False, alpha, beta)  # Recurse to evaluate this move.
                    board[row][col] = '.'  # Undo the move.
                    best_score = max(score, best_score)  # Update the best score if necessary.
                    alpha = max(alpha, score)  # Update alpha.
                    if beta <= alpha:
                        break  # Alpha-beta pruning.
        return best_score
    else:  # If it's the minimizing player's turn (X in this case).
        best_score = float('inf')  # Initialize the best score to positive infinity.
        for row in range(BOARD_ROWS):
            for col in range(BOARD_COLS):
                if board[row][col] == '.':  # If the cell is empty.
                    board[row][col] = 'X'  # Make a move.
                    score = minimax(board, depth + 1, True, alpha, beta)  # Recurse to evaluate this move.
                    board[row][col] = '.'  # Undo the move.
                    best_score = min(score, best_score)  # Update the best score if necessary.
                    beta = min(beta, score)  # Update beta.
                    if beta <= alpha:
                        break  # Alpha-beta pruning.
        return best_score


def best_move():
    best_score = float('-inf')
    move = (-1, -1)
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == '.':
                board[row][col] = 'O'  
                score = minimax(board, 0, False, float('-inf'), float('inf'))
                board[row][col] = '.'  
                if score > best_score:
                    best_score = score
                    move = (row, col)
    return move





player = 'X' 
running = True
game_over = False
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        

        if event.type == pygame.MOUSEBUTTONDOWN and not game_over and player == 'X': 
            #mouse click
            mouseX = event.pos[0]  
            mouseY = event.pos[1]  

            clicked_row = int(mouseY // SQUARE_SIZE)
            clicked_col = int(mouseX // SQUARE_SIZE)

            if available_square(clicked_row, clicked_col):
                mark_square(clicked_row, clicked_col, player)
                if check_winner(board) or is_board_full():
                    game_over = True
                else:
                    player = 'O'
                draw_figures()

   
    if not game_over and player == 'O':
        row, col = best_move() 
        if row != -1 and col != -1:
            pygame.time.wait(500) 
            mark_square(row, col, 'O')
            if check_winner(board) or is_board_full():
                game_over = True
            else:
                player = 'X'  
            draw_figures()

    if game_over:
        display_winner(check_winner(board))
        restart_button = draw_restart_button()  
        waiting_for_restart = True
        while waiting_for_restart:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = event.pos
                    if restart_button.collidepoint(mouse_x, mouse_y):
                        # Reset the game state to start a new game
                        board = [['.' for _ in range(BOARD_COLS)] for _ in range(BOARD_ROWS)]
                        player = 'X'
                        game_over = False
                        screen.fill(BG_COLOR)
                        draw_lines()
                        waiting_for_restart = False


    draw_lines()
    pygame.display.update()


pygame.quit()
