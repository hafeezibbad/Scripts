import random
import sys
import time


fd=open('~/sequence_float.txt','w')
time_before=time.time()
for x in range(1,int(sys.argv[1])):
    mango=random.randint(1,99)+random.random()
    fd.write('{}\n'.format(mango))
    #write the last integer with no trailing new line
#mango=random.randint(1,99)+random.random()
#fd.write('{}'.format(mango))
fd.close()
time_after=time.time()
time_taken=time_after-time_before
print "Time taken in generating", sys.argv[1], "numbers: ", time_taken, " seconds"
