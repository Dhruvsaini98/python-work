favourite_places = {
    'dhruv' : ['new york', 'london', 'melbourne'],
    'mani' : ['london', 'paris', 'helsenki'],
    'anuj' : ['noida', 'delhi', 'tokyo'],

}

for name, places in favourite_places.items():
    print(f"{name.title()}'s favourite places are :")
    for place in places:
        print(f'\t{place.title()}')
    print('\n')