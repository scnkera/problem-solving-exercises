def get_highest_rated(restaurants):
    
    # if falsy, return None
    if not restaurants: 
        return None
        
    # default best restaurant is at index = 0
    best_restaurant = restaurants[0] 
    
    # loops through and returns best restaurant
    for restaurant in restaurants:
        if restaurant["rating"] > best_restaurant["rating"]:
            best_restaurant = restaurant  
    
    print(f'The highest rated restaurant is {best_restaurant["name"]} with a rating of {best_restaurant["rating"]}!')
    return best_restaurant
    
get_highest_rated([{"name": "Sunny's Diner", "rating": 3}, {"name": "Moonlit Café", "rating": 4}, {"name": "Starry Bites", "rating": 4}])
get_highest_rated([{"name": "The Roaring Fork", "rating": 3}, {"name": "Silver Spoon", "rating": 2}, {"name": "Golden Plate", "rating": 5}, {"name": "Iron Skillet", "rating": 3}])
get_highest_rated([{"name": "Bistro on 5th", "rating": 2}, {"name": "Riverview Grill", "rating": 3}, {"name": "Mountain Lodge", "rating": 1}, {"name": "Skyline Eats", "rating": 5}, {"name": "Hidden Gem", "rating": 3}])
get_highest_rated([{"name": "Ocean's Delight", "rating": 4}, {"name": "The Garden Table", "rating": 5}, {"name": "Cozy Corner", "rating": 3}, {"name": "The Urban Kitchen", "rating": 3}, {"name": "Rustic Charm", "rating": 4}, {"name": "Home Hearth", "rating": 5}])
get_highest_rated([{"name": "Lavish Feast", "rating": 3}, {"name": "Simple Suppers", "rating": 4}, {"name": "Vegan Eden", "rating": 3}, {"name": "Carnivore's Cradle", "rating": 5}, {"name": "Brunch Bliss", "rating": 3}, {"name": "Dessert Dreams", "rating": 2}])
get_highest_rated([{"name": "Crow's Nest", "rating": 2}])
get_highest_rated([])