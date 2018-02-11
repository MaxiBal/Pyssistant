import spotipy
import spotipy.util as util
util.prompt_for_user_token(username,scope,client_id='2425341c45074bb698b46a1a47d8c46f',client_secret='f537e4f0359e40cbb3193223c0385177')
name = input("The artist name? ")
spotify = spotipy.Spotify()
results = spotify.search(q='artist: ' + name, type='artist')
print(results)
