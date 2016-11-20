import tweepy

# initialize the api object to be null
api = None

# send the auth tokens and whatnot
# def auth ():
# 	auth = tweepy.OAuthHandler('3vak8cyOxT0dHvbYvqUZ7i6Hp', 'tACDJJL56ZQNWTSHsUN2bYYn7qsuxRjFNvpVvfNYMHocAZqRdl')
# 	auth.set_access_token('1581800299-aiZuhraRWWWacTCegHpMFiUIPJDv1q2uv6x3udE', '47jzAZr4CqrZhvjsTY2GLwW750NC4qrJ16jATauUgrnL2')

# 	api = tweepy.API(auth)

# 	print "done"


if __name__ == '__main__':

	api = tweepy.API(auth)
	
	user = api.get_user('skota121')
	print user.followers_count







