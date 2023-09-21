car = 'sabaru'
print("Testing for car == 'sabaru")
print(car == 'sabaru')

num = 566
print(f'\n{num == 567}')
print(f'{num == 566}')
print(f'{num > 600}')
print(f'{num < 600}')
print(f'{num >= 600}')
print(f'{num <= 600}')

car1 = 'mercedes'
model = 'c class'
print(f"\n{car1 == 'mercedes' and model == 'c class'}")
print(f"{car1 == 'mercedes' and model == 'r 8'}")

num1 = 567
num2 = 234
print(f"\n{num1 == 567 or num2 == 23}")
print(f"{num1 == 567 or num2 == 234}")

cars = ['mercedes', 'lambo', 'sabaru', 'bmw', 'toyota']
value = 'bmw'
if value in cars:
    print(f"\nI own a {value.title()}")
else:
    print(f"\nI do not own a {value.title()}")

cars = ['mercedes', 'lambo', 'sabaru', 'bmw', 'toyota']
value = 'audi'
if value not in cars:
    print(f"\nI do not own an {value.title()}")



