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

def check_resources(order_ingredient):
    for item in order_ingredient:
        if order_ingredient[item]>resources[item]:
            print(f"sorry there is not enough {item}")
            return False
    return True 

def process_coin():
    print("please insert coins.")
    total = 0
    coin_five = int(input("How many 5kb coin?: "))
    coin_ten = int(input("How many 10kb coin?: "))
    coin_twenty = int(input("How many 20kb coin?: "))
    total = coin_five*5 + coin_ten*10 + coin_twenty*20
    return total

def is_payment_successful(money_recived, coffee_cost):
    if money_recived>=coffee_cost:
        global profit
        profit += coffee_cost
        change = money_recived-coffee_cost
        print(f"Here is your kb{change} in change.")
        return True
    else:
        print("Sorry that's not enough money. money refunded.")

def make_coffee(coffee_name, coffee_ingredient):
    for item in coffee_ingredient:
        resources[item] -= coffee_ingredient[item]
    print(f"Here is your {coffee_name} ....enjoy!!")
is_on=True
while is_on:
    choice = input("What would you like to have? (Latte/espresso/cappuccino): ")
    if choice == 'off':
        is_on=False
    elif choice == 'report':
        print(f"Water = {resources['water']}ml")
        print(f"Milk = {resources['milk']}ml")
        print(f"Coffee = {resources['coffee']}g")
        print(f"money = Kb{profit}")
    else:
        coffee_type  = menu[choice]
        print(coffee_type)
        if check_resources(coffee_type['ingredients']):
            payment = process_coin()
            if is_payment_successful(payment, coffee_type['cost']):
                make_coffee(choice, coffee_type['ingredients'])