class Restaurant:
    def __init__(self, restaurant_name, cuisine_type) -> None:
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"Name of the Restaurant: {self.restaurant_name}\nCuisine type: {self.cuisine_type}")

    def restaurant_open(self):
        print(f"{self.restaurant_name} is open!!")

my_restaurant = Restaurant("Barbeque Nation", "Indian")
print(my_restaurant.restaurant_name)
print(my_restaurant.cuisine_type)
my_restaurant.describe_restaurant()
my_restaurant.restaurant_open()

your_restaurant = Restaurant("Golden Dragon", "Chinese")
print(your_restaurant.restaurant_name)
print(your_restaurant.cuisine_type)
your_restaurant.describe_restaurant()
your_restaurant.restaurant_open()