class Restaurant:
    def __init__(self, restaurant_name, cuisine_type) -> None:
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.customers_served = 0   #default attribute

    def describe_restaurant(self):
        print(f"Name of the Restaurant: {self.restaurant_name}\nCuisine type: {self.cuisine_type}\nCustomers served = {self.customers_served}")

    def restaurant_open(self):
        print(f"\n{self.restaurant_name} is open!!")

    def update_served(self, number):
        self.customers_served = number

    def increment_served(self, number1):
        self.customers_served = self.customers_served + number1

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type="Ice Cream"):
        """Initializing attributes"""
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = []

    def icecream_flavors(self):
        """Printing the list of available ice creams"""
        print("\nWe have the following flavors available:")
        for flavor in self.flavors:
            print(f'- {flavor}')

icecream = IceCreamStand('Giani')
icecream.update_served(5)
icecream.increment_served(3)
icecream.describe_restaurant()
icecream.flavors = ['Chocoloate', 'Vanilla', 'Butterscotch', 'Strawberry']
icecream.icecream_flavors()
icecream.restaurant_open()


