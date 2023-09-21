prompt = '\nEnter the toppings you want in your Pizza'
prompt += '\nEnter "quit" once you are done with your toppings: '

active = True
while active:
    topping = input(prompt)
    
    if topping == 'quit':
        print('Your Pizza will be ready in 30 mins')
        active = False
    else:
        print(f"{topping} will be added to your pizza")




    