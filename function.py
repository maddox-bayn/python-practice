def calculate_rectangle_area(lenght, width):
    return lenght * width

def calcuiate_circle_area(raduis):
    return 3.14 * raduis * raduis


rect_area = calculate_rectangle_area(10, 5)
circle_area = calcuiate_circle_area(7) 

print(f"Area of the rectangle: {rect_area}")
print(f"Area of the circle: {circle_area}")

try:
    # code that may raise an exception
except ExceptionType:
    #code to handle the exception 
else:
    #code to execute if no exception are raised (optiional)
finally:
    #code that will run no matter what (optional)

    # function & exception 
 def divide_numbers(a, b):
    try:
        result = a / b 
    except ZeroDivisionError:
        return "Error: cannot divide by Zero!"
    except TypeError:
        return "Error: invalid input! please provide numbers."
    else: 
        return result
    # using the function 
num1 = input("enter the fisrt number: ")
num2 = input("enter the second number: ")

try:
    num1 = float(num1)
    num2 = float(num2)
    print(f"Result:{divide_numbers(num1, num2)}")
except ValueError:
    print("invalid input! please enter numeric value.")

# fuction raise
def check_positive_number(num):
    if num <= 0:
        raise ValueError("the number must be positive")
    return num
try:
    check_positive_number(5)
except ValueError as e:
    print(e)
 # combining function exception
def divide_numbers(numbers, divisor):
    results = []
    for num in numbers:
        try:
            result = num / divisor
            results.append(result)
        except ZeroDivisionError:
            results.append("cannot divide by zero")
        except TypeError:
            results.append("invalide type, numers expected")
            return results
numbers = [10, 20, 30, "forty"]
divisor = 0 
print(divide_numbers(numbers, divisor))

def sum_and_diffrernce(num1, num2):
    sum = num1 + num2
    diffrernce = num1 - num2
    return sum, diffrernce
sum_result, diff_result = sum_and_diffrernce(10, 4)
print(f"sum: {sum_result}, diffrernce: {diff_result}")

def is_year_leap(year):
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True
years = [2000, 1999, 2020, 2024, 2023]
for year in years:
    if is_year_leap(year):
        print(f"{year} is a leap year")
    else:
        print(f"{year} is nott a leap year")

# recursive function
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)
print(factorial(4))
def fun(a):
    if a > 30:
        return 3
    else:
        return a + fun(a + 3)
print(fun(25))
# function is triagle
def is_triangle(a, b, c):
    return a + b > c and b + c > a and a + c > b
def therom(a, b, c):
    p = (a+b+c)/2
    return(p*(p-a)*(p-b)*(p-c))
def areaa_of_triangle(a, b, c):
    if not is_triangle(a, b, c):
        return None
    return therom
print(areaa_of_triangle(1, 1, 2**5))
# fntion fctoria
def factorial_fun(n):
    if n < 0:
        return None
    if n < 2:
        return 1
    Product = 1
    for i in range(2, n + 1):
        Product*= i
    return Product
for i in range(1, 6):
    print(factorial_fun(3))
    def is_num_prime(num):
    for i in range(2, int(1 + num ** 0.5)):
        if num % i == 0:
            return False
    return True
for i in range(1, 20):
    if is_num_prime(i + 1):
        print(i + 1, end="")
print()