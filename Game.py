from Human import Human
from MCTS import MCTS
import random

class Game(object):
    def __init__(self,board,**kwargs):
        self.board = board
        self.player = [1,2]
        self.n_in_row = int(kwargs.get('n_in_row',5))
        self.time = float(kwargs.get('time',5))
        self.max_actions = int(kwargs.get('max_actions',1000))


    def start(self):
        p1,p2 = self.init_player()
        self.board.init_board()

        # board,play_turn,n_in_row=5,time=5,max_actions=100
        ai = MCTS(self.board,[p1,p2],self.n_in_row,self.time,self.max_actions)
        human = Human(self.board,p2)
        players = {}
        players[p1] = ai
        players[p2] = human
        turn = [p1,p2]
        random.shuffle(turn)
        while(1):
            p = turn.pop(0)
            turn.append(p)
            player_in_turn = players[p]
            move = player_in_turn.get_action()
            self.board.update(p,move)
            self.graphic(self.board,human,ai)
            end,winner = self.game_end(ai)
            if end:
                if winner != -1:
                    print("Game end. Winner is: ", players[winner])
                break

    def init_player(self):
        plist = list(range(len(self.player)))
        index1 = random.choice(plist)
        plist.remove(index1)
        index2 = random.choice(plist)

        return self.player[index1], self.player[index2]


    def game_end(self,ai):
        win,winner = ai.has_a_winner(self.board)
        if win:
            return True,winner
        elif not len(self.board.availables):
            print("Game end. Tie")
            return True,-1
        return False,-1


    def graphic(self,board,human,ai):
        width = board.width
        height = board.height
        print("Human Player",human.player, "with X".rjust(3))
        print("AI Player",ai.player,"with 0".rjust(3))
        print()
        for x in range(width):
            print("{0:8}".format(x),end='')
        print('\r\n')
        for i in range(height-1,-1,-1):
            print("{0:4d}".format(i),end='')
            for j in range(width):
                loc = i*width + j
                if board.states[loc] == human.player:
                    print('X'.center(8),end = '')
                elif board.states[loc] == ai.player:
                    print('o'.center(8),end='')
                else:
                    print('_'.center(8),end='')
            print('\r\n')




