num = input("Enter a number and I'll check whether it is a multiple of 10 or not: ")
num = int(num)
if num % 10 == 0:
    print(f'{num} is a multiple of 10')
else:
    print(f'{num} is not a multiple of 10')