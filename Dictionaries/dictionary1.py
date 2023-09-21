favourite_numbers = {
    'Dhruv' : 7,
    'Mehul' : 4,
    'Sarthak' : 69,
    'Anuj' : 96,
    'Kaustav' : 7,
    }

favourite_number = favourite_numbers['Sarthak']
print(favourite_number)

favourite_numbers['Kaustav'] = 8
print(f"{favourite_numbers['Kaustav']}")

del favourite_numbers['Mehul']
print(favourite_numbers)