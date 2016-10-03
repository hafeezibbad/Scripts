#! /usr/bin/python

import random
import time
import sys
import getopt


# Test script for monty hall.
def montyhall(n):
    # make doors
    doors = [i for i in range(1, n+1)]
    # put car in one door
    car = random.choice(doors)
    # put goat in rest of the doors
    goats = [i for i in range(1, n+1)]
    goats.remove(car)
    # make first choice
    choice1 = random.choice(doors)
    # Open n-2 doors which do not have a car
    if choice1 == car:
        unopen = random.choice(goats)
    else:
        unopen = car
    # unopened_doors = [choice1, unopen]
    # shift your choice
    choice2 = unopen
    # print "Choice 1: ", choice1, " Unopened Doors: ", unopened_doors, \
    #     " choice2: ", choice2, "Correct choice: ", car
    if choice2 == car:
        return 1
    else:
        return 0


def main(argv):
    try:
        opts, args = getopt.getopt(argv, "hi:d:", ["iter=", "door="])
    except getopt.GetoptError:
        print "Trouble in getting arguments"
        sys.exit(2)
    try:
        iterations = -1
        door_count = -1
        results = []
        for opt, arg in opts:
            if opt == '-h':
                print "montyhall.py -i <iteration count> -d <no. of doors>"
                sys.exit()
            elif opt in ("-i", "--iter"):
                iterations = int(arg)
            elif opt in ("-d", "--door"):
                door_count = int(arg)

        random.seed(time.time())
        for _ in range(iterations):
            results.append(montyhall(door_count))
        print "Success %", (sum(results) / (len(results) + 0.0)) * 100
    except ValueError:
        print "Error: Please provide integer values as arguments"
        sys.exit(2)

if __name__ == '__main__':
    main(sys.argv[1:])
