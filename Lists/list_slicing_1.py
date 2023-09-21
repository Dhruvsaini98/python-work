my_pizzas = ['country first', 'chicken', 'paneer', 'double cheese', 'margherita']
friend_pizzas = my_pizzas[:]

my_pizzas.append('peproni')
friend_pizzas.append('mutton')

print("My favourite pizzas are:")
for pizza in my_pizzas[0:]:
 print(pizza.title())

print("\nMy Friend's favourite pizzas are:")
for pizza in friend_pizzas[0:]:
 print(pizza.title())