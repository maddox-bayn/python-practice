def make_pizza(size, *toppings):
    """"summerize pizza we are about to makre"""
    print(f"making a {size} inch pizza with the following toppings: ")
    for topping in toppings:
            print(topping)
make_pizza(15, 'pepperoni', 'green peppers')
