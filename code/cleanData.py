import pandas as pd 
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import html.parser
import re
from textblob import TextBlob
import csv
import numpy as np
import random


data = pd.read_csv("../datasets/TwitterRawData.csv")
data = data.reindex(np.random.permutation(data.index))

csvFile = open('../datasets/suicideTweetData.csv','w')
csvWriter = csv.writer(csvFile)

def preprocess(tweet):
	html_parser = html.parser.HTMLParser()
	temp_tweet = html_parser.unescape(tweet)
	temp_tweet = re.sub(r'@[A-Za-z0-9]+','',temp_tweet)
	temp_tweet = re.sub('https?://[A-Za-z0-9./]+','',temp_tweet)
	temp_tweet = temp_tweet.strip('\'"') 
	temp_tweet = re.sub(r'[,_~<>%)-*/(#:\'.\?]','',temp_tweet)
	temp_tweet = re.sub('[0-9]+', ' ',temp_tweet)
	temp_tweet = re.sub(r'[:=x][)(/3)D]','',temp_tweet)

	emoji_pattern = re.compile("["u"\U0001F600-\U0001F64F""]+",flags = re.UNICODE)
	temp_tweet = emoji_pattern.sub(r'',temp_tweet)

	stop= stopwords.words('english') + [' ']
	temp_tweet = temp_tweet.lower()
	temp_tweet = re.sub(' +',' ',temp_tweet)
	csvWriter.writerow([temp_tweet,-1])

for i in range(data.shape[0]):
	tweet = data.iloc[i][0]
	preprocess(tweet)

