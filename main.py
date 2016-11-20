import tweepy
import json

# initialize the api object to be null
api = None

# send the auth tokens and whatnot
# def auth ():

# 	api = tweepy.API(auth)

# 	print "done"


if __name__ == '__main__':
	# authorize the api
	auth = tweepy.OAuthHandler('"stop looking"')
	auth.set_access_token('DONT LOOK HERE PLEASE')

	api = tweepy.API(auth)
	
	# 1a. search for addresses
	stringified = str(api.search("123 Defhacks Avenue"))
	usr = "skota121"
	
	address_occurences = stringified.count(usr) / 5
	print "address occurences: ", address_occurences

	# 1b. search for phone numbers
	stringified = str(api.search("453-958-1904"))
	usr = "skota121"
	
	phone_occurences = stringified.count(usr) / 5
	print "phone occurences", phone_occurences







