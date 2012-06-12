import re
path1="/home/wei/Downloads/tweets/US_cluster_truth.txt"

def ReadKeyWord(path):
    wordList=[]
    f=open(path,'r')
    while 1:
        word=f.readline()
        if word=='\n':
            word=f.readline()
        if not word: break
        word=(re.findall(r'\w+', word))[0]
        wordList.append(word)
    f.close()
    wordList.remove('retweet')
    wordList.remove('jobs')
    return wordList

#print ReadKeyWord(path1)
#print len(ReadKeyWord(path1))