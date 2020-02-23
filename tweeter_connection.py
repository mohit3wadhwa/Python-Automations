import tweepy

print("I am Twitter app")

CONSUMER_KEY = 'xpYDhdBj39T5Gzktwrksg8bBH'
CONSUMER_SECRET = '5SpeKHJ4TIlV8is9l1rhd06h0vSWFiyOx9kWqICQaoGMXywERp' 
ACCESS_KEY = '4025843547-c8u7fy2mwIPU9C9hi77dpGZ1RJiFg8cM4iz9wfL'
ACCESS_SECRET = 'aUqb0GKH4tvBkFyHBclT126Bbx9JL5srXMQ2Yo8zlxbiw'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)
 

mentions = api.mentions_timeline()

for mention in mentions:
	print(str(mention.id) + " --> " + str(mention.text))

#print(api.mentions_timeline())  
