import tweepy
from config import X_BEARER_TOKEN, X_API_KEY, X_API_SECRET, X_ACCESS_TOKEN, X_ACCESS_SECRET, PROXY_URL

def get_x_client():
    kwargs = {}
    if PROXY_URL:
        kwargs['proxy'] = PROXY_URL

    return tweepy.Client(
        bearer_token=X_BEARER_TOKEN,
        consumer_key=X_API_KEY,
        consumer_secret=X_API_SECRET,
        access_token=X_ACCESS_TOKEN,
        access_token_secret=X_ACCESS_SECRET,
        **kwargs
    )