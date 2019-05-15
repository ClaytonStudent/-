class Board(object):
    """
    Board for games
    """
    def __init__(self,width=8,height=8,n_in_row=5):
        self.width = width
        self.height = height
        self.states = {} # 记录当前棋盘的状态 Key：位置 value：棋子
        self.n_in_row = n_in_row


    def init_board(self):

        if self.width < self.n_in_row or self.height < self.n_in_row:
            raise Exception("Board with and height can not less than {}".format(self.n_in_row))
        self.availables = list(range(self.width * self.height))
        for m in self.availables:
            self.states[m] = -1


    def move_to_location(self,move):
        h = move // self.width
        w = move % self.width
        return [h,w]

    def location_to_move(self,location):
        if(len(location)!=2):
            return -1
        h = location[0]
        w = location[1]
        move = h * self.width + w
        if (move not in range(self.width * self.height)):
            return -1
        return move

    def update(self,player,move):
        self.states[move] = player
        self.availables.remove(move)
        