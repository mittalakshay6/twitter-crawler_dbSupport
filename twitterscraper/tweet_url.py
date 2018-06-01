import json

with open('mySecurityTweets.json') as f:
    data = json.load(f)
d=data[0]['url']
d="www.twitter.com"+d
