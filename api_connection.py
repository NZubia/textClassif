import tweepy
import sys

api_credentials = {
    'api_key': 'tuhe3YrhjnPDZBuMfdveUVxNr',
    'api_secret': 'efMGa2euwUcmD8SJu2di3xyoIjE1amM0UQJurOCcx8yBnWnsll'
}

def connect_api():

    # Replace the API_KEY and API_SECRET with your application's key and secret.
    auth = tweepy.AppAuthHandler(api_credentials['api_key'], api_credentials['api_secret'])

    api = tweepy.API(auth, wait_on_rate_limit=True,
                       wait_on_rate_limit_notify=True)

    if (not api):
        print ("Can't Authenticate")
        sys.exit(-1)
    else:
        return api