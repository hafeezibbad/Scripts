#!/bin/bash


# This script extracts the RTT for ping attempts to a server, stored in a file

#Count Number of lines in file
lines=`cat $1| wc -l`

#number of ping instances
pings=$(($lines-5))

#empty the file
truncate -s 0 times.txt

#parse each line: start from second line and ignore last 4 lines
for i in `seq 2 $(($lines-4))`;
do
	echo `sed -n ${i}p $1 | awk '{print $8;}' | awk -F'=' '{print $2;}'` >> times.txt
done
