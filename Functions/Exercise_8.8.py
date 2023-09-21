def make_album(singer, album):
    "'Makes dictionaries of the singer and the album'"
    dict1 = {'Name' : singer, 'Album_Name' : album}

    #sing_alb = f'Name: {dict1["Name"]}, Album: {dict1["Album_Name"]}' 
    return dict1 

while True:
    print('Enter a singer name and his/her album')
    print('Enter q to quit')

    sin = input('Singer: ')
    if sin == 'q':
        break

    alb = input('Album: ')
    if alb == 'q':
        break

    singer_album = make_album(sin, alb)
    print(singer_album)


#print('Enter a singer name and his/her album')
#sin = input('Singer: ')
#alb = input('Album: ')

#singer_album = make_album(sin, alb)
#print(singer_album)