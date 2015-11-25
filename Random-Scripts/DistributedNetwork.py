
#__author__ = 'eb'

#import packages
import sys
import socket
import thread
import time

configuration_file=sys.argv[1]
local_id=int(sys.argv[2])


#local variables
super_peer_list={}
local_peer_list={}
# by default no node is Super Node
isSuper=False
localPort=-1
localHostname=""
messagesSent=0
mySuperPeer=-1

superMod=3
class Packet:
    def __init__(self,destination,nextHop,payload):
        self.destination=destination
        self.nextHop=nextHop
        self.payload=payload


# node structure
class Node:
    """ Node class representing each node"""
    def __init__(self,hostname,port):
        self.hostname=hostname
        self.port=int(port)
    def display(self):
        print "Hostname:",self.hostname," Port:",self.port

def findSuperPeer(id):
    counter=int(id)
    while (counter%superMod!=0):
        counter+=1
    return counter

def isSuperNode(local_id):
    if (int(local_id)%superMod==0):
        return True
    else:
        return False

#make routing tables
def generateRoutingTable(configuration_file,local_id):
    global super_peer_list
    global local_peer_list
    global isSuper
    global localHostname
    global localPort
    isSuper=isSuperNode(local_id)
    if (isSuper):
        print "I am super peer with ID ", local_id
        #open the configuration file
        conf_file=open(configuration_file,'r')
        for line in conf_file:
            #tokenize the line
            line_info=line.split(' ')
            line_info[0]=int(line_info[0])
            #if information is for local peer
            if (line_info[0]==local_id):
                localPort=int(line_info[2])
                localHostname=line_info[1]
                #print "I am ",localHostname," with port ",localPort
            #save in local neighbors
            elif (line_info[0]<local_id and line_info[0]>(local_id-superMod)):
                node=Node(line_info[1],int(line_info[2]))
                local_peer_list[line_info[0]]=node
            #save in global neighbors
            elif (line_info[0]%superMod==0):
                node=Node(line_info[1],int(line_info[2]))
                super_peer_list[line_info[0]]=node
        conf_file.close()
    else:
        print "I am not a super peer"
        #find super peer
        superPeer=findSuperPeer(local_id)
        #open the configuration file
        conf_file=open(configuration_file,'r')
        #find local nodes
        for line in conf_file:
            #tokenize the string
            line_info=line.split(' ')
            line_info[0]=int(line_info[0])
            if (line_info[0]==local_id):
                localPort=int(line_info[2])
                localHostname=line_info[1]
            elif (line_info[0]<(superPeer) and line_info[0]>(superPeer-superMod)):
                #neighboring peer
                node=Node (line_info[1],int(line_info[2]))
                local_peer_list[line_info[0]]=node
            elif (isSuperNode(line_info[0])):
                #super peer
                node=Node (line_info[1],int(line_info[2]))
                super_peer_list[line_info[0]]=node
        conf_file.close()


def sendMessages(configuration_file):
    global messagesSent
    global local_id
    #open the file
    conf_file=open(configuration_file,'r')
    for line in conf_file:
        line_info=line.split(' ')
        line_info[0]=int(line_info[0])
        if (line_info[0]!=local_id):
            #send message: give only destination node ID
            #destination_node=id of destination node
            #nextHop = packet will decide
            #payload = id of node from which packet is coming
            payload=str(local_id)+","+str(line_info[0])+","+"Message from "+str(local_id)
            #print "sending message to ",line_info[0], " from sendMessages of ",local_id
            sendMessageTo(int(line_info[0]),payload)
        else:
            print "Hey got your message, its me myself :D"

    conf_file.close()


