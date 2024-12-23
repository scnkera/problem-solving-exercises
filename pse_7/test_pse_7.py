def test_two_nominal_lists():
    # nominal test case
    # Arrange
    matrix = [[1], [2], [3], [4]]
    r = 1
    c = 4

    # Act
    result = reshape_matrix(matrix, r, c)

    # Assert
    assert result == [[1, 2, 3, 4]]

def test_empty_lists():
    # edge test case
    # Arrange
    matrix = []
    r = 0
    c = 0

    # Act
    result = reshape_matrix(matrix, r, c)

    # Assert
    assert result == []

def test_list_one_all_before_list_two():
    # alternative edge test case
    # Arrange
    matrix = [[1,2], [3,4]]
    r = 3
    c = 2

    # Act
    result = reshape_matrix(matrix, r, c)

    # Assert
    assert result == [[1,2], [3,4]]
