#-*- coding: utf-8 -*-
from twitter import TweetFiles
#import cjson, gzip
import re
import os
dir1 = '/home/wei/Downloads/tweets/2011/'
#dir1='/home/wei/spacialTemporal/testdata/testdata2/'
#path1="/home/wei/Downloads/geo.2011-10-02_23-49.txt.gz"
monthDict = {'Jan':1, 'Feb':2, 'Mar':3, 'Apr':4, 'May':5, 'Jun':6, 'Jul':7, 'Aug':8, 'Sep':9, 'Oct':10, 'Nov':11, 'Dec':12}
#===============================================================================
# build a full dictionary with all necessary dimensions included
#===============================================================================
#another way to read dir
#import os
#import glob

#path = 'sequences/'
#for infile in glob.glob( os.path.join(path, '*.fasta') ):
#    print "current file is: " + infile
def DocidWordFreqTimeLocationDictFromDir(directory):
    #---------------------- use each tweet as a doc. here may not be appropriate
    #---------------------------------------------------------------- initialize
    collectionWordDict = {}#word:frequency
    dict2 = {}
    timeLocationStamps = {}# docID:"time+location"
    timeLocationStampToDocIdDict = {}#time+location:[DocIds]
    timeToLocationDict = {}#time:[locations]
    locationToTimeDict = {}#location:[times]
    docId = 0
    listing = os.listdir(directory)
    for path in listing:
        print "current file is: " + path
        path = directory + path
        for tweet in TweetFiles.iterateTweetsFromGzip(path):
            try:
                docId += 1
                dict2[docId] = {}       
                #get time stamp
                dict2[docId]['docWordCount'] = 0
                tempTime = []
                tempTime=re.split(r' ',tweet['time'])
                dict2[docId]['time'] = {}
                dict2[docId]['time']['year'] = int(tempTime[5])
                #dict2[docId]['time']['month']={}#seems this is useless
                year='%04d' % int(tempTime[5])
                tempMonth = tempTime[1]
                dict2[docId]['time']['month'] = monthDict[tempMonth]
                month='%02d' % monthDict[tempMonth]
                dict2[docId]['time']['day'] = int(tempTime[2])
                day='%02d' % int(tempTime[2])
                dict2[docId]['time']['hour'] = int(re.split(r':', tempTime[3])[0])
                hour='%02d' % int(re.split(r':', tempTime[3])[0])
                dict2[docId]['time']['minute'] = int(re.split(r':', tempTime[3])[1])
                if dict2[docId]['time']['minute'] < 10:
                    minuteStamp = 0
                elif dict2[docId]['time']['minute'] >= 10 and dict2[docId]['time']['minute'] < 20:
                    minuteStamp = 1
                elif dict2[docId]['time']['minute'] >= 20 and dict2[docId]['time']['minute'] < 30:
                    minuteStamp = 2
                elif dict2[docId]['time']['minute'] >= 30 and dict2[docId]['time']['minute'] < 40:
                    minuteStamp = 3
                elif dict2[docId]['time']['minute'] >= 40 and dict2[docId]['time']['minute'] < 50:
                    minuteStamp = 4
                else:
                    minuteStamp = 5                     
#                print dict2[docId]['time']
#                get location stamp
#                if tweet['coordinates'] != None:
#                    tempLoc1 = '%.2f' % tweet['coordinates']['coordinates'][0]
#                    tempLoc2 = '%.2f' % tweet['coordinates']['coordinates'][1]
                if tweet['corrdinate']!= None:
                    tempLoc1='%d'% tweet['corrdinate'][0]
                    tempLoc2='%d'% tweet['corrdinate'][1]
#                elif tweet['place']['bounding_box'] != None:
#                    tempLocList = []
#                    tempLocList = tweet['place']['bounding_box']['coordinates'][0]
#                    #print tempLocList[0][0]
#                    #print tempLocList        
#                    tempLoc1 = '%.2f' % ((tempLocList[0][0] + tempLocList[1][0] + tempLocList[2][0] + tempLocList[3][0]) / 4)
#                    tempLoc2 = '%.2f' % ((tempLocList[0][1] + tempLocList[1][1] + tempLocList[2][1] + tempLocList[3][1]) / 4)
                else:
                    print "no location info"
                    tempLoc1 = '0'
                    tempLoc2 = '0'
                dict2[docId]['location'] = []
                dict2[docId]['location'].insert(0, tempLoc1)
                dict2[docId]['location'].insert(1, tempLoc2)
                timeStamp = year+month+day+hour+ str(minuteStamp)
                locationStamp = tempLoc1 + tempLoc2
                timeLocationStamps[docId] = (timeStamp + ',' + locationStamp)    
                #print timeLocationStamps
                #creat the other three dictionary for later use
                if timeLocationStamps[docId] not in timeLocationStampToDocIdDict.keys():
                    timeLocationStampToDocIdDict[timeLocationStamps[docId]] = []
                timeLocationStampToDocIdDict[timeLocationStamps[docId]].append(docId)    
                if timeStamp not in timeToLocationDict.keys():
                    timeToLocationDict[timeStamp] = []
                timeToLocationDict[timeStamp].append(locationStamp)               
                if locationStamp not in locationToTimeDict.keys():
                    locationToTimeDict[locationStamp] = []
                locationToTimeDict[locationStamp].append(timeStamp)               
                #get words
                dict2[docId]['words'] = {}
        #-------------------------------------------------------- DocWordFreqDict(path1)
    #            if tweet['text']==None:
    #                docId-=1
    #            if re.findall(r'\w+', tweet['text'])==None:
    #                docId-=1
                
                #for puretweet in tweet['text'].split():
                #    dict2[docId]['docWordCount'] += 1 
                #    if(puretweet in dict2[docId]['words'].keys()):
                #        dict2[docId]['words'][puretweet] += 1 
                #    else:
                #        dict2[docId]['words'][puretweet] = 1
                #    if(puretweet in collectionWordDict.keys()):
                #        collectionWordDict[puretweet] += 1
                #    else:
                #        collectionWordDict[puretweet] = 1
                # 
                for puretweet in re.findall(r'\w+', tweet['text']):
                    
                        
                    #-------------------------- for puretweet in tweet['text'].split('\W+'):
                        #---------------------------------------------print pure text tweets
                        #------------------------------ if (dict2[docNum][puretweet]!=None):
                        #puretweet=str(puretweet)
                    dict2[docId]['docWordCount'] += 1 
                    if(puretweet in dict2[docId]['words'].keys()):
                        dict2[docId]['words'][puretweet] += 1 
                    else:
                        dict2[docId]['words'][puretweet] = 1
                    if(puretweet in collectionWordDict.keys()):
                        collectionWordDict[puretweet] += 1
                    else:
                        collectionWordDict[puretweet] = 1
            except: pass
#    print collectionWordDict
#    print dict2
    return (collectionWordDict, dict2, timeLocationStamps, timeLocationStampToDocIdDict, timeToLocationDict, locationToTimeDict)
#print DocidWordFreqTimeLocationDict(path1)   
f= open('/home/wei/Downloads/out.txt','w')
print >>f, DocidWordFreqTimeLocationDictFromDir(dir1)   
f.close()
#DocidWordFreqTimeLocationDictFromDir(dir1)    
