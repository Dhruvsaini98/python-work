usernames = []
if usernames:
    for username in usernames:
        if username == 'admin':
            print(f'Hello {username}, would you like to see the messages?')
        else:
            print(f'Hello {username}, thanks for logging in')
else:
    print('List of users is empty')