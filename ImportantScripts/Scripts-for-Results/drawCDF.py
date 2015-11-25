#!/usr/bin/python
__author__ = 'hafeez'


from scipy.stats import cumfreq
import numpy
import random
import matplotlib.pyplot as plt
import csv
from pylab import *

a = []

outputfile = '/home/hafeez/Desktop/top1k-times.csv'

# read values from file to dictionary
reader = csv.reader(open(outputfile, 'rb'))
retrieved_dict = dict(x for x in reader)
for key in retrieved_dict.keys():
    a.append(float(retrieved_dict[key]))
#
# sorted_data = numpy.sort(a)
#
# num_bins = 145
#
# counts, bin_edges = numpy.histogram(a, bins=num_bins, normed=True)
# # cdf = numpy.cumsum(counts)
#
# cdf = numpy.cumsum(sorted_data)
#
# # plt(bin_edges[1:], cdf)
#
# plt.plot(cdf)
# plt.show()



values, base = numpy.histogram(a, bins=1000)

cumulative = numpy.cumsum(values)

plt.plot(base[:-1], cumulative, c='blue')

plt.grid()

plt.show()
