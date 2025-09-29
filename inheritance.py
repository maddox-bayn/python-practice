class Car:
    def __init__(self, make, model, year) -> None:
        self.make=make
        self.model=model
        self.year=year
        self.odometer_reading=0
    def get_descriptive_name(self):
        long_name=f"{self.year} {self.make} {self.model}"
        return long_name.title()
    def read_odometer(self):
        print(f"the car has {self.odometer_reading} miles on it")
    def update_odometer(self, millage):
        if millage >= self.odometer_reading:
            self.odometer_reading = millage
        else:
            print("you can't roll back the odometer!")
    def increment_odometer(self, mile):
        self.odometer_reading += mile
class Battery:
    def __init__(self, battery_size=75) -> None:
        self.battery=battery_size
    def describ_battery(self):
        print(f"this car has a {self.battery}-kwh battery")
    def get_battery(self):
        if self.battery ==75:
            range =260
        elif self.battery == 150:
            range =315
        print(f"the car can go about {range} miles on full speed")

    def upgrade_battery(self):
        if self.battery != 100:
           self.battery  = 150
class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery=Battery()
    def describ_battery(self):
        print(f"this car has a {self.battery}-kwh battery.")
    def fill_gas_tank(self):
        print("this car dosen't need gas tank")

my_tesla=ElectricCar('tesla','model', 2029)
my_tesla.battery.describ_battery()
my_tesla.battery.get_battery()
my_tesla.battery.upgrade_battery()
my_tesla.battery.get_battery n 