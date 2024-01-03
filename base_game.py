import numpy as np
def create_board():
    board =np.zeros((6,7))
    return board
board =create_board
game_over=False
turn =0
while not game_over:
    if turn==0:
        selection =input("Player 1 make your selection (0-6):")
        print(selection)
        print(type(selection))
    else:
        selection=input("Player 2 make your selection (0-6):")
    
    turn +=1
    turn=turn%2