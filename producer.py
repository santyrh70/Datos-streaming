import tweepy
from kafka import KafkaProducer
import logging

consumerKey = "tc0Ii7CVS0DZb3nKyilfoeQXH"
consumerSecret = "1XdmockCisgmKYpVonUwMjNWhq7dsKMDwZ36pDm1MxIcQBjiB9"
accessToken = "884699978-vx7JZBam0FBh7ohn1PTX8InYlp3SAOSoJFWqm9WW"
accessTokenSecret = "4OBlyAFA59ytIZuXWG4dHhh1T2DNuGifO1TSu4Y0FoX2K"

producer = KafkaProducer(bootstrap_servers='localhost:9092')
search_term = ["europe"]
topic_name = 'twitter'


def twitterAuth():
    authenticate = tweepy.OAuthHandler(consumerKey, consumerSecret)
    authenticate.set_access_token(accessToken, accessTokenSecret)
    api = tweepy.API(authenticate, wait_on_rate_limit=True)
    return api


class TweetListener(tweepy.Stream):

    def on_data(self, raw_data):
        logging.info(raw_data)
        producer.send(topic_name, value=raw_data)
        return True

    def on_error(self, status_code):
        if status_code == 420:
            return False

    def start_streaming_tweets(self, search_term):
        self.filter(track=search_term, stall_warnings=True, languages=["en"])


if __name__ == '__main__':
    twitter_stream = TweetListener(consumerKey, consumerSecret, accessToken, accessTokenSecret)
    twitter_stream.start_streaming_tweets(search_term)

