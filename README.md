# tweet-python
Python script using `tweepy` library to post tweets on my twitter account 

## Usage
Sign up to a twitter developer account and create an app.   
Once you have created an app find your keys in the `keys and tokens` section of the app. 
### Fill in cfg.py file
```
[twitter_config]
consumer_secret = 
consumer_key = 
access_token = 
access_token_secret = 
```
Put your keys here with no speech marks. i.e. consumer_secret = adsdb23123-dsbhdasb23231 (made up key).   
Run the program with:
```
python post_tweet.py
```
This will post a tweet on the account you have registered on twitter when signing up to a developer account. 
