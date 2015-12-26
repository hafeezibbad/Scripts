"""
Convert Dot separated IP address to Integer
"""
ip2int = lambda ip: reduce(lambda a,b: (a << 8) + b, map(int, ip.split('.')), 0)
int2ip = lambda n: '.'.join([str(n >> (i << 3) & 0xFF) for i in range(0, 4)[::-1]])

print ip2int('255.255.255.255')
print int2ip(ip2int('255.255.255.255'))

##########################################################################################
import socket, struct
def ip2int(ipAddr):
    """
    This function converts IP address from dotted decimal notation <string> to integer form.
    :param Dot separated IP address 127.0.0.1
    :return: Intger form of IP address e.g. 213076433
    """
    return struct.unpack('>L',socket.inet_aton(ipAddr))[0]

def int2ip(intIP):
    """
    This function converts IP address from integer form to dotted decimal notation <string>.
    :param Intger form of IP address e.g. 213076433
    :return: Dot separated IP address 127.0.0.1
    """
    return socket.inet_ntoa(struct.pack('>L',intIP))

print ip2int('0.0.0.0')
print int2ip(ip2int('0.0.0.0'))
##########################################################################################
