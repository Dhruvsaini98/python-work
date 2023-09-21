from restaurant import Restaurant, IceCreamStand

icecream = IceCreamStand('Giani')
icecream.update_served(5)
icecream.increment_served(3)
icecream.describe_restaurant()
icecream.flavors = ['Chocoloate', 'Vanilla', 'Butterscotch', 'Strawberry']
icecream.icecream_flavors()
icecream.restaurant_open()

barbeque = Restaurant('Barbeque Nation', 'Indian')
barbeque.update_served(5)
barbeque.increment_served(3)


barbeque.describe_restaurant()
barbeque.restaurant_open()