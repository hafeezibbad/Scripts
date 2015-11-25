#!/bin/bash

count="$1"
while [ $count -lt "$2" ]
do
  sudo nmap -p $count -sT $3 &
  count=$[$count+1]
done
