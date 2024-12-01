def pairs_with_given_sum(numbers, target):

    if not isinstance(target, int) or not all(isinstance(num, int) for num in numbers):
        raise ValueError("Inputs must be intergers only.")
    
    count = 0
    
    for index in range(len(numbers)):
        for j in range(index + 1, len(numbers)):
            if numbers[index] + numbers[j] == target:
                count += 1
                
    return count