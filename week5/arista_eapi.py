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
print(remote_connect)

response = remote_connect.runCmds(1, ['show version'])
response2 = remote_connect.runCmds(1, ['show arp', 'show ip route'])

#pprint.pprint(response)
#pprint.pprint(response2)

'''
Response is a list with a single object.  This object is a dictionary.
We are pulling the dictionary out of the list
'''
dictionary_repsonse = response[0]
dictionary_repsonse2 = response2[0]


#print(dictionary_repsonse.keys())
#print(dictionary_repsonse2.keys())

systemMacAddress = dictionary_repsonse['systemMacAddress']
print(systemMacAddress)

totalEntries = dictionary_repsonse2['totalEntries']
print(totalEntries)
