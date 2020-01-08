import json
import requests
from secret import *

#api_token = oauth1
#api_token2 = oauth2

api_url_base = 'https://api.spotify.com/v1/me'

def headers(token):
    
    headers = {'Content-Type': 'application/json',
                'Accept' : "application/json",
            'Authorization': 'Bearer {0}'.format(token)}
    return headers
    

def get_currently_playing(head):

    response = requests.get(api_url_base+"/player/currently-playing", headers=head)

    if response.status_code == 200:
        return response
    else:
        return None


def play(songid, songposition, head):  
    
    data = {
        "uris":["spotify:track:" + songid],
        "position_ms": songposition
    }

    response = requests.put(api_url_base + "/player/play", data = json.dumps(data), headers=head)

    return response


def refresh(oauth1, oauth2):
    
    if get_currently_playing(headers(oauth1)) != None:
        songposition = get_currently_playing(headers(oauth1)).json()["progress_ms"]
        songid = get_currently_playing(headers(oauth1)).json()["item"]["id"]
        print(get_currently_playing(headers(oauth1)).text)

        play(songid, songposition, headers(oauth2))
        
        
        print('success')

    else:
        print('error')
        return None

    return









