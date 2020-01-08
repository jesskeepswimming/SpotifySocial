import json
import requests
from secret import *

api_token = oauth1
api_token2 = oauth2

api_url_base = 'https://api.spotify.com/v1/me'

headers = {'Content-Type': 'application/json',
            'Accept' : "application/json",
           'Authorization': 'Bearer {0}'.format(api_token)}

def get_currently_playing():

    response = requests.get(api_url_base+"/player/currently-playing", headers=headers)

    #print(response.timestamp)
    #print(response.id)

    if response.status_code == 200:
        return response
    else:
        return None

print(get_currently_playing()["timestamp"])



def play():  
    
    data = {
        "uris":["spotify:track:75ls0gurX68lUmMjE7QcsE"],
        "position_ms": 15000
    }

    response = requests.put(api_url_base + "/player/play", data = json.dumps(data), headers=headers)

    return response





