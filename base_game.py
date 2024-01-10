import numpy as np
import pygame
import sys
import random

BLUE = (0, 116, 186)
PINK = (240, 90, 136)
YELLOW = (248, 230, 10)
BLACK =(0, 0, 0)

ROW_COUNT = 6
COL_COUNT = 7

PLAYER = 0
AI = 1

def create_board():
    board = np.zeros((ROW_COUNT, COL_COUNT))
    return board

def drop_piece(board, row, col, piece):
    board[row][col] = piece

def is_valid_location(board, col):
    return board[ROW_COUNT - 1][col] == 0

def get_next_open_row(board, col):
    for r in range(ROW_COUNT):
        if board[r][col] == 0:
            return r
        
def print_board(board):
    print(np.flip(board, 0))

def winning_move(board, piece):
    #Check for horizontal locations
    for c in range(COL_COUNT - 3):
        for r in range(ROW_COUNT):
            if board[r][c]==piece and board[r][c + 1] == piece and board[r][c + 2] == piece and board[r][c + 3] == piece:
                return True
    #Check for vertical locations
    for c in range(COL_COUNT):
        for r in range(ROW_COUNT - 3):
            if board[r][c] == piece and board[r + 1][c] == piece and board[r + 2][c] == piece and board[r + 3][c] == piece:
                return True
    #Check positively sloped diagonal
    for c in range(COL_COUNT - 3):
        for r in range(ROW_COUNT - 3):
            if board[r][c] == piece and board[r + 1][c + 1] == piece and board[r + 2][c + 2] == piece and board[r + 3][c + 3] == piece:
                return True
    #Check negatively sloped diagonal
    for c in range(COL_COUNT - 3):
        for r in range(3, ROW_COUNT):
            if board[r][c]==piece and board[r - 1][c + 1] == piece and board[r - 2][c + 2] == piece and board[r - 3][c + 3] == piece:
                return True

def draw_board(board):
    for c in range(COL_COUNT):
        for r in range(ROW_COUNT):
            pygame.draw.rect(window, YELLOW, (c*SQUARESIZE, r*SQUARESIZE+SQUARESIZE, SQUARESIZE, SQUARESIZE))
            pygame.draw.circle(window, BLACK, (int(c*SQUARESIZE+SQUARESIZE/2),int(r*SQUARESIZE+SQUARESIZE+SQUARESIZE/2)), RADIUS)

    for c in range(COL_COUNT):
        for r in range(ROW_COUNT):
            if board[r][c]==1:
                pygame.draw.circle(window, BLUE, (int(c*SQUARESIZE+SQUARESIZE/2),height-int(r*SQUARESIZE+SQUARESIZE/2)), RADIUS)
            elif board[r][c]:
                pygame.draw.circle(window, PINK, (int(c*SQUARESIZE+SQUARESIZE/2),height-int(r*SQUARESIZE+SQUARESIZE/2)), RADIUS)
    pygame.display.update()

board = create_board()
print_board(board)
game_over = False
turn = 0

pygame.init()
SQUARESIZE = 100
width = COL_COUNT * SQUARESIZE
height = (ROW_COUNT+1) * SQUARESIZE
size = (width, height)
RADIUS = int(SQUARESIZE / 2 - 5)

window = pygame.display.set_mode(size)
draw_board(board)
pygame.display.update()
pygame.display.set_caption("Connect 4 Minimax")
myfont = pygame.font.SysFont("monospace",75)

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEMOTION:
            pygame.draw.rect(window, BLACK,(0,0,width, int(SQUARESIZE)))
            posX = event.pos[0]
            if turn == 0:
                pygame.draw.circle(window, BLUE, (posX, int(SQUARESIZE / 2)),RADIUS)
            else:
                pygame.draw.circle(window, PINK, (posX, int(SQUARESIZE / 2)),RADIUS)
        pygame.display.update()
        if event.type == pygame.MOUSEBUTTONDOWN:
            pygame.draw.rect(window, BLACK,(0, 0, width, int(SQUARESIZE)))
            if turn == PLAYER:
                posX = event.pos[0]
                col = int(posX / SQUARESIZE) 
                if is_valid_location(board, col):
                    row = get_next_open_row(board, col)
                    drop_piece(board, row, col,1)
                    if winning_move(board, 1):
                        label = myfont.render("Player 1 wins!", 1, BLUE)
                        window.blit(label, (40, 10))
                        game_over = True

                    turn += 1
                    turn = turn % 2 
    
    if turn == AI and not game_over:
        col = random.randint(0, COL_COUNT - 1)

        if is_valid_location(board, col):
            row=get_next_open_row(board, col)
            drop_piece(board, row, col, 2)
            if winning_move(board, 2):
                label = myfont.render("Player 2 wins!", 1, PINK)
                window.blit(label, (40, 10))
                game_over = True

            print_board(board)
            draw_board(board)

            turn += 1
            turn = turn % 2 

    if game_over:
        pygame.time.wait(3000)

pygame.quit()