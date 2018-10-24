'''
1. Use Arista's eAPI to obtain 'show interfaces' from the switch. Parse the 'show interfaces' output to obtain the 'inOctets' and 'outOctets' fields for each of the interfaces on the switch.  Accomplish this using Arista's pyeapi.
'''

import jsonrpclib
import ssl
import pprint

ssl._create_default_https_context = ssl._create_unverified_context

ip = '172.31.33.249'
port = '443'
username = 'admin'
password = 'admin'

switch_url = 'https://{}:{}@{}:{}'.format(username, password, ip, port)
switch_url = switch_url + '/command-api'
print(switch_url)

remote_connect = jsonrpclib.Server(switch_url)
print(remote_connect)

response = remote_connect.runCmds(1, ['show interfaces'])

dict = response[0]
pprint.pprint(dict)

for interfaces, interface_name in dict.items():
    pprint.pprint(interface_name)
