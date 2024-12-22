def reshape_matrix(matrix, r, c):
    '''
    INPUT: Two dimensional list, and number of rows and columns of reshaped matrix
    OUTPUT: Reshaped matrix
    '''

    if not matrix:
        return matrix

    new_matrix = [num for row in matrix for num in row]
    matrix_length = len(new_matrix)

    if matrix_length != r * c:
        return matrix

    reshaped_matrix = []
    position = 0
    for row in range(r):
        final_row = []
        for col in range(c):
            final_row.append(new_matrix[position])
            position += 1
        reshaped_matrix.append(final_row)
    return reshaped_matrix
    