class Restaurant:
    def __init__(self, restaurant_name, cuisine_type) -> None:
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"Name of the Restaurant: {self.restaurant_name}\nCuisine type: {self.cuisine_type}")
        print("\n")
    def restaurant_open(self):
        print(f"{self.restaurant_name} is open!!")

my_restaurant = Restaurant("Barbeque Nation", "Indian")
my_restaurant.describe_restaurant()


your_restaurant = Restaurant("Golden Dragon", "Chinese")
your_restaurant.describe_restaurant()

his_restaurant = Restaurant("Dominoes", "Italian")
his_restaurant.describe_restaurant()

her_restaurant = Restaurant("Mcdonalds", "American")
her_restaurant.describe_restaurant()


