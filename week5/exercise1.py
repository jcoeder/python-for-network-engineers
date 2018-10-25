'''
1. Use Arista's eAPI to obtain 'show interfaces' from the switch. Parse the 'show interfaces' output to obtain the 'inOctets' and 'outOctets' fields for each of the interfaces on the switch.  Accomplish this using Arista's pyeapi.
'''

import jsonrpclib
import ssl
import pprint
import six

ssl._create_default_https_context = ssl._create_unverified_context

ip = '172.31.33.249'
port = '443'
username = 'admin'
password = 'admin'

switch_url = 'https://{}:{}@{}:{}'.format(username, password, ip, port)
switch_url = switch_url + '/command-api'
#print(switch_url)

remote_connect = jsonrpclib.Server(switch_url)
#print(remote_connect)

interfaces = remote_connect.runCmds(1, ['show interfaces'])

# Strip off unneeded dictionary
interfaces = interfaces[0]
interfaces = interfaces['interfaces']

for interface in interfaces.keys():
    print('')
    print('Interface: ' + interface)
    inOctets = interfaces[interface]['interfaceCounters']['inOctets']
    print('inOctets: ' + str(inOctets))
    outOctets = interfaces[interface]['interfaceCounters']['outOctets']
    print('outOctets: ' + str(outOctets))
