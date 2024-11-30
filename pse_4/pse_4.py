def palindrome(s):
    cleaned_string = ""
    
    for char in s:
        if char.isalnum(): # checks if the string this is alphanumeric
            cleaned_string += char.lower()

    left = 0 # initial left most index
    right = len(cleaned_string) - 1 # initial right most index

    while left < right:
        if cleaned_string[left] != cleaned_string[right]: # compares characters at indices
            return False
        # continues to increment if true
        left += 1 
        right -= 1

    return True