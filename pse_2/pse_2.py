def calculate_total(cart):
    store_items = {
    "apple": 0.75,
    "beans": 2.00,
    "cheese": 2.50,
    "chicken": 4.00,
    "flour": 1.75,
    "onion": 0.50,
    "orange": 0.85,
    "lettuce": 1.25,
    "milk": 3.00,
    "tomato": 0.45
    }
    
    cart_total = 0.0
    
    for item in cart:
        item_lower = item.lower()
        if item_lower in store_items:
            cart_total += store_items[item_lower]

    print(f'The total cart amount is: ${cart_total}')
    return(cart_total)

calculate_total({
    "apple": 0.75,
    "beans": 2.00,
    "cheese": 2.50,
    "chicken": 4.00,
    "flour": 1.75,
    "onion": 0.50,
    "orange": 0.85,
    "lettuce": 1.25,
    "milk": 3.00,
    "tomato": 0.45
    })