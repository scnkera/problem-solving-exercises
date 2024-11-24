def hamming_distance(strand1, strand2):
    if len(strand1) != len(strand2):
        raise ValueError("Error message describing the issue")
    
    num_of_differences = 0
    for i in range(len(strand1)):
        if strand1[i] != strand2[i]:
            num_of_differences += 1
    return num_of_differences