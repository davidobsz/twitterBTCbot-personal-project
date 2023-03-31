import datetime
import time
from datetime import datetime
import tweepy
import requests

# All tokens
bearer_token = ''
consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''
# client_id= ''
# client_secret = ''

# Authenticate to twitter
auth=tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)
api=tweepy.API(auth)

# Send tweet
while True:
    try:

        symbol = 'BTCUSDT'

        # Binance API call
        response = requests.get(f'https://api.binance.us/api/v3/ticker/price?symbol=BTCUSDT')

        # if binance API call successful
        if response.status_code == 200:

            # get data from the json response and get the price
            data = response.json()
            price = data['price']
            # print(f"The current price of {symbol} is {price}")
            currentDateAndTime = datetime.now()

            # send the tweet of the current price of x and the date & time
            api.update_status(f"Current price of {symbol}: ${price}\n\n{currentDateAndTime}")

        else:

            print(f"Error: {response.status_code}")

    except:

        print("error")

    # run the while loop every x seconds
    time.sleep(10)