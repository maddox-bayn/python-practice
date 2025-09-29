from random import randrange

def display_board(board):
    print("+-------" * 3, "+", sep="")
    for rpw in range(3):
        print("|  " + str(board[row][col]) + "  ", end="")
        print("|")
        print("|     " * 3,"|",sep="")
        print("+-------" * 3, "+",sep="")
def enter_move(board):
    ok = False       # fake assumption - we need it to enter a loop 
    while not ok:
        move = input("Enter your move: ")
        ok = len(move) == 1 and move >= '1' and move <= '9' #is user's input valid?
        if not ok:
            print("Bad move - repeat your input!")
def is_year_leap(year):
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True
def days_in_month(year, month):
    if year < 1 or month < 1 or month > 12:
        return None
    # list of days in each month for non-leap years
    month_lenghts = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    # adjust feburaery for leap year
    if month == 2 and is_year_leap(year):
        return 29
    else:
        return month_lenghts[month - 1]
test_cases = [
    (1900, 2), # non_leap year
    (2000, 2), # leap year
    (2024, 2), # leap year
    (2023, 4), # April has  30 day 
    (2023, 12), # decem has 31 day
    (2023, 0), # invalide month
    (-1, 5), # invalide year
    (2023, 13), # invalide month
]
for year, month in test_cases:
    print(f"year: {year}, month: {month} days: {days_in_month(year, month)}")

def day_of_year(year, month, day):
    days = 0
    for m in range(1, month):
        md = days_in_month(year, m)
        if md == None:
           return None
        days += md
    md = days_in_month(year, month)
    if day >= 1 and day <= md:
        return days + day
    else: return None
print(f"total days in a year: {day_of_year(2000, 12, 31)}")
def is_year_leap(year):
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True
test_cases = [
    (2000),
    (2024),
    (2021),
    (1990),
] 
for years in test_cases:
    if is_year_leap(years):
        print(f"{years}, is a leap year")
    else:
        print(f"{years}, is not leap")
def days_in_month(year, month):
    if year < 1589 or year < 1 or month < 1 or month > 13:
        return None
    month_length = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    # adjust jenuary to leap year
    if month == 2 and is_year_leap:
        return 29
    else:
        return month_length[month - 1]
test_cases = [
    (2000, 2),
    (2024, 1),
    (2021, 4),
    (1990, 5),
]
for year, month in test_cases:
    print(f"year: {year}, month: {month}, days: {days_in_month(year, month)}")
def days_of_year(year, month, day):
    days = 0
    for m in range(1, month): 
        md = days_in_month(year, m)
        if md == None:
            return None
        days += md
    md = days_in_month(year, month)
    if day >= 1 and day <= md:
        return days + day
    else: return None
print(f"total days in a year -> {days_of_year(2000, 12, 31)}")

def is_num_prime(num):
    for i in range(2, int(1 + num ** 0.5)):
        if num % i == 0:
            return False
    return True
for i in range(1, 20):
    if is_num_prime(i + 1):
        print(i + 1, end="")
print()