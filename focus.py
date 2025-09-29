def is_year_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
    
def days_in_month(month, year):
    list_month = [31,28,31,30,31,30,31,31,30,31,30,31]
    if month == 2 and is_year_leap(year):
        return 29
    else:
        return [month-1]
year = int(input('Enter year: '))
month= int(input("Enter year: "))
out_put = days_in_month(month, year)