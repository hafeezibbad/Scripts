#!/usr/bin/python
# __author__ = 'eb'


import math

string="tiina.niklander@cs.helsinki.fi"

substrings=[]
indexes_original=[]
suffix_dictionary={}
suffix_indexes=[]
for i in range(len(string)):
    #save the substrings
    substrings.append(string[i:])
    #save the strings
    indexes_original.append(i)
#substrings
#print substrings
#sorted substrings
sorted_substrings=(sorted(substrings))
#print sorted_substrings

#find suffix indexes
for substring in sorted_substrings:
    suffix_indexes.append(substrings.index(substring))

#print suffix_indexes

#suffix table built :)


#do the suffix matching
start=0
end=len(suffix_indexes)
pattern="niklander"
pattern=pattern.lower()
found =0

while True:
    middle=(start+end)/2
    #finding the correction middle
    check = middle-int(middle)
    if (check<0.5):
        middle=int(middle)
    else:
        middle=int(middle)+1
    #print start,":",end,":",middle
    #ending criteria met
    if start > end:
        print "No matching pattern found "
        break
    elif (len(sorted_substrings[middle-1])>len(pattern)):
        #match only required bits
        if(sorted_substrings[middle-1][0:len(pattern)]>pattern):
            #print (sorted_substrings[middle-1]),":",pattern
            end=middle-1
        elif (sorted_substrings[middle-1][0:len(pattern)]<pattern):
            #print (sorted_substrings[middle-1]),":",pattern
            start=middle+1
        elif (sorted_substrings[middle-1][0:len(pattern)]==pattern):
            print "found the match: ",sorted_substrings[middle-1]
            found =1
            break
    else:
        if(sorted_substrings[middle-1]>pattern):
            #print (sorted_substrings[middle-1]),":",pattern
            end =middle-1
        elif (sorted_substrings[middle-1]<pattern):
            print (sorted_substrings[middle-1]),":",pattern
            start=middle+1
        elif (sorted_substrings[middle-1][0:len(pattern)]==pattern):
            print "found the match: ",sorted_substrings[middle-1]
            print substrings.index(substring)
            found =1
            break
if (found):
    print "The index of suffix in string is: ", suffix_indexes[middle-1]
    print "Index in suffix table is ", middle," and original substring table is: ",substrings.index(substring)
