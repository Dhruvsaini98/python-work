tommy = {
    'name' : 'tommy',
    'animal_type' : 'dog',
    'owner' : 'dhruv',
}

simba = {
    'name' : 'simba',
    'animal_type' : 'lion',
    'owner' : 'mufasa',
}

ginger = {
    'name' : 'ginger',
    'animal_type' : 'cat',
    'owner' : 'blitz',
}

pets = [tommy, simba, ginger]

for pet in pets:
    for key, value in pet.items():
        print(f'{key.title()} : {value.title()}')
    print('\n')