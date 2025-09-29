# count ofeven and odd
def count_even_odd(number):
    even_number = 0 
    odd_number = 0
    for num in number:
        if num % 2 == 0:
            even_number += 1
        else:
            odd_number += 1
    return even_number, odd_number
numbers = [1, 2, 3, 4, 5, 6, 7]
even_number, odd_number = count_even_odd(numbers)             
print(f"even count: {even_number} odd count: {odd_number}")

fruits = ["Mango", "Apple", "Orange", "Gova", "Mellon",]
for elem in ["Banana"]:
    new_fruit = (f"add {elem} to the list")
    fruits.append(new_fruit)
    new_fruit = fruits
    print(new_fruit)

for num in range(1, 101):
    if num % 3 == 0 and num % 5 == 0:
        print("Fussuss")
    elif num % 3 == 0: 
        print("Fuss")
    elif num % 5 == 0:
        print("Buss")
    else:
        print(num)

user_input = int(("Enter your I number: "))
if user_input % 2 == 0:
    print("even number: ")
else:
    print("odd number: ")

    def count_vowel_and_consinant(input_string):
    vowels = "aeiouAEIOU"
    vowei_count = 0
    consonant_count = 0
    for latter in input_string:
        if latter in vowels:
            vowei_count += 1
        else:
            consonant_count += 1
    return vowei_count, consonant_count
user_input = input("Enter your string")
vowels, consonsnts = count_vowel_and_consinant(user_input)
print(f"number of vowel: {vowels}")
print(f"number of consonant: {consonsnts}")

dic = {"name":"Maddox", "age":"19","city":"califonia"}
print(dic["age"])
print(dic["city"])
print(dic["name"])

def divide_number(number, divisor):
    results = []
    try:
        result = number / divisor
        results.append(result)
    except ZeroDivisionError:
        results.append("cannot divide by zero")
    return results 
number = 10
divisor = 0
print(divide_number(number, divisor))

def divide_number(numbers, divisor):
    results = []
    try:
        for num in numbers:
            result = num / divisor
            results.append(result)
    except ZeroDivisionError:
        results.append("can't divide by zero")
    except TypeError:
        results.append("invalid type, number expected")
    return results
numbers = [10, 20, 15, 25, 80, 54]
divisor = 2
print(divide_number(numbers, divisor))

def reverse_string(string):
    try:
        word = list(string)
        word.reverse()
    except ValueError:
        if string is not str(print("error, non string inputs"))
    return word
