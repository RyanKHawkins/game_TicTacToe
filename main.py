"""
Title:  TicTacToe
Author:  Ryan Hawkins
Update:  2019-11-08
"""

board = {}
BLANK = ""

def create_board():
    for row in range(1,4):
        for col in range(1,4):
            board[(row,col)] = BLANK
    return board

def display_board(board):
    labels = []
    for row in range(1,4):
        for col in range(1,4):
            labels.append(str(board[(row,col)]).center(3))
    print("""
{}|{}|{}
---+---+---
{}|{}|{}
---+---+---
{}|{}|{}""".format(*labels))

def display_locations():
    print("""
 1 | 2 | 3 
---+---+---
 4 | 5 | 6 
---+---+---
 7 | 8 | 9 """)

board = create_board()
display_board(board)

board[(1,1)] = "X"
display_board(board)

display_locations()