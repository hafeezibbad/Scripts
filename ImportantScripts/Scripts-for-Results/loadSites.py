#!/usr/bin/python

__author__ = 'hafeez'

import threading
import csv
import time
import os

filename = '/home/hafeez/Desktop/top500.csv'
outputfile = '/home/hafeez/Desktop/top500-times.csv'

dict_times = {}

counter = 0

def load_page(link_str):
    global dict_times
    global counter
    link = 'wget www.'+link_str+' -o /dev/null'
    st = time.time()
    os.system(link)
    loadingTime = time.time() - st
    counter += 1
    dict_times[link_str] = loadingTime
    print "%d: Loaded %s in %d seconds" % (counter, link_str, dict_times[link_str])

with open(filename, 'rb') as inputfile:
    csv_reader = csv.reader(inputfile, delimiter=',')
    for row in csv_reader:
        threading._start_new_thread(load_page, (row[1],))


time.sleep(60)

print '************************** update times **************************'
# update the times which are un-understandably high
for key in dict_times.keys():
    if int(dict_times[key]) > 10:
        print '*************** before *******************'
        print key, dict_times[key]
        threading._start_new_thread(load_page,(key,))
        print '*************** after *******************'
        print key, dict_times[key]

print '************************** times updated **************************'
# write the values from dictionary to file
writer = csv.writer(open(outputfile, 'wb'))
for key, value in dict_times.items():
    writer.writerow([key, value])



# read values from file to dictionary
reader = csv.reader(open(outputfile, 'rb'))
try:
    retrieved_dict = dict(x for x in reader)
    for key, val in retrieved_dict:
        print key, val
except:
    print 'invalid value in the dictionary'