inpute = "communication"
print(reverse_string(inpute)
      
def reverse_string(string_input):
    if not isinstance(string_input, str):
        raise ValueError("enter must be a string")
    return string_input[::-1]
try:
    result = reverse_string("Hello , word")
    print(result)
except ValueError as e:
    print(e)

fruits = ["Mango", "Apple", "Orange", "Gova", "Mellon",]

def add_fruit(fruit_list):
    new_fruit = input("Enter a new fruit to add to the list: ")
    fruit_list.append(new_fruit)
    print("friut added successfully!")
def print_fruits(fruit_list):
    print("\nUpdated list of fruits:")
    for fruit in fruit_list:
        print(fruit)
if __name__ == "_main_":
    add_fruit(fruits)
    print_fruits(fruits)

fruits = ["Mango", "Apple", "Orange", "Gova", "Mellon",]
print(fruits)
new_fruit = input("add new fruit to the list: ")
fruits.append(new_fruit)
print(fruits)

def calculate_average():
    try:
        # user input
        user_input = [2, 3, 4, 5, 6, 7, 8]
        # split the input_string into a list of string and convert to integer
        number = list(map(int, user_input.split()))
        if not number:
            raise ValueError("list must not be empty")
        average = sum(number) / len(number)
        print(f"the average of the entered number is: {average:.2f}")
    except ValueError as e:
        print(f"valueerror: {e}")
    except Exception as e:
        print(f"an error occurred: {e}")
calculate_average() 
# REVISION ON DICTIONARY
favourite_languager ={
    "jen": "python",
    "maddox": "c",
    "sheddy": "ruby",
    "elite": "python",
}
for name in sorted(favourite_languager.keys()):
    print(f"{name.title()}, Thank you for talking the poll.")
print("the following language has been mentioned")
for language in set(favourite_languager.values()):
    print(language) 
 
pizza = {
    'crust': 'tick',
    'topping': ['mushrooms', 'estral chese'],
}
print(f"you ordered a {pizza['crust']}-crust pizza with thefollowing topping:")
for toppin in pizza['topping']:
    print(f"\t{toppin}") 

favourite_languager ={
    "jen": "python",
    "maddox": "c",
    "sheddy": "ruby",
    "elite": "python",
}
for key, value in favourite_languager.items():
    print(f"{key.title()} : {value}")

Users = {
    'Maddox': {
        'first': 'maddox',
        'last': 'bayn',
        'location': 'califonia',
    },
    'Raddox': { 
 q       'first': 'raddox',
        'last': 'wayn',
        'location': 'denmack'
    },
}
for username, user_info in Users.items():
    print(f"\nuser_name: {username}")
    full_name = f"{user_info['first']} {user_info['last']}"
    location = user_info['location']
    print(f"\t full name: {full_name.title()}")
    print(f"\t location: {location.title()}")

person_0 = {'first_name': 'maddox', 'last_name': 'bayn', 'age': 19, 'city': 'califonia'}
person_1 = {'first_name': 'raddox', 'last_name': 'wayn', 'age': 18, 'city': 'denmark'}
pperson_2 = {'first_name':'john', 'last_name': 'johnson', 'age': 24, 'city': 'new york'}
people = [person_0, person_1, pperson_2]
for person in people:
    for k, v, in person.items():
        print(f"{k}, {v}")
    print("\n")    

favourite_number = {
    'peter': [3, 7],
    'maddox': [2, 0],
    'logan': [3, 5, 8],
}
for name, number in favourite_number.items():
    print(f"{name.title()}'s favourite numbers are:")
    for num in number:
        print(f"{num}")
    print('\n')

height = input("How tall are you, in inches?")
height = int(height)
if height >= 48:
     print("\nyou are tall enough to ride!")
else:
    print("\nyou will be able to ride when are older")
promt = "if you tell us who you are we can pesonalze the messages you see"
promt += "\n what is your fist name? "

name = input(promt)
print(f"hello, {name}! ")

# while loop
current_numnber = 1
while current_numnber <= 5:
    print(current_numnber)
    current_numnber += 1

promt = "\ntell me something and i will repeat it back to you"
promt += "\nEnter 'quit' to end the program. "
message =  ""
while message != 'quit':
    message = input(promt)
    if message != 'quit':
        print(message)

promt = "\ntell me something and i will repeat it back to you"
promt += "\nEnter 'quit' to end the program. "
active = True
while active:
    message = input(promt)
    if  message == 'quit':
        active = False
    else:
        print(message)
promt = "\ntell me something and i will repeat it back to you"
promt += "\nEnter 'quit' to end the program. "
active = True
while active:
    message = input(promt)
    if  message == 'quit':
        active = False
    else:
        print(message)
promt = "\ntell me something and i will repeat it back to you"
promt += "\nEnter 'quit' to end the program. "
active = True
while active:
    message = input(promt)
    if  message == 'quit':
        active = False
    else:
        print(message)
promt = "\ntell me something and i will repeat it back to you"
promt += "\nEnter 'quit' to end the program. "
active = True
while active:
    message = input(promt)
    if  message == 'quit':
        active = False
    else:
        print(message)
promt = "\ntell me something and i will repeat it back to you"
promt += "\nEnter 'quit' to end the program. "
active = True
while active:
    message = input(promt)
    if  message == 'quit':
        active = False
    else:
        print(message)
promt = "\ntell me something and i will repeat it back to you"
promt += "\nEnter 'quit' to end the program. "
active = True
while active:
    message = input(promt)
    if  message == 'quit':
        active = False
    else:
        print(message)
promt = "\ntell me something and i will repeat it back to you"
promt += "\nEnter 'quit' to end the program. "
active = True
while active:
    message = input(promt)
    if  message == 'quit':
        active = False
    else:
        print(message)
promt = "\ntell me something and i will repeat it back to you"
promt += "\nEnter 'quit' to end the program. "
active = True
while active:
    message = input(promt)
    if  message == 'quit':
        active = False
    else:
        print(message)
promt = "\ntell me something and i will repeat it back to you"
promt += "\nEnter 'quit' to end the program. "
active = True
while active:
    message = input(promt)
    if  message == 'quit':
        active = False
    else:
        print(message)
promt = "\ntell me something and i will repeat it back to you"
promt += "\nEnter 'quit' to end the program. "
active = True
while active:
    message = input(promt)
    if  message == 'quit':
        active = False
    else:
        print(message)
promt = "\ntell me something and i will repeat it back to you"
promt += "\nEnter 'quit' to end the program. "
active = True
while active:
    message = input(promt)
    if  message == 'quit':
        active = False
    else:
        print(message)
promt = "\ntell me something and i will repeat it back to you"
promt += "\nEnter 'quit' to end the program. "
active = True
while active:
    message = input(promt)
    if  message == 'quit':
        active = False
    else:
        print(message)
promt = "\ntell me something and i will repeat it back to you"
promt += "\nEnter 'quit' to end the program. "
active = True
while active:
    message = input(promt)
    if  message == 'quit':
        active = False
    else:
        print(message)
promt = "\ntell me something and i will repeat it back to you"
promt += "\nEnter 'quit' to end the program. "
active = True
while active:
    message = input(promt)
    if  message == 'quit':
        active = False
    else:
        print(message)
promt = "\ntell me something and i will repeat it back to you"
promt += "\nEnter 'quit' to end the program. "
active = True
while active:
    message = input(promt)
    if  message == 'quit':
        active = False
    else:
        print(message)
promt = "\ntell me something and i will repeat it back to you"

promt = "\nplease enter the name of a city you  have visited"
promt += "\nente quit when you have finished.) "
while True:
    city = input(promt)
    if city == 'quit':
        break
    else:
        print(f"i had loved to go to {city.title()}! ")

promt = "which pizza tooping would you like"
promt += "(type 'quit' to stop adding topping)"

while True:
    topping = input(promt)
    if topping == 'quit':
        break
    else:
        print(f"Adding {topping} t you pizza")

promt = "\nhow old are you?"
promt += "\ntype quit to stop.)"
while True:
    age = input(promt)
    if age == 'quit':
        break
    else:
        age = int(age)
        if age < 3:
            price = 0
        elif age < 13:
            price = 10
        else:
            price = 15
        print(f"\nthe ticket price is {price}. ")

unconfirmed_user = ['alice', 'bain', 'candace']
confirmed_users = []
while unconfirmed_user:
    current_user = unconfirmed_user.pop()
    print(f"verifying user: {current_user.title()}") 
    confirmed_users.append(current_user)
print("\nthe following uses have beeen confirmed: ")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())

