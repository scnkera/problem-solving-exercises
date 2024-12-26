def tic_tac_toe_winner(board):
    for i in range(3):
        
        # if items in a row are the same but not empty
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] != '':
            return board[i][0]
            
        # if items in a col are the same but not empty
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] != '':
            return board[0][i]
            
    # if items in diagonally are the same but not empty     
    if board[0][0] == board[1][1] == board[2][2] and board[1][1] != '':
        return board[0][0]
    # if items in diagonally are the same but not empty    
    if board[0][2] == board[1][1] == board[2][0] and board[1][1] != '':
        return board[0][2]
        
    # if tie
    is_full = True
    for row in board:
        for cell in row:
            if cell == '':
                is_full = False
                break
        if not is_full:
            break
    
    if is_full:
        return 'Tie'
        
    return None