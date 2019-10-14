def make_album(artist_name, album_name, tracks=''):
    album = {'artist': artist_name, 'album':album_name}
    if tracks:
        album['tracks'] = tracks
    return album

while True:
    artist = input('Enter artist name: ')
    album = input('Enter album title: ')
    print(make_album(artist, album))
    repeat = input('Enter another album? yes/no\n')
    if repeat == 'no':
        break
    
