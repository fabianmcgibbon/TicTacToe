from src.Board import Board


def test_board_init_3():
    board = Board(3)

    assert board.board == [[' ', ' ', ' '],
                           [' ', ' ', ' '],
                           [' ', ' ', ' ']]
    assert board.turn == 1
    assert board.gameover == False


def test_board_init_4():
    board = Board(4)

    assert board.board == [[' ', ' ', ' ', ' '],
                           [' ', ' ', ' ', ' '],
                           [' ', ' ', ' ', ' '],
                           [' ', ' ', ' ', ' ']]
    assert board.turn == 1
    assert board.gameover == False


def test_board_execute_move_4_1_1():
    board = Board(4)
    board.execute_move([1, 1])

    assert board.board == [[' ', ' ', ' ', ' '],
                           [' ', 'X', ' ', ' '],
                           [' ', ' ', ' ', ' '],
                           [' ', ' ', ' ', ' ']]
    assert board.turn == 2
    assert board.gameover == False


def test_board_execute_move_3_1_1():
    board = Board(3)
    board.execute_move([1, 1])

    assert board.board == [[' ', ' ', ' '],
                           [' ', 'X', ' '],
                           [' ', ' ', ' ']]
    assert board.turn == 2
    assert board.gameover == False


def test_board_execute_move_same_place():
    board = Board(3)
    board.execute_move([1, 1])
    board.execute_move([1, 1])

    assert board.board == [[' ', ' ', ' '],
                           [' ', 'X', ' '],
                           [' ', ' ', ' ']]
    assert board.turn == 2
    assert board.gameover == False


def test_board_execute_move_invalid():
    board = Board(3)
    board.execute_move([1])

    assert board.board == [[' ', ' ', ' '],
                           [' ', ' ', ' '],
                           [' ', ' ', ' ']]
    assert board.turn == 1
    assert board.gameover == False


def test_board_check_win_hor():
    board = Board(3)
    board.execute_move([0, 0])
    board.execute_move([1, 0])
    board.execute_move([0, 1])
    board.execute_move([1, 1])
    board.execute_move([0, 2])
    board.check_win()

    assert board.board == [['X', 'X', 'X'],
                           ['O', 'O', ' '],
                           [' ', ' ', ' ']]

    assert board.gameover == True


def test_board_check_win_ver():
    board = Board(3)
    board.execute_move([0, 0])
    board.execute_move([0, 1])
    board.execute_move([1, 0])
    board.execute_move([1, 1])
    board.execute_move([2, 0])
    board.check_win()

    assert board.board == [['X', 'O', ' '],
                           ['X', 'O', ' '],
                           ['X', ' ', ' ']]

    assert board.gameover == True


def test_board_check_win_diag():
    board = Board(3)
    board.execute_move([0, 0])
    board.execute_move([0, 1])
    board.execute_move([1, 1])
    board.execute_move([1, 2])
    board.execute_move([2, 2])

    assert board.size == 3

    assert board.board == [['X', 'O', ' '],
                           [' ', 'X', 'O'],
                           [' ', ' ', 'X']]

    board.check_win()

    assert board.gameover == True


def test_board_check_win_diag_inv():
    board = Board(3)
    board.execute_move([0, 2])
    board.execute_move([0, 1])
    board.execute_move([1, 1])
    board.execute_move([1, 0])
    board.execute_move([2, 0])

    assert board.size == 3

    assert board.board == [[' ', 'O', 'X'],
                           ['O', 'X', ' '],
                           ['X', ' ', ' ']]

    board.check_win()

    assert board.gameover == True