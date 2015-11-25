#!/usr/bin/python
__author__ = 'eb'

# network layout
#  h1--                     -- h3
#     |                    |
#     | --- s1 ==== s2 --- |
#     |                    |
#  h2--                     -- h4

from mininet.topo import Topo
from mininet.net import Mininet
from mininet.util import dumpNodeConnections
from mininet.link import TCLink
from mininet.node import Controller

class TestTopo (Topo):
    "Two switches, each connected to two hosts"
    def __init__(self, switches=2, hosts=2, **opts):
        Topo.__init__(self, **opts)
        hostCount = 1
        totalSwitches = []
        # Add switch
        for switch in range(switches):
            newSwitch = self.addSwitch('s%s' % (switch+1))
            totalSwitches.insert(switch, newSwitch)
            # Add Hosts to switch
            for host in range(hosts):
                host = self.addHost('h%s' % (hostCount))
                hostCount+=1
                self.addLink(host, newSwitch, bw=100, delay='1ms')
        # Connect switches with each other
        for sw in range(switches - 1):
            # every link has 1ms delay 
            self.addLink (totalSwitches[sw], totalSwitches[sw+1], bw=1000, delay='1ms')


def testing():
    "Create network and run simple performance"
    topology = TestTopo(sw=2, hosts=2)
    net = Mininet(topo=topology, link=TCLink)
    net.start()
    print "Dumping host connections"
    dumpNodeConnections(net.hosts)
    net.pingAll()
    # get hosts from net
    h1, h4 = net.get('h1', 'h4')
    
    # Testing bandwidth
    #print "Testing bandwidth between h1 and h4"
    #net.iperf((h1, h4))
    
    # Testing ping
    print "Testing ping from h1 to h4"
    h1.cmd('ping -c50 %s' % (h4.IP()))
    net.stop()

if __name__ == '__main__':
    testing()
