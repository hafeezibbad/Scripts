#!/usr/bin/python

# network layout
#  h1--                     -- h3
#     |                    |
#     | --- s1 ==== s2 --- |
#     |                    |
#  h2--                     -- h4

from mininet.topo import Topo
from mininet.net import Mininet
#from mininet.node import setLogLevel
from mininet.util import dumpNodeConnections
from mininet.link import TCLink, Intf
from mininet.node import Controller, RemoteController, OVSController
from mininet.net import OVSKernelSwitch

class TestTopo (Topo):
    "Two switches, each connected to two hosts"
    def __init__(self, switches=2, hosts=2, **opts):
        Topo.__init__(self, **opts)
        totalSwitches = []
        for switch in range(switches):
            newSwitch = self.addSwitch('s%s' % (switch+1))
            totalSwitches.insert(switch, newSwitch)
            for host in range(hosts):
                host = self.addHost('h%s' % (host+1))
                self.addLink(host, newSwitch, bw=100, delay='1ms')

def testing():
    "Create network and run simple performance"
    topology = TestTopo(sw=3, hosts=4)
    controllerIP='127.0.0.1'
    controllerPort=6653
    net = Mininet(topo=topology,
                  link=TCLink,
                  controller=lambda name: RemoteController('c0', controllerIP, controllerPort),
                  autoSetMacs=True,
                  cleanup=True)
    net.start()
    print "Dumping host connections"
    dumpNodeConnections(net.hosts)
    net.pingAll()
    print "Testing bandwidth between h1 and h4"
    h1, h4 = net.get('h1', 'h4')
    net.iperf((h1, h4))
    net.stop()

if __name__ == '__main__':
    #setLogLevel('info')
    testing()
