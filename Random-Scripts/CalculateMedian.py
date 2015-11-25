

import os
import sys


### Two data sets we will use, along with two samples
DATA1 = '/data/dsp15/data-1.txt'
DATA2 = '/data/dsp15/data-2.txt'
DATA3 = '/data/dsp15/data-1-sample.txt'
DATA4 = '/data/dsp15/data-2-sample.txt'

### Some variables you may want to personalize
AppName = "question-1"
TMPDIR = "/cs/taatto/group/cone/tmp/"


### Creat a Spark context on Ukko cluster
from pyspark import SparkConf, SparkContext
conf = (SparkConf()
        .setMaster("spark://ukko080:7077")
        .setAppName(AppName)
        .set("spark.rdd.compress", "true")
        .set("spark.broadcast.compress", "true")
        .set("spark.cores.max", 10)  # do not be greedy :-)
        .set("spark.local.dir", TMPDIR))
sc = SparkContext(conf = conf)


### Put your algorithm here.

def calculate_average(fn):
    data = sc.textFile(fn)
    data = data.map(lambda s: float(s))
    myAvg = data.sum() / data.count()
    return myAvg

def calculate_min(fn):
    data=sc.textFile(fn)
    data=data.map(lambda s: float(s))
    myMin=data.min()
    return myMin

def calculate_max(fn):
    data=sc.textFile(fn)
    data=data.map(lambda s: float(s))
    myMax=data.max()
    return myMax
def calculate_variance(fn):
    data=sc.textFile(fn)
    data=data.map(lambda s: float(s))
    variance=data.variance()
    return variance


def calculate_median(fn):
    data=sc.textFile(fn)
    dataPairs=data.map(lambda s: float(s))
    pairs=dataPairs.map(lambda s: (int(s),1)).reduceByKey(lambda a, b: a + b)
    sortedPairs=pairs.sortByKey()
    merapairs=sortedPairs.collect()
    totalValues=0;
    for x,y in merapairs:
        print x,y
        totalValues+=y
       
    print "totalValues",totalValues
    indexOfMedianValue=0
    if(totalValues%2==0):
    	indexOfMedianValue=totalValues/2
    else:
	indexOfMedianValue=(totalValues+1)/2
    print "index of median value:",indexOfMedianValue
    #find bucket of median value
    bucketOfMedian=0
    previousCount=0
    countTillNow=0
    for x,y in merapairs:
	previousCount=countTillNow
	countTillNow+=y
	if(indexOfMedianValue>=previousCount and indexOfMedianValue<=countTillNow):
		bucketOfMedian=x
		break;
    
    bucket=dataPairs.filter(lambda s: int(s)==bucketOfMedian)
    bucketIter=bucket.collect();
    bucketIter.sort()
    myMedian=bucketIter[countTillNow-previousCount-1]
    return myMedian

if __name__=="__main__":
   # myAvg = calculate_average(DATA1)
   # myMin = calculate_min(DATA1)
   # myMax = calculate_max(DATA1)
   # myVariance = calculate_variance(DATA1)
   # print "Avg. = %.8f" % myAvg
   # print "Min. = %.8f" %myMin
   # print "Max. = %.8f" %myMax
   # print "Variance. =%.8f" %myVariance
     myMedian=calculate_median(DATA1)
   
     print "Median. =%.8f" %myMedian
		
     sys.exit(0)
