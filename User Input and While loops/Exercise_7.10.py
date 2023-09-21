response = {}
poll_active = True
while poll_active:
    name = input("Enter yor name: ")
    place = input("If you could visit anywhere in the whole world, where would you visit? ")
    response[name] = place

    conti = input("\nDo you want others to poll? (y/n)")
    if conti == 'n':
        poll_active = False
    else:
        poll_active = True

print("\nPoll results: ")
for names, answers in response.items():
    print(f'{names.title()} would like to visit {answers.title()}') 
