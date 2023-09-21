# Exercise 3-4
invitees = ['bill gates', 'albert', 'newton']
print(f"{invitees[0].title()}, you have been invited to the Party")
print(f"{invitees[1].title()}, you have been invited to the Party")
print(f"{invitees[2].title()}, you have been invited to the Party")
print(f"Number of people being invited - {len(invitees)}")

# Exercise 3-5 
print(f"\n{invitees[0].title()} can't make it")
del invitees[0]
new_invitee = invitees.insert(0, 'elon musk')
print(f"\n{invitees[0].title()}, you have been invited to the Party")
print(f"{invitees[1].title()}, I hope you are still coming to the Party?")
print(f"{invitees[2].title()}, I hope you are still coming to the Party?")
print(f"Number of people being invited - {len(invitees)}")

# Exercise 3-6
print(f"\nGuys, I have found a bigger table. I'll invite more people")
invitees.insert(0, 'nikola tesla')
invitees.insert(2, 'hitler')
invitees.append("oppenheimer")
print(f"\n{invitees[0].title()}, you have been invited to the party")
print(f"{invitees[1].title()}, I hope you are still coming to the Party?")
print(f"{invitees[2].title()}, you have been invited to the party")
print(f"{invitees[3].title()}, I hope you are still coming to the Party?")
print(f"{invitees[4].title()}, I hope you are still coming to the Party?")
print(f"{invitees[5].title()}, you have been invited to the Party")
print(f"Number of people being invited - {len(invitees)}")

# Exercise 3-7
print(f"\nGuys bad news, the table won't arrive on time. I can only invite two people now.")
invitee_0 = invitees.pop(0)
invitee_1 = invitees.pop(0)
invitee_2 = invitees.pop(0)
invitee_3 = invitees.pop(0)
print(f"\n{invitee_0.title()}, you are not invited anymore. Sorry about this")
print(f"{invitee_1.title()}, you are not invited anymore. Sorry about this")
print(f"{invitee_2.title()}, you are not invited anymore. Sorry about this")
print(f"{invitee_3.title()}, you are not invited anymore. Sorry about this")
print(f"{invitees[0].title()}, you are still invited")
print(f"{invitees[1].title()}, you are still invited")
print(f"Number of people being invited - {len(invitees)}")
del invitees[0]
del invitees[0]
print(invitees)
