def test_nominal_list():
    # nominal test case
    # Arrange
    arr = [2,3,4,7,11]
    k = 5

    # Act
    result = kth_missing_positive_number(arr, k)

    # Assert
    assert result == 9

def test_empty_lists():
    # edge test case
    # Arrange
    arr = []
    k = 3

    # Act
    result = kth_missing_positive_number(arr, k)

    # Assert
    assert result == 3
