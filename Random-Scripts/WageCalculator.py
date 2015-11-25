#!/usr/bin/python
try:
    hours = int(input("Please enter the number of hours: "))
    rate = float(input("Please enter the wage rate: "))
    if (hours<=40):
        print "Total pay is ", (hours*rate)
    else:
        print "Total Pay is ", ((40*rate)+((hours-40)*(rate+5)))
except:
    print "Please give meaningful inputs"

