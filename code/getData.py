import tweepy
from tweepy import OAuthHandler
import csv
import time

#API Credentials
consumer_key = 'GvyzAMpV6G5xsOCf4HtjaKO52'
consumer_secret = 'VZ8Ra1Vp46D5Gq5Otf6XVCaLzAVmRPHGG4MLHXpKSO7zWZJFPO'
access_token = '804568727685447680-Wuv4RjqRvkp1OoAXeIVJLokl4boO1Hl'
access_secret = 'HBcA0FJ8YBbg9SXGLy8JhdF2PKpGjyUeIvgZRBWzAZurZ'

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

# Open/create a file to write data to
csvFile = open('result1.csv','w')

#Use csv writer
csvWriter = csv.writer(csvFile)

words = ['Asleep and never wake','Just want to sleep forever','Take my own life','Can’t do this anymore','Kill myself','Thoughts of suicide'
,'Could just fall asleep','Killing myself','Tired of being alone',
'Die in my sleep','Life is so meaningless','Tired of being lonely',
'Don’t want to be here','Life is too hard','To end this nightmare',
'Don’t want to exist','Life is worthless','To hurt myself',
'Don’t want to go on','My death would','To live anymore',
'Don’t want to live','My life consists of nothing','Want it to be over',
'Don’t want to try anymore','My life is pointless','Want to be alive anymore',
'Don’t want to wake up','My life is this miserable','Want to be around anymore',
'End it all','My life isn’t worth','Want to be dead',
'End my life','Not want to be alive','Want to be gone',
'End this pain','Nothing to live for','Want to be here anymore',
'Ending it all','Point in living','Want to die',
'Hate my life','Put an end to this','Want to disappear',
'Hate myself','Ready to die','Want to end it',
'I’m drowning','Really need to die','Wanted to die',
'I’m leaving now','Stop the pain','Wanting to kill yourself',
'I’m worthless','Suicidal','What is wrong with me',
'Isn’t worth living','Suicide','Why should I continue living',
'Just want to give up','Take it anymore']

for word in words:
	print(word)
	c = tweepy.Cursor(api.search, q=word).items(3000)
	while True:
		try:
			tweet = c.next()
			# Insert into file
			csvWriter.writerow([tweet.text])
		except tweepy.TweepError:
			time.sleep(60 * 15)
			continue
		except StopIteration:
			break
csvFile.close()
