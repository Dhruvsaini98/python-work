#Case sensitive program
users = ['dhRUv', 'anuj', 'SARTHAK', 'maNI', 'VipuL']
new_users = ['DHRUV', 'ANUJ', 'SARTHAK', 'MEHUL', 'MANT']

for new_user in new_users:
    if new_user in users:
        print(f'{new_user}, is not available for use')
    else:
        print(f'{new_user}, is available for use')
print('\n')

#Case insensitive program
current_users = ['dhRUv', 'anuj', 'SARTHAK', 'maNI', 'VipuL']
new_users = ['DHRUV', 'ANUJ', 'SARTHAK', 'MEHUL', 'MANT', 'vIPul']

current_users_lower = current_users[:]
for value in range(len(current_users_lower)):
    current_users_lower[value] = current_users_lower[value].lower()
print(current_users_lower)

for new_user in new_users:
    new_user_lower = new_user.lower()
    if new_user_lower in current_users_lower:
        print(f'{new_user}, is not available for use')
    else:
        print(f'{new_user}, is available for use')
