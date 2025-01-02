def test_two_nominal_lists():
    # nominal test case
    # Arrange
    stocks = [7,1,5,3,6,4]

    # Act
    result = max_profit(stocks)

    # Assert
    assert result == 7

def test_empty_lists():
    # edge test case
    # Arrange
    stocks = []

    # Act
    result = max_profit(stocks)

    # Assert
    assert result == 0

    # Assert
    assert result == []

def test_list_1_all_before_list_2():
    # alternative test case
    # Arrange
    stocks = [7,6,5,4,3,1]

    # Act
    result = max_profit(stocks)

    # Assert
    assert result == 0