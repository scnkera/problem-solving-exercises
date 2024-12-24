def kth_missing_positive_number(numbers, k):
    '''
    INPUT: List of positive numbers in increating order & a positive integer k
    OUTPUT: The kth missing number
    '''

    last_number = numbers[-1]
    num_list = []

    for i in range(1,last_number + 1):
        num_list.append(i)

    for num in numbers:
        if num in num_list:
            num_list.remove(num)

    if not num_list:
        return numbers[-1] + k
    else: 
        return num_list[k-1]