def test_picks_highest_rated_from_list():
    # nominal test case

    # arrange
    restaurants = [
            {"name": "Grillby's", "rating": 1},
            {"name": "Crow's Nest", "rating": 5}
        ]

    # act
    output = get_highest_rated(restaurants)
    
    # assert
    assert output == {"name": "Crow's Nest", "rating": 5}

def test_picks_from_list_of_one():
    # edge test case

    # arrange
    restaurants = [{"name": "Crow's Nest", "rating": 1}]

    # act
    output = get_highest_rated(restaurants)
    
    # assert
    assert output == {"name": "Crow's Nest", "rating": 1}

def test_returns_none_with_zero_restaurants(self):
    # edge test case

    # arrange
    restaurants = []

    # act
    output = get_highest_rated(restaurants)
    
    # assert
    assert output is None