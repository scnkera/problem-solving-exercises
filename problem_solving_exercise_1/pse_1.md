Imagine working on software that deals with restaurant reviews.

Create a function named get_highest_rated that is responsible for finding the highest-rated restaurant.

This function should take in a list of dictionaries named restaurants as a parameter. Each dictionary represents the data associated with a restaurant, including its rating. This function should have a return value of the restaurant with the highest rating.

Input (Parameters of the function)	Expected Output (Return value of the function)
restaurants = [{"name": "Grillby's", "rating": 1}, {"name": "Crow's Nest", "rating": 5}]	{"name": "Crow's Nest", "rating": 5}
restaurants = [{"name": "Crow's Nest", "rating": 1}]	{"name": "Crow's Nest", "rating": 1}
restaurants = []	None