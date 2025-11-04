def make_album(artist_name, album, track=None):
    if track:
        print(f"{artist_name} : {album.capitalize()} Album had {track} songs on it.")
        
    else:
        print(f"{artist_name.title()} : {album}")

make_album('nirvana','smells like teen spirit')
make_album('nirvana','smells like teen spirit', '8')