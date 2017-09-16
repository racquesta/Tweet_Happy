# Dependencies

import tweepy
import time
import json
import random

# Twitter API Keys
consumer_key = 'vFyAOBmE8Bylt6IIiUHVUQxYp'
consumer_secret = "mj0EXkBHSMJSjeHuNU6TpKamNAntP9kRZEks4PMFw4VJhLV6kz"
access_token = "1570660926-AAS0qgH2V7uIEQtbRe6F7mACAK4Lbhnm8nshtBA"
access_token_secret = "BrUa5pu4JFN6Sql0jRSDAbvtUcezGFE5c0hWjWeXuWcZj"


# Use Tweepy to Authenticate our access
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())

# Quotes to Tweet
happy_quotes = [
    "For every minute you are angry you lose sixty seconds of happiness. - Ralph Waldo Emerson",
    "Folks are usually about as happy as they make their minds up to be. - Abraham Lincoln",
    "Happiness is when what you think, what you say, and what you do are in harmony. - Mahatma Gandhi",
    "Count your age by friends, not years. Count your life by smiles, not tears. - John Lennon",
    "Happiness is a warm puppy. - Charles M. Schulz",
    "The happiness of your life depends upon the quality of your thoughts. - Marcus Aurelius",
    "Now and then it's good to pause in our pursuit of happiness and just be happy. - Guillaume Apollinaire"]

# Create function for tweeting
def tweety_happy(tweet):
    
    api.update_status(tweet)

# Twitter credentials

# Tweet a random quote



while(True):
    rand_tweet = happy_quotes[random.randrange(0, len(happy_quotes)-1)]
    print(rand_tweet)
    try:
        
        tweety_happy(rand_tweet)
    
# Print success message
        print('Success')

    except:
        print('Dup')
# Set timer to run every minute
    time.sleep(60)

#     tweet_id = api.user_timeline(count = 1)[0]['id']
# # print(tweet_id)
#     api.destroy_status(tweet_id)



