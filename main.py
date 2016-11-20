import tweepy
import json

# initialize the api object to be null
api = None

# send the auth tokens and whatnot
# def auth ():
# 	auth = tweepy.OAuthHandler('3vak8cyOxT0dHvbYvqUZ7i6Hp', 'tACDJJL56ZQNWTSHsUN2bYYn7qsuxRjFNvpVvfNYMHocAZqRdl')
# 	auth.set_access_token('1581800299-aiZuhraRWWWacTCegHpMFiUIPJDv1q2uv6x3udE', '47jzAZr4CqrZhvjsTY2GLwW750NC4qrJ16jATauUgrnL2')

# 	api = tweepy.API(auth)

# 	print "done"


if __name__ == '__main__':
	# authorize the api
	auth = tweepy.OAuthHandler('DONOTREAD')
	auth.set_access_token('NOT NOW NOT EVER')

	api = tweepy.API(auth)
	
	# 1a. search for phone number
	stringified = str(api.search("123 Defhacks avenue"))
	usr = "skota121"
	print stringified.find(usr)







