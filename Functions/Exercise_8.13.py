def build_profile(first, last, **additional):
    additional['First_name'] = first
    additional['Last_name'] = last
    return additional

user_profile = build_profile('Dhruv', 'Saini', Weight = '68', Height = '170cm', Hobbies = 'Reading')
print(user_profile)