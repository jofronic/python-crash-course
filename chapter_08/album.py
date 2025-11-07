def make_album(artist_name, album, track=None):
    """This recives artist album information """
    summary = {'artist:':artist_name, 'album:':album}

    if track:
        summary['track number'] = track
    
    return summary
while True:
    stop = 'quit'
    artist_answer = input('\nWhat is the name of the artist? ')
    if artist_answer.lower() == stop:
         break
    
    album_answer= input ('What is the name of the album: ')
    if album_answer.lower() == stop:         
         break
    
    track_answer = input('How many tracks were on the album? ')
    
    if track_answer == '':

        full_info = make_album(artist_answer, album_answer)
    else:
        full_info = make_album(artist_answer, album_answer,track_answer)

        
print(f"These are the results of your albums lists:")
print(full_info)

    