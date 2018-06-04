from datetime import datetime

from bs4 import BeautifulSoup
from coala_utils.decorators import generate_ordering
import json


@generate_ordering('timestamp', 'id', 'text', 'user', 'replies', 'retweets', 'likes')
class Tweet:
    # def __init__(self, user, fullname, id, url, timestamp, text, replies, retweets, likes, html):
    #     self.user = user.strip('\@')
    #     self.fullname = fullname
    #     self.id = id
    #     self.url = url
    #     self.timestamp = timestamp
    #     self.text = text
    #     self.replies = replies
    #     self.retweets = retweets
    #     self.likes = likes
    #     self.html = html

    def __init__(self, url, timestamp, html):
        self.url = url
        self.timestamp = timestamp
        self.html = html

    @classmethod
    def from_soup(cls, tweet):
        return cls(
            # user=tweet.find('span', 'username').text or "",
            # fullname=tweet.find('strong', 'fullname').text or "",
            # id=tweet['data-item-id'] or "",
            url=tweet.find('div', 'tweet')['data-permalink-path'] or "",
            timestamp=datetime.utcfromtimestamp(
                int(tweet.find('span', '_timestamp')['data-time'])),
            # text=tweet.find('p', 'tweet-text').text or "",
            # replies = tweet.find(
            #     'span', 'ProfileTweet-action--reply u-hiddenVisually').find(
            #         'span', 'ProfileTweet-actionCount')['data-tweet-stat-count'] or '0',
            # retweets = tweet.find(
            #     'span', 'ProfileTweet-action--retweet u-hiddenVisually').find(
            #         'span', 'ProfileTweet-actionCount')['data-tweet-stat-count'] or '0',
            # likes = tweet.find(
            #     'span', 'ProfileTweet-action--favorite u-hiddenVisually').find(
            #         'span', 'ProfileTweet-actionCount')['data-tweet-stat-count'] or '0',
            html=str(tweet.find('p', 'tweet-text')) or "",
        )

    @classmethod
    def from_html(cls, html):
        soup = BeautifulSoup(html, "lxml")
        tweets = soup.find_all('li', 'js-stream-item')
        if tweets:
            for tweet in tweets:
                try:
                    yield cls.from_soup(tweet)
                except AttributeError:
                    pass  # Incomplete info? Discard!

    @classmethod
    def tweet_html(cls, i, jsonfile):
        with open(jsonfile) as f:
            data = json.load(f)
        if data[i]:
            d = data[i]['html']
            return d
        else:
            return -1

    @classmethod
    def tweet_url(cls, i, jsonfile):
        with open(jsonfile) as f:
            data = json.load(f)
        try:
            d = data[i]['url']
            d = "www.twitter.com" + d
            return d
        except IndexError:
            return -1
