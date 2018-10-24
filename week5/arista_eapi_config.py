'''
Requires Python2. jsonrpclib has been renamed in Python3
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
#print(remote_connect)

commands = [{'cmd': 'enable', 'input': ''}, 'configure terminal', 'vlan 225', 'vlan 522', 'vlan 252', 'exit']

remote_connect.runCmds(1, commands)

respone = remote_connect.runCmds(1, ['show vlan'])

pprint.pprint(respone)
