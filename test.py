import os
import glob

path = '/home/wei/Downloads/tweets/'
for infile in glob.glob( os.path.join(path, '*.txt.gz') ):
    print "current file is: " + infile