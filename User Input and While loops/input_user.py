people = input('How many peolple are there in your dinner group? ')
people = int(people)
if people > 8:
    print('You will have to wait because the seating capacity is of 8 only')
else:
    print(f'{people} is adjustable. Please have a seat')
