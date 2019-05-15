from Board import Board
from Game import Game
import random

def run():
    n = 5
    try:
        board = Board(width=8, height=8, n_in_row=n)
        game = Game(board, n_in_row=n, time=1)
        game.start()
    except KeyboardInterrupt:
        print('\n\rquit')

if __name__ == '__main__':
    run()