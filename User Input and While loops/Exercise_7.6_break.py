prompt = '\nEnter the toppings you want in your Pizza'
prompt += '\nEnter "quit" once you are done with your toppings: '

while True:
    topping = input(prompt)
    
    if topping == 'quit':
        print('Your Pizza will be ready in 30 mins')
        break
    else:
        print(f"{topping} will be added to your pizza")
    