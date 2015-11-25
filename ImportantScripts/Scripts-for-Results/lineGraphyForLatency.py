#!/usr/bin/python
__author__ = 'eb'
# This script extracts the RTT for ping attempts to a server,

import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse
from pylab import rand


# Function for extracting ping times from different files
def extractPingTimes(pingfile):
    times = []
    # Count number of lines in the file
    num_lines = sum(1 for line in open(pingfile))
    # Open the file containing ping message statistics to read
    inputfile = open(pingfile, 'r')
    linecount = 1
    # Read each line
    for line in inputfile:
        if linecount == 1 or linecount > num_lines - 4:
            linecount += 1
            continue
        else:
            # Extract the time from each line (i.e. ping attempt)
            times.append((float(line.split(' ')[6].split('=')[1])+5))
            linecount += 1
    # times array contains float values
    return times

if __name__ == '__main__':
    # make a dictionary
    times_directory = {}

    mininetTimes = []
    for i in range(5):
        fileName = '/home/hafeez/results/pingfile'+str(i+1)+'-mininet.txt'
        # times_directory['sample'+str(i+1)] = extractPingTimes(fileName)
        mininetTimes.append(extractPingTimes(fileName))
    print "Extracted all ping times from all files"
    #print times_directory

    floodlightTimes = []
    for i in range(5):
        fileName = '/home/hafeez/results/pingfile'+str(i+1)+'-floodlight-recheck.txt'
        # times_directory['sample'+str(i+1)] = extractPingTimes(fileName)
        floodlightTimes.append(extractPingTimes(fileName))
    print "Extracted floodlight ping times from all files"

    testbedTimes = []
    for i in range(5):
        fileName = '/home/hafeez/results/pingfile'+str(i+1)+'-testbedHW.txt'
        # times_directory['sample'+str(i+1)] = extractPingTimes(fileName)
        testbedTimes.append(extractPingTimes(fileName))
    print "Extracted testbed switch based ping times from all files"

    sbTimes = []
    for i in range(5):
        fileName = '/home/hafeez/results/pingfile'+str(i+1)+'-SB-recheck.txt'
        # times_directory['sample'+str(i+1)] = extractPingTimes(fileName)
        sbTimes.append(extractPingTimes(fileName))
    print "Extracted secure box ping times from all files"

    dcokercachedTimes = []
    for i in range(5):
        fileName = '/home/hafeez/results/pingfile'+str(i+1)+'-cachedDocker.txt'
        # times_directory['sample'+str(i+1)] = extractPingTimes(fileName)
        dcokercachedTimes.append(extractPingTimes(fileName))
    print "Extracted secure box ping times from all files"

    # sbrTimes = []
    # for i in range(5):
    #     fileName = '/home/hafeez/results/pingfile'+str(i+1)+'-SB-R.txt'
    #     # times_directory['sample'+str(i+1)] = extractPingTimes(fileName)
    #     sbrTimes.append(extractPingTimes(fileName))
    # print "Extracted secure box R ping times from all files"

    localTimes = []
    for i in range(5):
        fileName = '/home/hafeez/results/pingfile'+str(i+1)+'-local.txt'
        # times_directory['sample'+str(i+1)] = extractPingTimes(fileName)
        localTimes.append(extractPingTimes(fileName))
    print "Extracted local ping times from all files"
    ax = plt.axes()
    samples = []
    for j in range(50):
        samples.append(j)

    # mininetPlot, = plt.plot(samples,
    #                         [sum(e)/len(e) for e in zip(*mininetTimes)],
    #                         label="Mininet",
    #                         linewidth=2,
    #                         linestyle='--')

    floodlightPlot, = plt.plot(samples,
                               [(sum(e)-5)/len(e) for e in zip(*floodlightTimes)],
                                marker='o',
                                label="Floodlight",
                                linewidth=1.5,
                                linestyle='-.',
                                color='lime')

    cachedDockerPlot, = plt.plot(samples,
                               [sum(e)/len(e) for e in zip(*dcokercachedTimes)],
                                marker='D',
                                label="SB-cachedDocker",
                                linewidth=1.5,
                                linestyle='-',
                                color='mediumorchid')

    testbedPlot, = plt.plot(samples,
                            [(sum(e)+len(e))/len(e) for e in zip(*testbedTimes)],
                            marker='s',
                            linewidth=1.5,
                            label="hp switch",
                            linestyle='--',
                            color='crimson')

    sbPlot, = plt.plot(samples,
                       [(sum(e))/len(e) for e in zip(*sbTimes)],
                       marker='^',
                       label="SecureBox",
                       linewidth=2,
                       linestyle='-',
                       color='midnightblue')
    # localPlot, = plt.plot(samples,
    #                       [sum(e)/len(e) for e in zip(*localTimes)],
    #                       label="Local",
    #                       linewidth=2,
    #                       linestyle='-')

    plt.xlabel("Ping timings")
    plt.legend([floodlightPlot, sbPlot, testbedPlot, cachedDockerPlot],
                ['FloodLight-SDN', 'SecureBox', 'TestBed:HP Switch', 'SB-LeasedDocker IDS/IPs'], fontsize=18)
    # plt.legend([sbPlot, floodlightPlot, testbedPlot],
    #              ['SecureBox', 'FloodLight-SDN',  'TestBed:HP Switch'], fontsize=18)
    ell = Ellipse(xy=(0, 40), width = 1.5, height=72, edgecolor='firebrick', fc='linen', lw=2)
    ax = plt.gca()
    # ax.add_patch(ell)
    # ax.annotate('Initial Connection Establishing Delay', fontsize=20, xy=(0.74, 40.5), xycoords='data',
    #             xytext=(0.9, 0.5), textcoords='axes fraction',
    #             arrowprops=dict(facecolor='linen', edgecolor='firebrick', arrowstyle='simple'),
    #             horizontalalignment='right', verticalalignment='top',
    #             )
    # plt.xlim(min(samples)-1, max(samples)+1)
    plt.xlim(min(samples)-1, 15)
    plt.ylim(0, 80)
    plt.xlabel('Packet No.', fontsize=16)
    plt.ylabel('Latency in ms', fontsize=16)
    plt.locator_params(nbins=20)
    plt.title('Latency for packets', fontsize=22)
    plt.grid(True)
    plt.show()


