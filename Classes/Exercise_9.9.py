class Car:
    """A simple attempt to represent a car."""
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
 
    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()
 
    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it.")
 
    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
 
    def increment_odometer(self, miles):
        self.odometer_reading += miles


class Battery:
    """A simple attempt to model a battery for an electric car."""
    def __init__(self, battery_size=40):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size
        
    def describe_battery(self):
        """Print a statement describing the battery size."""
        print("This car has a " + str(self.battery_size) + "-kWh battery.")

    def upgrade_battery(self):
        """Will upgrade the battery from the default to 65"""
        if self.battery_size != 65:
            self.battery_size = 65

class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""
    def __init__(self, make, model, year):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car.
        """
        super().__init__(make, model, year)
        self.battery = Battery()
    
    def get_range(self):
        """Print a statement about the range this electric car provides."""
        if self.battery.battery_size == 40:
           range = 150
            # Add more elif conditions for other car models and their respective ranges
        elif self.battery.battery_size == 65:
            range = 250
            # Add more elif conditions for other car models and their respective ranges

        message = "This car can go approximately " + str(range)
        message += " miles on a full charge."
        print(message)


my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.get_range()
my_tesla.battery.upgrade_battery()
my_tesla.get_range()