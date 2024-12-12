def test_two_nominal_lists():
    # nominal test case
    # Arrange
    list1 = [1, 2, 4, 6]
    list2 = [5]

    # Act
    result = merge_lists(list1, list2)

    # Assert
    assert result == [1, 2, 3, 4, 5, 6]

def test_empty_lists():
    # edge test case
    # Arrange
    list1 = []
    list2 = []

    # Act
    result = merge_lists(list1, list2)

    # Assert
    assert result == []

def test_list_1_all_before_list_2():
    # alternative test case
    # Arrange
    list1 = [-50, -25, 0]
    list2 = [10, 20, 30]

    # Act
    result = merge_lists(list1, list2)

    # Assert
    assert result == [-50, -25, 0, 10, 20, 30]