class Restaurant:
    def __init__(self, restaurant_name, cuisine_type) -> None:
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.customers_served = 0   #default attribute

    def describe_restaurant(self):
        print(f"Name of the Restaurant: {self.restaurant_name}\nCuisine type: {self.cuisine_type}\nCustomers served = {self.customers_served}")

    def restaurant_open(self):
        print(f"{self.restaurant_name} is open!!")

    def update_served(self, number):
        self.customers_served = number

    def increment_served(self, number1):
        self.customers_served = self.customers_served + number1

my_restaurant = Restaurant("Barbeque Nation", "Indian")

my_restaurant.describe_restaurant()
my_restaurant.restaurant_open()
my_restaurant.customers_served = 10
my_restaurant.describe_restaurant()

my_restaurant.update_served(20)
my_restaurant.describe_restaurant()

my_restaurant.increment_served(10)
my_restaurant.describe_restaurant()






