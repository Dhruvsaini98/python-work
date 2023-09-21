prompt = '\nYour age will determine the price of your movie ticket'
prompt += '\nEnter your age: '

age = 1
while age:
    age = input(prompt)
    age = int(age)
    
    if age < 3:
        print("Your ticket is free")
    elif age < 12:
        print("Your ticket price is $10")
    else:
        print("Your ticket price is $15")