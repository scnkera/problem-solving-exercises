def test_nominal_board():
    # nominal test case
    # Arrange
    board = [['X', 'X', 'X'],
             ['O', 'O', ''],
             ['', '', 'O']]

    # Act
    result = tic_tac_toe_winner(board)

    # Assert
    assert result == 'X'

def test_empty_board():
    # edge test case
    board = [['', '', ''],
             ['', '', ''],
             ['', '', '']]

    # Act
    result = tic_tac_toe_winner(board)

    # Assert
    assert result is None

def test_tied():
    # alternative test case
    # Arrange
    board = [['O', 'X', 'X'],
             ['X', 'O', 'O'],
             ['X', 'O', 'X']]

    # Act
    result = tic_tac_toe_winner(board)

    # Assert
    assert result == 'Tie'