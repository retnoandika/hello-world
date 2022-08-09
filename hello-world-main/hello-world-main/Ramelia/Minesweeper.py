import random

#lets create a board object to represent the minisweeper game
# this is so that we can just say "create a new board object", or 
# "dig here", or "render this game for this object"
class Board:
    def _init_(self, dim_size, num_bombs):
        # let's keep track of these parameters. they'll be helpful later
        self.dim_size = dim_size
        self.num_bombs = num_bombs

        # let's create the board
        # helper function!
        self.board = self.make_new_board() # plant the bombs
        self.assign_values_to_board()
        
        # initialize a set to keep track of which locations we've uncovered
        # we'll save (row,col) tuples into this set
        self.dug = set() # if we dig at 0, 0, then self.dug = {(0,0)}

    def make_new_board(self):
        # construct a new board based on the dim size and num bombs
        # we should construct the list of lists here(or whatever representation you prefer,
        # but since we have a2-D board, list of lists is most natural)

        # generate a new board
        board = [[None for _ in range(self.dim_size)] for _ in range(self.dim_size)]
        # this creates an array like this:
        # [ [None, None, ..., None],
        #   [None, None, ..., None],
        #   [...                  ],
        #   [None, None, ..., None]]
        # we can see how this represents a board!

        # plant the bombs
        bombs_planted = 0
        while bombs_planted < self.num_bombs:
            loc = random.randint(0, self.dim_size**2 -1) # return a random integer N such that a <= N <= b
            row = loc // self.dim_size # we want the number of times dim_size goes into loc to tell us 
            col = loc % self.dim_size # we want the remainder totell us what index in that row to loo

            if board[row][col] == '*':
                # this means we've actually planted a bomb there already so keep going
                continue

            board[row][col] = '*' # plant the bomb
            bombs_planted += 1

# play the game
def play(dim_size=10, num_bombs=10):
    # step 1= create the board and planet the bombs
    # step 2: show the user the board and ask for where they want todig
    # step 3a: if location is a bomb, show game over message
    # step 3b: if location is a bomb, dig recursively until each square is at least
    #           next to a bomb
    # step 4: repeat steps 2 and 3a/b until there are no more places to dig -> VICTORY!
    pass