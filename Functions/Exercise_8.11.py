def print_messages(list_messages, sent_messages):
    while list_messages:
        message = list_messages.pop()
        print(f'Message: {message}')
        sent_messages.append(message)

def show_messages(sent_messages):
    print('\nThe following messages have been printed: ')
    for messag in sent_messages:
        print(f'{messag}')


list_messages = ['Hello', 'Bye', 'Goodnight', 'Goodmorning']
sent_messages = []
print_messages(list_messages[:], sent_messages)
show_messages(sent_messages)
sent_messages.reverse()
print(sent_messages)
print(list_messages)