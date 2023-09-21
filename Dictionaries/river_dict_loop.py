country_rivers = {
    'india' : 'ganga',
    'brazil' : 'amazon',
    'egypt' : 'nile',
}

for country, river in country_rivers.items():
    print(f'The {river.title()} flows through {country.title()}')

print('\n')

for country in country_rivers.keys():
    print(f'{country.title()}')

print('\n')

for river in country_rivers.values():
    print(f'{river.title()}')