from src.Board import Board


def game():
    """
    Set up tic-tac-toe game. User will be asked for input.
    :return:
    """
    board_size = input("Choose your board size: ")

    if board_size.isnumeric():
        tictactoe = Board(int(board_size))
    else:
        print("Sorry. Not a valid board size")
        return

    # Keep looping through turns until the game is over
    while not tictactoe.gameover:

        # Ask user for move to input
        move = list(map(int, input("Player " + str(tictactoe.turn) + " enter your move: ").split(",")))

        # Check move is valid
        if len(move) == 2 and move[0] < tictactoe.size and move[1] < tictactoe.size:
            # Execute the users move (only if space is available)
            tictactoe.execute_move(move)

            # Show board to the user
            tictactoe.show_board()

            # Check whether a player has won
            tictactoe.check_win()

        else:
            print("Not a valid move! Try again.")


if __name__ == "__main__":
    game()
