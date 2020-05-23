class Board():
    """
    Class that creates a 3x3 board that is modified by user input.
    """
    def __init__(self, size):
        """
        Initialises size of board. Sets player 1 as first turn. Sets gameover to False.
        """
        self.size = size
        self.board = []

        row = [' '] * size
        for i in range(size):
            self.board.append(row[:])

        # Set Player 1 to move first
        self.turn = 1

        # Set gamover flag to False
        self.gameover = False

    def show_board(self):
        """
        Shows current state of the board.
        :return:
        """
        for i in range(len(self.board)):
            print(self.board[i])

    def execute_move(self, move):
        """
        Takes in user int list of size 1 x 2 to define player move.
        :param move: 1 x 2 size list of integers. [x, y] where x gives vertical and y gives horizontal position.
        :return:
        """
        # Check that the move is valid first
        if len(move) == 2 and move[0] <= self.size - 1 and move[1] <= self.size - 1:
            # Check that space is open first
            if self.board[move[0]][move[1]] == " ":

                # Player 1's turn
                if self.turn == 1:
                    self.board[move[0]][move[1]] = "X"

                    self.turn = 2

                # Player 2's turn
                elif self.turn == 2:
                    self.board[move[0]][move[1]] = "O"

                    self.turn = 1
            else:
                print("This space is taken! Please try again...")
        else:
            print("Out of bounds. Please try again!")

    def check_win(self):
        """
        Checks board to see if a player has one. Sets self.gameover to True if this is the case.
        :return:
        """

        # Check horizontals
        for i in range(self.size):
            if self.board[i][:] == ['X'] * self.size:
                self.gameover = True
                print("Player 1 wins!")
                return

            if self.board[i][:] == ['O'] * self.size:
                self.gameover = True
                print("Player 2 wins!")
                return

        # Check verticals

        # transpose board using zip matrix. using map will keep it as list of lists.
        transpose = list(map(list, zip(*self.board)))

        for i in range(self.size):
            if transpose[i][:] == ['X'] * self.size:
                self.gameover = True
                print("Player 1 wins!")
                return

            if transpose[i][:] == ['O'] * self.size:
                self.gameover = True
                print("Player 2 wins!")
                return

        # check diagonals
        diagonal = []
        diagonal_inv = []

        # Create list of diagonal values
        for i in range(self.size):
            diagonal.append(self.board[i][i])
            diagonal_inv.append(self.board[self.size - i - 1][i])

        # Check win
        if diagonal == ['X'] * self.size or diagonal_inv == ['X'] * self.size:
            self.gameover = True
            print("Player 1 wins!")
            return
        elif diagonal == ['O'] * self.size or diagonal_inv == ['O'] * self.size:
            self.gameover = True
            print("Player 2 wins!")
            return

        # Check if board is full
        if not any(' ' in x for x in self.board) and self.gameover == False:
            self.gameover = True
            print("Board full! Nobody wins... :(")
            return
