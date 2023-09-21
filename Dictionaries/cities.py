cities = {
    'delhi' : {
        'country' : 'india',
        'population' : '2m',
        'fact' : 'Capital of india',
    },
    'new york' : {
        'country' : 'the usa',
        'population' : '1m',
        'fact' : 'A city that never sleeps',
    },
    'london' : {
        'country' : 'the uk',
        'population' : '1m',
        'fact' : 'Capital of the uk',
    },
}

for city, infomation in cities.items():
    print(f'{city.title()} :')
    for key, value in infomation.items():
        if value == 'the usa':
        
            print(f'\t{key.title()} : {value[:1].upper() + value[1:4].lower() + value[4:5].upper() + value[5:].upper()}')
        elif value == 'the uk':
            print(f'\t{key.title()} : {value[:1].upper() + value[1:4].lower() + value[4:5].upper() + value[5:].upper()}')
        elif value == 'Capital of the uk':
            words = value.split()
            last_word = words[-1]
            changed_last_word = last_word.upper()
            words[-1] = changed_last_word
            converted_string = ' '.join(words)
            print(f'\t{key.title()} : {converted_string}')
        else: 
            print(f'\t{key.title()} : {value.title()}')
    print('\n')
        