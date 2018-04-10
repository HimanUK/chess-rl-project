'''
Created on Sun Apr  8 18:14:14 2018
@author: Himanshu Kankal
'''

import chess
import random

board = chess.Board()

while True:
    print(board)
    
    lgmov = list(board.legal_moves)
    lgmov = [str(x) for x in lgmov]
    
    mov = random.choice(lgmov)
    
    now_move = chess.Move.from_uci(mov)
    board.push(now_move)
    
    if board.is_game_over():
        break
    
    print('--------------------------------------- \n')
    
