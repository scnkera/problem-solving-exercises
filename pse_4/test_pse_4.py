def test_true_for_single_word_palindrome():
    # nominal test case

    # Arrange
    s = "kayak"

    # Act
    result = palindrome(s)

    # Assert
    assert result == True

def test_ignores_capitalization():
    # edge test case

    # Arrange
    s = "Kayak"

    # Act
    result = palindrome(s)

    # Assert
    assert result == True