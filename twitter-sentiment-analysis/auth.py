import tweepy
####################################################################
ckey = "kJ7cVjRFIqShDEueI5eoJNXgA"
csecret = "iMcXFluWDb1azrpgPR3hDTNjiqjJSktS64jlpNv34xPlFzLteI"
atoken = "733948324215132160-To4B4L8SzBny5HrrW56ScizgS7AvRGN"
asecret = "Hs1Ld9QASf472jWlXmRzqZO1GfBcpGBgtkQK0mxkP4kHB"

keys = {'consumer_key':ckey, 'consumer_secret':csecret,
    'access_token_key':atoken, 'access_token_secret':asecret}
####################################################################
try:
    auth = tweepy.OAuthHandler(keys['consumer_key'], keys['consumer_secret'])
    api = tweepy.API(auth)
except:
    print("authorization failed.")

####################################################################