#function to keep listening messages from other nodes
def listening(portNum):
    local_sock=socket.socket()
    #get hostname for socket
    hostname=socket.gethostname()
    local_sock.bind((hostname,portNum))
    #optimistic number by can be changed
    local_sock.listen(1000)
    print "Listening on ",hostname,":",portNum
    #keep listening
    while (True):
        connObj,addr=local_sock.accept()
        buff=connObj.recv(1024)
       # print "got a connection from ",addr
        incomingMsg=str(buff)
        #tokenize the incoming string
        incoming=incomingMsg.split(",")
        #print incoming
        #incoming packet should be of order
        #Source
        #Destination
        #Payload
        #print incoming
        #if I am destination
        if (int(incoming[1])==local_id):
            print "Recieved a Message ",incoming[2]," from ",incoming[0]
        else:
            #forward the packet to destination
            print "forwarding message from ",incoming[0], " to ",incoming[1]
            forwarding(incomingMsg)
        connObj.close()

#send message to any node
def sendMessageTo(destination,payload):
    #print "I am in send Messages module"
    global local_id
    #find super peer of destination
    superPeerOfDest=findSuperPeer(destination)
    #find own super peer
    mySuperPeer=findSuperPeer(local_id)
    if (destination%superMod==0):
        #destination is some super peer
        superList=True
        #send the Message to destination
        sendMessageToDest(superList,destination,payload)
    elif(superPeerOfDest==mySuperPeer):
        #packet is in local scope
        superList=False
        #send message to destination
        sendMessageToDest(superList,destination,payload)
    else:
        #packet is in local scope of some other super peer
        superList=True
        sendMessageToDest(superList,superPeerOfDest,payload)

def forwarding(incomingMsg):
    #print "I am in forwarding module"
    #get different fields from string
    incoming=incomingMsg.split(",")
    source=int(incoming[0])
    destination=int(incoming[1])
    payload=incoming[2]
    global local_id
    #find super peer of destination
    superPeerOfDest=findSuperPeer(incoming[1])
    #messageToSend=str(incoming[0])+
    #find own super peer
    mySuperPeer=findSuperPeer(local_id)
    if (destination%superMod==0):
        #destination is some super peer
        superList=True
        #send the Message to destination
        sendMessageToDest(superList,destination,incomingMsg)
    elif(superPeerOfDest==mySuperPeer):
        #packet is in local scope
        superList=False
        #send message to destination
        sendMessageToDest(superList,destination,incomingMsg)
    else:
        #packet is in local scope of some other super peer
        superList=True
        sendMessageToDest(superList,superPeerOfDest,incomingMsg)

#Simpley send a message to destination
def sendMessageToDest(superList,nextHop,message):
    #print "I am in send message to destination module"
    global super_peer_list
    global local_peer_list
    nextHop=int(nextHop)
    hostName=""
    portNumber=-1
    if (superList):
        #check in super peer list
        #print "Next Hop:",super_peer_list[nextHop].display()
        hostName=super_peer_list[nextHop].hostname
        portNumber=super_peer_list[nextHop].port
        #print hostName,":",portNumber
    else:
        #check in local Peer list
        #print "Next Hop:",super_peer_list[nextHop].display()
        hostName=local_peer_list[nextHop].hostname
        portNumber=local_peer_list[nextHop].port
        #print hostName,":",portNumber

    #open a socket
    sock=socket.socket()
    #connect to client
    #print "connecting to ",hostName,":",portNumber
    sock.connect((hostName,portNumber))
    #print "connected to ",hostName,":",portNumber
    #send the message
    sock.send(message)
    #close the socket
    sock.close()


#generate routing tables
generateRoutingTable(configuration_file,local_id)
#for key in super_peer_list.keys():
#    print super_peer_list[key].display()

#for key in local_peer_list.keys():
#    print local_peer_list[key].display()


#start listening in separate thread
thread.start_new_thread(listening,(localPort,))
#sleep so that everybody starts
time.sleep(10)
sendMessages(configuration_file)
#generate routing tables
#generateRoutingTable(configuration_file,local_id)
#for key in super_peer_list.keys():
#    print super_peer_list[key].display()

#for key in local_peer_list.keys():
#    print local_peer_list[key].display()
time.sleep(20)
sys.exit(0)









