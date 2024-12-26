Imagine working on software that determines the winner of a game of Tic Tac Toe. Create a function named tic_tac_toe_winner that is responsible for determing the state of a Tic Tac Toe board - Either there's no winner, it's a tie, 'X' won, or 'O' won. This function should take in 3x3 matrix as a parameter. Each element is either an 'X', 'O', or empty string ''. This function should have a return value of the winner 'X' or 'O', 'Tie' (for a full board with no winner), or None (for a game that is still in progress).

Example 1: Input:

[
    ['X', 'O', 'X'],
    ['O', 'O', 'X'],
    ['X', 'X', 'O']
]
Output: 'Tie'

Example 2: Input:

[
    ['X', 'O', 'X'],
    ['O', 'O', 'X'],
    ['X', 'O', '']
]
Output: 'O'

Example 3: Input:

[
    ['X', 'O', 'O'],
    ['O', 'X', 'O'],
    ['', '', 'X']
]
Output: 'X'

Example 4: Input:

[
    ['X', '', 'O'],
    ['O', 'X', 'X'],
    ['', '', '']
]
Output: None