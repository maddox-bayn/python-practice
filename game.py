from random import randrange
def display_board(board):
    print("+-------" * 3, "+", sep="")
    for row in range(3):
        print("|       " * 3, "|", sep="")
        for col in range(3):
            print("|   " + str(board[row][col] + "   ", end=""))
        print("|")        
        print("|       " * 3, "|", sep="") 
        print("+-------" * 3, "+", sep="" )
# function to handle the user move
def enter_move(board):
    while True:
        try:
            move = int(input("Enter your move(1 - 9): ")) - 1
            row, col = move // 3, move % 3
            if 0 <= move <= 8 and board[row][col] not in ['O', 'X']:
                board[row][col] = 'O'
                break
            else:
                print("invalide move! the cell is either occupied or out of range.")
        except ValueError:
            print("please enter a valid number between  1 and 9,")
# function to find free fileds on the board 
def make_list_of_free_fields(board):
    free = []
    for row in range(3): # iterate through rows
        for col in range(3): # iterate through columns 
            if board[row][col] not in ['O, X']: # is the cell free
                free.append((row, col)) # yes, it is - append new tupel to the list 
    return free
# function to check if a player has won 
def victory_for(board, sgn):
    winning_combinations = [
        [(0, 0), (0, 1), (0, 2)], # rows

        [(1, 0), (1, 1), (1, 2)],
        [(2, 0), (2, 1), (2, 2)], 
        [(0, 0), (1, 0), (2, 0)], # colums

        [(0, 1), (1, 1), (2, 1)],
        [(0, 2), (1, 2), (2, 2)],
        [(0, 0), (1, 1), (2, 2)], #diagonals

        [(0, 2), (1, 1), (2, 0)]
    ]
    for combination in winning_combinations:
        if all(board[row][col] == sgn for row, col in combination):
            return 'me' if sgn == 'X'else 'you'
    return None
# funtion to handle the computer's move
def draw_move(board):
    free = make_list_of_free_fields(board)
    if free:
        row, col = free[randrange(len(free))]
        board[row][col] = 'X'
# main game logic 
def main():
    # initiate the game board
    board = [[3 * j + i + 1 for i in range(3)] for j in range(3)]
    board[1][1] = 'X' # computer start with the center cell
    human_turn = True
    while True:
        display_board(board) # display the board 
        if human_turn:
            enter_move(board) # User's turn 
            victor = victory_for(board, 'O')
        else:
            draw_move(board) # computer's turn
            victor = victory_for(board, 'X')
        # check for a winner
        if victor:
            display_board(board)
            print("you won!" if victor == 'you' else "I won")
            break
        # check for tie
        if not make_list_of_free_fields(board):
            display_board(board)
            print("it is a tie!")
            break
        human_turn = not human_turn # swich turns
# Run the game
if __name__ == "__main__":
    main()