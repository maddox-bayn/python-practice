import os
def add(a, b):
    return a + b
def substract(a, b):
    return a - b
def multiplication(a, b):
    return a * b
def divide(a, b):
    return a / b

operation_dic = {
    '+': add,
    '-': substract,
    '*': multiplication,
    '/': divide,
}

def calculator():
    number1 = int(input("Enter number: "))
    for symbols in operation_dic:
        print(symbols)
    continue_flag = True
    while True:
        op_symbols = input("Enter any Operation")
        numbwe2 = int(input("Enter second number: "))
        calculation_function = operation_dic[op_symbols]
        output = calculation_function(number1,numbwe2)
        print(f"{number1} {op_symbols} {numbwe2} = {output}")
        should_continue  = input(f"Enter y to cntinue with {output}, or n to new operation or x to  exit")
        if should_continue == 'y':
            number1 = output
        elif should_continue == 'n':
            continue_flag = False
            os.system("cls")
            calculator()
        else:
            continue_flag = False
calculator()


# caculator
import os
def add(a, b):
    return a + b
def sudtraction(a, b):
    return a - b
def multiplication(a, b):
    return a * b
def divide(a, b):
    return a / b

operatiion_dic = {
    '+': add,
    '-': sudtraction,
    '*': multiplication,
    '/': divide,
}

def caculator():
    number1 = float(input("Enter your first number: "))
    for symbol in operatiion_dic:
        print(symbol)
    continue_flag = True
    while True:
        op_symbol = input("Pick an Operation ")
        number2 = float(input("Enter your second number: "))
        caculator_function = operatiion_dic[op_symbol]
        output = caculator_function(number1,number2)
        print(f"{number1} {op_symbol} {number2} = {output}")

        shoud_continue = input(f"enter y to continue calculation with {output} or n to  start a new calculation or x exit: ").lower()
        if shoud_continue == 'y':
            number1 = output
        elif shoud_continue == 'n':
            continue_flag = False
            os.system('cls')
            caculator()
        else:
            continue_flag = False
            print("Bye")
caculator()