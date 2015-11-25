#!/usr/bin/python
# __author__ = 'eb'


import random
import sys

def getSuffixTable(string):
    substrings=[]
    indexes_original=[]
    suffix_indexes=[]
    sorted_substring=[]

    for i in range (len(string)):
        substrings.append(string[i:])
        indexes_original.append(i)

    #sort the substrings
    sorted_substrings=(sorted(substrings))

    #find suffix indexes
    for substring in sorted_substrings:
        suffix_indexes.append(substrings.index(substring)+1)
    return suffix_indexes



def generate_random_string(length):
    return [random.choice('ab') for _ in range(length)]

# find the string which matches our required conditions of suffix table

if __name__=="__main__":

    count =0
    targetSuffixTable=[16,13,3,14,11,9,4,6,15,12,2,10,8,5,1,7]

    while True:
        string_list=generate_random_string(16)
        count+=1
        string =''.join(string_list)
        print count,":",string
        #a=getSuffixTable(string)
        #print a
        if (getSuffixTable(string)==targetSuffixTable):
            print "The required string is: ",string
            break

    sys.exit(0)
