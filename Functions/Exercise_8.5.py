def describe_country(city, country = 'USA'):
    "'Describe which city is in which country'"
    print(f'{city} is in {country}')

describe_country("Dallas")
describe_country(city = 'New York')
describe_country(city = 'Delhi', country = 'India')
describe_country(city = 'Mumbai', country = 'India')
