import time
import copy
import math
import random
class MCTS(object):
    """
    AI Player, use Monte Carlo Tree Search with UCB

    """
    def __init__(self,board,play_turn,n_in_row=5,time=5,max_actions=100):
        self.board = board
        self.play_turn = play_turn
        self.calculation_time = float(time)
        self.max_actions = max_actions
        self.n_in_row = n_in_row

        self.player = play_turn[0]
        self.confident = 1.96
        self.plays = {} # 记录着法参与模拟的次数 key:(palyer,move) value: number
        self.wins = {} # 记录着法获胜的次数 (玩家，落子)： 次数
        self.max_depth = 1


    def get_action(self): # return moves
        if len(self.board.availables) == 1:
            return self.board.availables[0]
        self.plays = {}
        self.wins = {}
        simulations = 0
        begin = time.time()
        while time.time() - begin < self.calculation_time :
            board_copy = copy.deepcopy(self.board)
            play_turn_copy = copy.deepcopy(self.play_turn)
            self.run_simulation(board_copy,play_turn_copy)
            simulations += 1
        print("Total simulations = ",simulations)

        move = self.select_one_move() # 选择最佳着法
        location = self.board.move_to_location(move)
        print("Max depth searched: ", self.max_depth)
        print("AI move: {0}, {1}".format(location[0],location[1]))
        return move


    def run_simulation(self,board,play_turn):
        """
        MCTS main process
        :param board:
        :param play_turn:
        :return:
        """
        plays = self.plays
        wins = self.wins
        availables = board.availables

        player = self.get_player(play_turn)
        visited_states = set()
        winner = -1
        expand = True

        # simulation
        for t in range(1,self.max_actions + 1):
            if all(plays.get((player,move))for move in availables):
                log_total = math.log(sum(plays[(player,move)]for move in availables))
                value,move = max(((wins[(player,move)]/plays[(player,move)])+ math.sqrt(self.confident*log_total/plays[(player,move)]),move) for move in availables)
            else:
                move = random.choice(availables)
            board.update(player,move)

            # Expand
            if expand and (player,move) not in plays:
                expand = False
                plays[(player,move)] = 0
                wins[(player,move)] = 0
                if t > self.max_depth:
                    self.max_depth = t
            visited_states.add((player,move))
            is_full = not len(availables)
            win,winner = self.has_a_winner(board)
            if is_full or win:
                break
            player = self.get_player(play_turn)

        # Back propagation
        for player,move in visited_states:
            if (player,move) not in plays:
                continue
            plays[(player,move)] += 1
            if player == winner:
                wins[(player,move)] += 1

    def get_player(self,players):
        p = players.pop(0)
        players.append(p)
        return p


    def select_one_move(self):
        percent_wins, move = max((self.wins.get((self.player,move),0)/ self.plays.get((self.player,move),1),move) for move in self.board.availables)
        return move

    def has_a_winner(self,board):
        moved = list(set(range(board.width * board.height)) - set(board.availables))
        if (len(moved) < self.n_in_row +2):
            return False,-1
        width = board.width
        height = board.height
        states = board.states
        n = self.n_in_row
        for m in moved:
            h = m // width
            w = m % width
            player = states[m]

            # 横向连城一线
            if (w in range(width - n + 1) and len(set(states[i] for i in range(m,m+n))) == 1):
                return True,player
            # 竖向连城一线
            if (h in range(height -n + 1) and len(set(states[i] for i in range(m,m+n*width,width)))==1):
                return True,player
            if (w in range(width - n + 1) and h in range(height-n+1) and len(set(states[i] for i in range(m,m+n*(width+1),width+1)))==1):
                return True,player
            if (w in range(width - n + 1) and h in range(height-n+1) and len(set(states[i] for i in range(m,m+n*(width-1),width-1)))==1):
                return True,player
        return False,-1


    def __str__(self):
        return "AI"





