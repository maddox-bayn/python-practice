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
