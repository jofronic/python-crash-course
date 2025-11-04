def make_album(artist_name, album, track=None):
    """This recives artist album information """
    album_info = {'artist name': artist_name, 'album': album}
    if track:
        album_info['tracks'] = track
    return album_info

while True:
    
    artist_name = input('Enter the artist name')
    if artist_name.lower() == 'quit':
        break

    album = input('What is the name of the album? ')
    if album.lower() == 'quit':
        break
    
    track = input ("do you remember the track count(Press enter to skip)")
    if track.lower == 'quit':
        break

album_dict = make_album(artist_name, album, track)
print(album_dict)
