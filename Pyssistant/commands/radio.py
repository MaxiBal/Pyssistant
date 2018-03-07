import spotipy
import spotipy.util as util
util.prompt_for_user_token(username,scope,client_id='',client_secret='')
name = input("The artist name? ")
spotify = spotipy.Spotify()
results = spotify.search(q='artist: ' + name, type='artist')
print(results)
