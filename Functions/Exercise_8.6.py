def city_country(city, country = ''):
    "'Prints the city and its country'"
    country_city = f'"{city}, {country}"'
    return country_city.title()

Country_city = city_country('Mumbai', 'India')
print(Country_city)

print('Enter a city name and its country')
ci = input('City: ')
co = input('Country: ')
Country_city = city_country(ci, co)
print(Country_city)

print('Enter a city')
cit = input('City: ')
Country_city = city_country(cit)
print(Country_city)