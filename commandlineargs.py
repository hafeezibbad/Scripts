#! /usr/bin/python
"""
This script creates a json file for configuration of securebox.
"""
import json
import sys
import getopt
from uuid import getnode as get_mac
from os.path import expanduser

def generate_configuration(username, password):
    """
    This function generates a configuration for the securebox to be used.
    :return:
    """
    return {
        "name": 'sbox1',
        'mac-address':
            ':'.join(("%012x" % get_mac())[i:i+2] for i in range(0, 12, 2)),
        "username": username,
        # TODO: password should be stored as hash
        "password": password,
        "baseaddress": 'http://127.0.0.1:5000/',
        "policyFileName": expanduser('~')+'/policies.json',
    }

if __name__ == '__main__':
    # get options
    username = ''
    password = ''
    try:
        opts, args = getopt.getopt(sys.argv[1:],
                                   "hu:p:",
                                   ["username=", "password="])
    except getopt.GetoptError:
        print 'generate_configuration.py -user <username> -pass <password>'
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print 'generate_configuration.py -user <username> -pass <password>'
            sys.exit()
        elif opt in ("-u", "--username"):
            username = arg
        elif opt in ("-p", "--password"):
            password = arg

    if not username or not password:
        print 'generate_configuration.py -user <username> -pass <password>'
        sys.exit(2)

    # generate configuration
    conf = generate_configuration(username, password)
    # Write data to file
    configfile = open(expanduser('~')+'/configuration.json', 'w')
    configfile.write(json.dumps(conf, indent=4, sort_keys=True))
    configfile.close()
