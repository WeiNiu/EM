'''
Created on Jun 14, 2011

@author: kykamath
'''

import cjson, gzip
from datetime import datetime

twitter_api_time_format = '%a %b %d %H:%M:%S +0000 %Y'

class TweetFiles:
    @staticmethod
    #generator
    def iterateTweetsFromGzip(file):
        for line in gzip.open(file, 'rb'):
            try:
                data = cjson.decode(line)
                #read one line each time and return. notice the difference between yield and return.
                #to avoid read all tweets into the memory at one time
                if 'text' in data: yield data
            except: pass
        
def getDateTimeObjectFromTweetTimestamp(timeStamp): return datetime.strptime(timeStamp, twitter_api_time_format)
def getStringRepresentationForTweetTimestamp(timeStamp): return datetime.strftime(timeStamp, twitter_api_time_format)