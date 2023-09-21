favourite_numbers = {
    'dhruv' : [7, 16, 25],
    'mehul' : [4, 13, 22],
    'sarthak' : [69, 9, 8],
    'anuj' : [96, 10, 7],
    'kaustav' : [7, 45, 56],
    }

for name, numbers in favourite_numbers.items():
    print(f"{name.title()}'s favourite numbers are :")
    for number in numbers:
        print(f'\t{number}')
    print('\n')