def print_board(board):
    for row in board:
        print(" | ".join(row))   
        print("-" * 9)
def check_winner(board):
    # check rowss, columns, and
    for row in board:
        if row.count(row[0]) == 3 and row[0] != " ":
            return row[0]
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return board[0][col]
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] ==  board[2][0] and board[0][2] != " ":
        return board[0][2]
    return None
def is_board_full(board):
    for row in board:
        if " " in row:
            return False      
    return True
def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    currenta_player = "X"   
    while True:
        print_board(board)
        print(f"player {currenta_player} enter your move (row and colunm): ")
        try:
            row, col = map(int, input().split())
            if board[row][col] != " ":
                print("this position is already taken. try again.")
                continue
        except (ValueError, IndexError):
            print("invalid input. please enter row a row and colboumn as two numbers (0, 1)")
            continue
        board[row][col] = currenta_player
        winner = check_winner(board)
        if winner:
            print_board(board)  
            print(f"player {winner} wins!")
            break
        if is_board_full(board):
            print_board(board)
            print("it's a draw!")
            break
        currenta_player = "O" if currenta_player == "X" else "X"
if __name__ == "_main_":
    tic_tac_toe()  