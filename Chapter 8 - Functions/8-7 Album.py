def make_album(artist_name, album_name, tracks=''):
    album = {'artist': artist_name, 'album':album_name}
    if tracks:
        album['tracks'] = tracks
    return album

album1 = make_album('Honey', 'Robyn', tracks=5)
print(album1)
