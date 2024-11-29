def test_correct_total_for_all_items():
    # nominal test case

    # Arrange
    cart = ["Cheese", "Chicken"]

    # Act
    result = calculate_total(cart)

    # Assert
    assert result == 6.5

def test_case_insensitive_gives_correct_total():
    # nominal test case

    # Arrange
    cart = ["beans", "MILK"]

    # Act
    result = calculate_total(cart)

    # Assert
    assert result == 5.0

def test_invalid_items_not_added_to_total():
    # edge test case
    
    # Arrange
    cart = ["Lemon", "Onion", "Onion"]

    # Act
    result = calculate_total(cart)

    # Assert
    assert result == 1.0