from random import randrange

def display_board(board):
    print("+-------" * 3, "+", sep="")
    for row in range(3):
        print("|       " * 3, "|", sep="" )
        for col in range(3):
            print("|   " + str(board[row][col]) + "  ", end="")
        print("|")
        print("|       " * 3,"|",sep="")
        print("+-------" * 3,"+",sep="")
def enter_move(board):
    ok = False       # fake assumption - we need it to enter a loop 
    while not ok:
        move = input("Enter your move: ")
        ok = len(move) == 1 and move >= '1' and move <= '9' #is user's input valid?
        if not ok:  
            print("Bad move - repeat your input!")
            continue
        move = int(move) - 1  # cell's number from 0 to 8
        row = move // 3  # cell' row
        col = move % 3 # cell's column
        sign = board[row][col] # check the selected square
        ok = sign not in ['0', 'x']
        if not ok: # it's occupied - to the input again 
            print("field already occupied - repeat your input! ")
            continue
    board[row][col] = '0' # set '0' at the selected  
# function to find free fileds on the board 
def make_list_of_free_fields(board):
    free = []
    for row in range(3): # iterate through rows
        for col in range(3): # iterate through columns 
            if board[row][col] not in ['O, X']: # is the cell free
                free.append((row, col)) # yes, it is - append new tupel to the list 
    return free
def victory_for(board, sgn):
    if sgn == "X": # are we looking for X?
        who = 'me' # yes - it's computer's side
    elif sgn == "O": # ... or for o?
        who = 'you' # yes - it's our side
    else:
        who = None # we should not fall here!
    cross1 = cross2 = True # for diagonals
    for rc in range(3):
        if board[rc][0] == sgn and board[rc][1] == sgn and board[rc][2] == sgn: # check row rc
             return who 
        if board[0][rc] == sgn and board[1][rc] == sgn and board[2][rc] == sgn: # check column rc
            return who 
        if board[rc][rc] != sgn:
            cross1 = False
        if board[2 -rc][2 - rc] != sgn: # check 2nd diagonal
            cross2 = False
        if cross1 or cross2:
            return who 
        return None
def drow_move(board):
    free = make_list_of_free_fields(board) # make a list of free fields
    cnt = len(free)
    if cnt > 0:
        this = randrange(cnt) # select a random free cell 
        row, col = free[this] # get the coordinates 
        board[row][col] = 'x' # place 'X'in the selected cell
board = [[3 * j + 1 for i in range (3)]for j in range(3)]
board[1][1] = 'X' # set first 'X' in the middle
free = make_list_of_free_fields(board)
human_turn = True # which turn is it now?
while len(free):
    display_board(board)
    if human_turn:
        enter_move(board)
        victor = victory_for(board, 'O')
    else:
        drow_move(board)
        victor = victory_for(board, 'X')
    if  victor is not None:
        break
    human_turn = not human_turn # switch turns
    free = make_list_of_free_fields(board) 
display_board(board)
if victor == 'you':
    print("you won!")
elif victor == 'me':
    print("i won")
else:
    print("Tie!")