import httplib
import oauth2
import urllib2

def sendgetrequest( url ):
	conn = httplib.HTTPConnection(url)
	conn.request("HEAD","/index.html")
	res = conn.getresponse()
	print res.status, res.reason

url = 'https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name=skota121'
params = '&oauth_consumer_key='

url = url + params

print "\n\n\n" + url
# print sendgetrequest(url)

content = urllib2.urlopen(url).read()
print content
							 


