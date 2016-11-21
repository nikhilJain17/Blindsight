import tweepy
import json
import oauth2
import requests
from socketIO_client import SocketIO, LoggingNamespace
from Naked.toolshed.shell import execute_js
import os


def notify(title, subtitle, message):
    t = '-title {!r}'.format(title)
    s = '-subtitle {!r}'.format(subtitle)
    m = '-message {!r}'.format(message)
    os.system('terminal-notifier {}'.format(' '.join([m, t, s])))
    print "notf"




# initialize the api object to be null
api = None

def oauth_req(url, key, secret, http_method="GET", post_body="", http_headers=None):
    consumer = oauth2.Consumer(key='NO', secret='NO')
    token = oauth2.Token(key=key, secret=secret)
    client = oauth2.Client(consumer, token)
    resp, content = client.request( url, method=http_method, body=post_body, headers=http_headers )
    return content



if __name__ == '__main__':
	# authorize the api
	auth = tweepy.OAuthHandler('No', 'No')
	auth.set_access_token('No', 'NO')

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
	print "phone occurences: ", phone_occurences

	#2. get followers of followers
	allfriends = oauth_req('https://api.twitter.com/1.1/followers/list.json?cursor=-1&screen_name=skota121&skip_status=true&include_user_entities=false', 'NO', 'NO' )
	allfriends = json.loads(allfriends)

	followers_of_followers = 0;

	# iterate through each follower
	for user in allfriends['users']:
		followers_of_followers += user['followers_count']

	print "followers of followers: ", followers_of_followers

	#3. get how many people you are blocking
	blocked_people = oauth_req('https://api.twitter.com/1.1/blocks/ids.json?stringify_ids=true&cursor=-1&screen_name=skota121&skip_status=true&include_user_entities=false', 'NO', 'NO' )
	blocked_people = json.loads(blocked_people)

	num_of_blocked_folks = len(blocked_people['ids'])

	print "blocked people: ", num_of_blocked_folks

	#4. how much you posted per week
	recent_tweets = oauth_req('https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name=skota121&count=13&since_id=796424467157319680', 'NO', 'NO')
	recent_tweets = json.loads(recent_tweets)

	# @todo put random tweet into twitter card
	print "tweets in the last month:", len(recent_tweets)


	# send data to server
	url = 'http://a37775ba.ngrok.io/data' # Set destination URL here
	data = {'address_occurences': address_occurences,'phone_occurences': phone_occurences, 'blocked_people': num_of_blocked_folks, 'recent_tweets': len(recent_tweets), 'followers_of_followers':followers_of_followers}     

	r = requests.post(url,data)

	print data
	print r.status_code, r.reason

	# # socket.io bois
	# with SocketIO('http://0a561ecd.ngrok.io', 3000, LoggingNamespace) as socketIO:
	# 	socketIO.emit('data')

	success = execute_js('client.js')

	if success:
		print "nice"
	else:
		print "dammit"

# 	# push notifications
# # Calling the function
# 	t = '-title {!r}'.format('BlindSight')
# 	s = '-subtitle {!r}'.format('Twitter Alert')
# 	m = '-message {!r}'.format('You posted a new tweet!')
# 	os.system('terminal-notifier {}'.format(' '.join([m, t, s])))
#     # os.system('terminal-notifier {}'.format(' '.join([m, t, s])))



	# title = 'BlindSight'
	# subtitle = 'Twitter'
	# message = 'You posted a new tweet!'
	# t = '-title {!r}'.format(title)
	# s = ""
 #    # s = '-subtitle {!r}'.format(subtitle)
 #    m = '-message {!r}'.format(message)

	# write to the html file
	target = open('index', 'w')

	target.write('Sankruth was here')
	target.close()












