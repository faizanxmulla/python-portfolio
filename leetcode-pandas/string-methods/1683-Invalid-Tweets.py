import pandas as pd

def invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame:
    tweets = tweets.query('content.str.len() > 15')
    return tweets[['tweet_id']]



# SELECT tweet_id
# FROM   tweets
# WHERE  LENGTH(content) > 15