def make_album(singer, album, songs = None):
    "'Makes dictionaries of the singer and the album'"
    dict1 = {'Name' : singer, 'Album_Name' : album}
    if songs:
        dict1['Songs_Number'] = songs
    return dict1

print('Enter a singer name and his/her album')
sin = input('Singer: ')
alb = input('Album: ')
son = input('Songs in the album: ' )
singer_album = make_album(sin, alb, son)
print(singer_album)


#print('Enter a singer name and his/her album')
#sin = input('Singer: ')
#alb = input('Album: ')

singer_album = make_album(sin, alb)
print(singer_album)