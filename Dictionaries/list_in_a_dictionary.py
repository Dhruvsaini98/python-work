favourite_lanuages = {
    'mehul' : ['python','c','ruby'],
    'sarthak' : ['C'],
    'anuj' : ['C++', 'scala'],
    'mani' : ['java', 'python'],
    'pallav' : ['ruby', 'r language'],
    'dhruv' : ['python'],
    'harsh' : ['java'],

}

for name, languages in favourite_lanuages.items():
    if len(languages) == 1:
        print(f"\n{name.title()}'s favourite language is: ")
    else:
        print(f"\n{name.title()}'s favourite languages are: ")
   
    for language in languages:
        print(f'\t{language.title()}')