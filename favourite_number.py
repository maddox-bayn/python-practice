my_tuple = (1, 2, 3, 4, 5)
my_list = list(my_tuple)
my_list.reverse()
print(my_list)


my_tuple = my_list
def print_board(board):
    print(f"{board[0]} | {board[1]} | {board[2]}") 