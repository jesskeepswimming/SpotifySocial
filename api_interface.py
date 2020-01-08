import json
import requests
from secret import *

api_token = oauth1
api_token2 = oauth2

api_url_base = 'https://api.spotify.com/v1/me'

headers = {'Content-Type': 'application/json',
            'Accept' : "application/json",
           'Authorization': 'Bearer {0}'.format(api_token)}

headers2 = {'Content-Type': 'application/json',
            'Accept' : "application/json",
           'Authorization': 'Bearer {0}'.format(api_token2)}

def get_currently_playing():

    response = requests.get(api_url_base+"/player/currently-playing", headers=headers)

    if response.status_code == 200:
        return response
    else:
        return None


def play(songid, songposition):  
    
    data = {
        "uris":["spotify:track:" + songid],
        "position_ms": songposition
    }

    response = requests.put(api_url_base + "/player/play", data = json.dumps(data), headers=headers2)

    return response


def refresh():
    
    if get_currently_playing() != None:
        songposition = get_currently_playing().json()["progress_ms"]
        songid = get_currently_playing().json()["item"]["id"]

        play(songid, songposition)
    else:
        print('error')
        return None

    return

refresh()








