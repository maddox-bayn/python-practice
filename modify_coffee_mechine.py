menu = {
    'latte':{  
        'ingredients':{
            'water': 200,
             'milk':150,
            'coffee':24,
        },
        'cost':150
    },
    'espresso':{
        'ingredients': {
            'water': 50,
            'coffee':18,
        },
        'cost': 100,
    },
    'cappuccino': {
        'ingredients':{
            'water': 250,
            'milk': 100,
            'coffee': 24,
        },
        'cost': 200
    }
}
profit=0
resources = { 
    'water': 500,
    'milk': 200,
    'coffee': 100
}

def check_resources(ordered_confi):
    for item in ordered_confi:
        if ordered_confi[item]>resources[item]:
            print(f"there is not enough {item}")
            return False
    return True

def process_coin(): 
    print("insert your how many of coin:")
    total = 0
    five_coin = input("insert your 5 kb coin: ")
    ten_coin = input("insert your 10 kb coin: ")
    twenty_coin = input("insert your 20 kb coin: ")
    total = five_coin*5 + ten_coin*10 + twenty_coin*20
    return total

def is_payment_successful(payment, coffee_cost):
    if payment>=coffee_cost:
        global profit
        profit += coffee_cost
        change = payment - coffee_cost
        print(f"Here is your {change}")
    else:
        print("insurficient funds! here is your money")

def make_coffee(choice, coffee):
    for item in coffee:
        resources[item]-= coffee[item]
    print("here is your cofffee")
is_on = True
while is_on:
    choice = input("what whould like to have (latte/esspresso/cappuccino): ")
    if choice == 'off':
        is_on = False
    elif choice == 'repot':
        print(f"water = {resources['water']}")
        print(f"milk = {resources['milk']}")
        print(f"coffee = {resources['coffee']}")
    else:
        coffee_type = menu[choice]
        if check_resources(coffee_type['ingredient']):
            payment = process_coin()
            if is_payment_successful(payment, coffee_type['cost']):
                make_coffee(choice,coffee_type['ingredient'])