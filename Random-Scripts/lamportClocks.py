# __author__ = 'eb'
#Submitted by:
#***** ******
#student Number:*********
#**************@helsinki.fi

#import required modules
import sys
import socket
import thread
import time
import random

#get local variables
config_file=sys.argv[1]
local_node_id=sys.argv[2]
local_hostname=''
local_port=-1
local_clock=0

neighbors=0
total_events=0

#lists from the configuration files
node_hostname=[]
node_id=[]
node_port=[]

#read the configuration file
def readConfiguration (config_file,local_node_id):
    #import global variables in local scope
    global local_hostname
    global local_port
    global neighbors
    #open file
    conf_file_obj=open(config_file,'r')
    #traverse all data
    for eachLine in conf_file_obj:
        line_info=eachLine.split(' ') #tokenize each line based on the space
        #if information is about local host using refernce id given in argument
        if line_info[0]== local_node_id:
            local_hostname=line_info[1]
            local_port=int (line_info[2])
        else:
            node_id.append(line_info[0])
            node_hostname.append(line_info[1])
            node_port.append(int(line_info[2]))
            neighbors+=1
    conf_file_obj.close()

def clockUpdate(incomingClockVal):
    global local_clock
    #choose the maximum clock value and increment that for reception of message
    local_clock=max(incomingClockVal,local_clock)+1

def listening(port_num):
    global neighbors
    global local_clock
    local_sock=socket.socket() #standard TCP socket from AF_INET family
    hostname=socket.gethostname()
    local_sock.bind((hostname,port_num))
    local_sock.listen(neighbors)

    while 1:
        connObj,addr=local_sock.accept()
        #print "got a message"
        buff=connObj.recv(1024)
        clockval=int(buff)
        clockUpdate(clockval)
        #print "receive event: clock updated to: ",clockval
        print 'r ',addr,' ',clockval,' ',local_clock
        #print 'r ',addr[0],' ',clockval,' ',local_clock
        connObj.close()

def sendMessage(dst_host,dst_port,clockVal):
    global  local_clock
    #print "i am sending now one ", dst_host, dst_port, clockVal
    sock=socket.socket() #standard TCP socket from AF_INET family
    sock.connect((dst_host,dst_port))
    msg=clockVal
    sock.send(str(msg))
    #print "sent clock: ",msg
    sock.close()

def main ():
    global total_events
    global local_clock
    while local_clock<100: #process 100 events
        flipCoin=random.random()
        #do a local event
        if flipCoin <0.5:
            local_event=random.randint(1,5) #generate random event
            local_clock+=local_event
            print 'l ',local_event
        #send a message
        else:
            random_index=random.randint(0,neighbors-1)
            local_clock+=1
            #use fully qualified names
            sendMessage(node_hostname[random_index]+'.cs.helsinki.fi',node_port[random_index],local_clock)
            #use only ukkoxxx names
            #sendMessage(node_hostname[random_index][0:6]+'.cs.helsinki.fi',node_port[random_index],local_clock)
            print 's ',node_id[random_index][0:6],' ',local_clock

readConfiguration(config_file,local_node_id)
#start the listening in a new thread to make sure it doesnt block local events
thread.start_new_thread(listening,(local_port,))
#wait for all nodes to spawn
time.sleep(10)
#sendMessage(node_hostname,node_port,2)
#run the main function where events are done
main()
# for graceful execution, execute any pending messages
time.sleep(10)
#Bye
print "Bye"
