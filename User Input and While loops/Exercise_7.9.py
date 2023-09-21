sandwitch_orders = ['Cheese Sandwitch', 'Pastrami', 'Chicken Sandwitch', 'Tuna Sandwitch','Pastrami', 'Pork Sandwitch','Pastrami']
finished_sandwitches = []
print('Restaurant has run out of Pastrami')
while sandwitch_orders:
    

    if  'Pastrami' in sandwitch_orders:
        sandwitch_orders.remove('Pastrami')
    
    else:
        sandwitch = sandwitch_orders.pop()
        print(f'\nYour {sandwitch} is ready!')
        
        finished_sandwitches.append(sandwitch)

print(f'\nSandwitches prepared : {finished_sandwitches}')