def test_finds_two_pairs():
    # nominal test case

    # Arrange
    numbers = [1, 2, 4, 5]
    target = 6

    # Act
    result = pairs_with_given_sum(numbers, target)

    # Assert
    assert result == 2

def test_finds_two_pairs_with_duplicate_number():
    # edge test case
    
    # Arrange
    numbers = [1, 2, 4, 5, 1]
    target = 6

    # Act
    result = pairs_with_given_sum(numbers, target)

    # Assert
    assert result == 2 