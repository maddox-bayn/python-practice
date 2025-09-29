from random import choice

value = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'a', 'b', 'c', 'd', 'e']

my_ticket = choice(value)

for i in range(0, len(value)):
    print(choice(value))
    if value[i]== my_ticket:
        print(f"i took {i + 1} iteration toget the ticket {value[i]}")
        break