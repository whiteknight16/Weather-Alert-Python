import json

def get_loc():
    from urllib.request import urlopen

    urlopen("http://ipinfo.io/json")

    data = json.load(urlopen("http://ipinfo.io/json"))

    lat = data['loc'].split(',')[0]

    lon = data['loc'].split(',')[1]

    return (lat, lon)