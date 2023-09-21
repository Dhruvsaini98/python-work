def sandwitch(*ingredients):
    print('The Sandwitch has been prepared with the following ingredients: ')
    for ingredient in ingredients:
        print(f'\t{ingredient}')

sandwitch('Cheese')
sandwitch('Cheese', 'Olives', 'Mayonnaise')

