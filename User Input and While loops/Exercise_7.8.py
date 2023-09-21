sandwitch_orders = ['Cheese Sandwitch', 'Chicken Sandwitch', 'Tuna Sandwitch', 'Pork Sandwitch']
finished_sandwitches = []

while sandwitch_orders:
    sandwitch = sandwitch_orders.pop()
    print(f'Your {sandwitch} is ready!')
    print('\n')
    finished_sandwitches.append(sandwitch)

print(f'\nSandwitches prepared : {finished_sandwitches}')

