class Intructor:
    followes = 0
    def __init__(self, name, address) -> None:
        self.name = name
        self.address = address
        #self.followes = 0
    def display(self, teach):
        print(f"hi, i am jeeny {self.name} and i teach {teach}")
    def update_followers(self, follower_name):
        self.followes += 1

intructor_1 = Intructor('maddox', 34)
print(intructor_1.name)
#print(intructor_1.address)
intructor_1.display('python')
intructor_1.update_followers("wayn")
print(intructor_1.followes)
intructor_2 = Intructor('wayn', 'dehli')
#    print(intructor_2.name)
#   print(intructor_2.address) 
intructor_2.update_followers('maddos')
print(intructor_2.followes)

class Restaurant:
    def __init__(self, restaurant_name, cousine_type) -> None:
        self.restaurant_name = restaurant_name
        self.cousine_type = cousine_type
    def about_restaurant(self):
        print(f"The name of the restaurant is {self.restaurant_name}")
        print(f"Their cousine type is {self.cousine_type}")
    def close_open(self):
        print(f"The {self.restaurant_name} is now open")

restaurant_1 = Restaurant('Maddichef', 'African')
restaurant_2 = Restaurant('Roitibe', 'Spanish')
restaurant_3 = Restaurant('Melic', 'English')

restaurant_1.about_restaurant()
print('--------')
restaurant_1.close_open()
print('--------')
restaurant_2.about_restaurant() 
print('--------') 
restaurant_3.about_restaurant()   

class BankAccount:
    def __init__(self, owner, balance) -> None:
        self.owner = owner
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
        print(f"yor {amount} deposit was successful your balance is {self.balance}")      
    def withdrawal(self, amount):
        if amount > self.balance:
            print("check our balance! insurficient funds") 
        else:
            self.balance -= amount
            print(f"your remaining balance is{self.balance}  ")
acount_1 = BankAccount("Maddox", 10000)
acount_1.deposit(30000)
acount_1.withdrawal(20000)
acount_1.withdrawal(40000)

class User:
    def __init__(self,first_name, last_name,location, age) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.location = location
        self.age = age
    def decrib_user(self):
        print(f"my full name is {self.first_name} {self.last_name} from {self.location} and {self.age} years of age")
    def greetuser(self):
        print(f"hello {self.first_name} {self.last_name}")

user1 = User('Maddox', 'Bayn', 'Nigeria', 19)
user2 = User('Ene', 'Awesome','Canada',24)
user3 = User('Elit', 'mega', 'Nigeria', 18)
user1.decrib_user()
user1.greetuser()
print('----------')
user2.decrib_user()
user2.greetuser()
print("----------")
user3.decrib_user()
user3.greetuser()

class Human:
    def __init__(self, heat) -> None:
        self.eyes=2
        self.nose=1
        self.heart=heat
    def eat(self):
        print("i can eat")
    def walk(self):
        print("i can walk")
class Male(Human):
    def __init__(self, name, heart) -> None:
        self.name = name
        super().__init__(heart)
    def flirt(self):
        print("i can flirt")
    def walk(self):
        print("i can rub")
        return super().walk()
    def display(self):   
        print(f"i am {self.name} i have {self.eyes} eyes, {self.nose} nose and {self.heart} heart")
    
Male_1=Male('maddox', 1)
#Male_1.eat()
#Male_1.flirt()
#Male_1.walk()
print(Male_1.nose)
print(Male_1.name)
Male_1.display()


class Restaurant:
    def __init__(self, restaurant_name, cousine_type) -> None:
        self.restaurant_name = restaurant_name
        self.cousine_type = cousine_type
    def about_restaurant(self):
        print(f"The name of the restaurant is {self.restaurant_name}")
        print(f"Their cousine type is {self.cousine_type}")
    def close_open(self):
        print(f"The {self.restaurant_name} is now open")

class IceCreanStand(Restaurant):
    def __init__(self, restaurant_name, cousine_type, flavours) -> None:
        super().__init__(restaurant_name, cousine_type)
        self.flavours = flavours

    def display_flavour(self):
        print("the flavour are:")
        for flavour in self.flavours:
            print(f" -{flavour}")
icescreamstand=IceCreanStand('choco','milo', ['milk','choco'])
icescreamstand.display_flavour()

class User:
    def __init__(self,first_name, last_name,location, age) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.location = location
        self.age = age
    def decrib_user(self):
        print(f"my full name is {self.first_name} {self.last_name} from {self.location} and {self.age} years of age")
    def greetuser(self):
        print(f"hello {self.first_name} {self.last_name}")

class Privilages:
    def __init__(self, privilages) -> None:
        self.privilages=privilages
        
    def show_privilage(self):
        print("Privilages: ")
        for privilage in self.privilages:
            print(f"-{privilage}")
        
class Admin(User):
    def __init__(self, first_name, last_name, location, age, privilages) -> None:
        super().__init__(first_name, last_name, location, age)
        self.first_name = first_name
        self.last_name = last_name
        self.location = location
        self.age = age
        self.privilages= privilages(privilages)
   
admin_1=Admin('Maddox', 'Bayn', 'USA', 23, ['can delet', 'can add ads', 'can remove ads', 'can display info' ])
admin_1.privilages.show_privilage()

from random import randint

class Die:
    def __init__(self, sides=6) -> None:
        self.sides=sides
    def roll_die(self):
        print(randint(1, self.sides))
die = Die(6)
for _ in range(0, 10):
    die.roll_die()
