people_who_should_poll = ['dhruv', 'mehul', 'sarthak', 'anuj', 'harsh', 'kaustav', 'mani', 'karun', 'pallav']
people_who_polled = {
    'mehul' : 'python',
    'sarthak' : 'C',
    'anuj' : 'C++',
    'mani' : 'java',
    'pallav' : 'ruby',
    'dhruv' : 'python',
    'harsh' : 'java',

}

for name in sorted(people_who_should_poll, reverse = True):
    if name in people_who_polled:
        print(f'{name.title()} thanks for your response')
    else:
        print(f'{name.title()} please complete your poll')

print('\n')

for value in sorted(set(people_who_polled.values()), reverse = True):
    print(value.title())