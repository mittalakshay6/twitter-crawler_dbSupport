import json

def tweet_html(josnFile):
    with open(jsonFile) as f:
        data = json.load(f)
    d=data[0]['html']
    return d
