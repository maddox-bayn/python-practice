import os

def add(a,b):
    return a +b 
def subtract(a,b):
    return a - b
def multiply(a,b):
    return a * b
def divide(a,b):
    return a / b

dic_calcualtion = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide,
}
def caculator():
    number1 = int(input("Enter first number: "))
    continue_flag = True
    while continue_flag:
        for symbols in dic_calcualtion:
            print(symbols)
        op_symbol = input("pick an operation: ")
        calculator_function = dic_calcualtion[op_symbol]
        number2 = int(input("Enter yuor second number: "))
        output = calculator_function(number1,number2)
        print(f"{number1} {op_symbol} {number2} = {output}")
        should_continue = input(f"Enter y to continue caculation with {output} and  n to start new calculation or 'x' to exit: ")
        if should_continue == 'y':
            number1 = output
        elif should_continue == 'n':
            os.system('cls')
            caculator()
        elif should_continue == 'x':
            continue_flag = False
            return
        else:
            print("wrong input! you entered a wrong condition")
            return
caculator()