pets = ['dog', 'goat', 'cat', 'rat', 'cat', 'rabbit', 'cat']
print(pets)
while 'cat'in pets:
    pets.remove('cat')
print(pets)

responses = {}
polling_acitve = True
while polling_acitve:
    name =  input("\n What is your name? ")
    response = input("which mountain would you like to go? ")
    responses[name] = response
    repeat = input('would you want another person to repeat?')
    if repeat == 'no':
        polling_acitve = False
print("\n_____pollin result______")
for name, response in responses.items():
    print(f"{name} wouold you like to go to mount {response}")

sandwich_order = [ 'tuna', 'chicken', 'pastrani']
finished_sandwiches = []
while sandwich_order:
    sandwich = sandwich_order.pop()
    print(f"i made your {sandwich} sandwich.")
    finished_sandwiches.append(sandwich)
print("_______finishd sandwiches_____")
for sandwich in finished_sandwiches:
    print(f"we made a {sandwich} sandwich.")

def favourite_book(books):
    """"finding favourite book"""
    print(f"my favourite book is {books.title()}")
favourite_book('alice in the wonder land')

# funtio of a formatted name
def get_formatted_name(first_nmae, last_name):
    """get full name, neatly arrenged"""
    full_name = f"{first_nmae} {last_name}"
    return full_name

while True:
    print("\ntell me your name")
    print("use q to quit information info")
    f_name = input("your first name: ")
    if f_name == 'q':
        break
    l_name = input("your last name: ")
    if l_name == 'q':
        break
    full_n= get_formatted_name(f_name, l_name)
    print(f"\nHello: {full_n}")

# fution that get artist album
def make_abum(artist, tittle, song=None):
    album = {'artist': artist, 'tittle': tittle, 'songs': song}
    return album

while True:
    print("\nEnter album information.")
    print("(Enter q at any time to quit.)")

    artists = input("Artist name: ")
    if artists == 'q':
        break
    title = input("Title name: ")
    if title == 'q':
        break
    song = input("Song number (optional): ")
    if song == 'q':
        break
    Album_info = make_abum(artists, title, song)
    print(Album_info)


def print_model(unprinted_designs, completed_designs):
    while unprinted_designs:   
        current_design = unprinted_designs.pop()
        print(f"printing model: {current_design}")
        completed_designs.append(current_design)

def show_completed_model(completed_designs):
    print("\nThe following models have been printed:")
    for design in completed_designs:
        print(design)

unprinted_designs = ['phone casse', 'robot pendant', 'dodechendron']
completed_designs = [] 

print_model(unprinted_designs[:], completed_designs)
show_completed_model(completed_designs)

print(unprinted_designs)
print(completed_designs)

# message function

def show_messages(messages):
    for message in messages:
        print(message)                                                                                   
#show_messages(messages)

def send_messages(messages, send_message):
    while messages:
        message = messages.pop()
        print(message)
        send_message.append(message)
l_message = ['Hi', 'How are yoe', 'wo the hell are you', 'your Father', 'what?']
send_message = []

send_messages(l_message, send_message)
print(l_message)
print(send_message)