dhruv = {
    'first_name' : 'Dhruv',
    'last_name' : 'Saini',
    'age' : 24,
    'height' : 1.7,
    'hobbies' : 'Reading, watching, playing',
    'strenghts' : 'detail oriented',
    'weaknesses' : 'overthinker',
    'skills' : 'C, C++, Python',
}

sarthak = {
    'first_name' : 'Sarthak',
    'last_name' : 'Kaushik',
    'age' : 24,
    'height' : 1.8,
    'hobbies' : 'Reading, watching, playing',
    'strenghts' : 'detail oriented',
    'weaknesses' : 'overthinker',
    'skills' : 'C, C++, Python',
}

anuj = {
    'first_name' : 'Anuj',
    'last_name' : 'Gupta',
    'age' : 24,
    'height' : 1.65,
    'hobbies' : 'Reading, watching, playing',
    'strenghts' : 'detail oriented',
    'weaknesses' : 'overthinker',
    'skills' : 'C, C++, Python',
}

peoples = [dhruv, sarthak, anuj]

for people in peoples:
    for key, value in people.items():
        print(f'{key.title()} : {value}')
    print('\n')









#if key == 'first_name':
#    print('\n')
#    print(f'{key.title()} : {value}')
#else:
#    print(f'{key.title()} : {value}')
        


