def test_correct_score_for_all_letters():
    # nominal test case

    # Arrange
    strand1 = "GAGCCTACTAACGGGAT"
    strand2 = "CATCGTAATGACGGCCT"

    # Act
    result = hamming_distance(strand1, strand2)

    # Assert
    assert result == 7

def test_ignores_special_characters():
    # edge test case

    # Arrange
    strand1 = "GAG"
    strand2 = ""

    # Act/Assert
    with pytest.raises(ValueError):
        hamming_distance(strand1, strand2)  