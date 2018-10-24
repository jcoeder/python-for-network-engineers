'''
file .eapi.conf is stored in users home directory.
=====================================
cat .eapi.conf

[connection:switch1]
username: admin
password: admin
host: 172.31.33.249


[DEFAULT]
port: 443
transport: https

=====================================
'''

import pyeapi
import pprint

switch1 = pyeapi.connect_to('switch1')

#Get config as a list
conf = switch1.get_config()
#Print each item in the list as a string
for line in conf:
    print(line)

#Get config as a string
conf2 = switch1.get_config(as_string=True)
print(conf2)

version = switch1.enable('show version')
pprint.pprint(version)
dict = version[0]
result = dict ['result']
pprint.pprint (result)
print('')
pprint.pprint (result['internalVersion'])

cmds = ['vlan 234', 'name VLAN234', 'vlan 444', 'name NOTVLAN234']
switch1.config(cmds)
vlans = switch1.enable('show vlan')
pprint.pprint(vlans)

'''
cmds = ['no vlan 234', 'no vlan 444']
switch1.config(cmds)
vlans = switch1.enable('show vlan')
pprint.pprint(vlans)
'''
save = switch1.enable('write memory')
pprint.pprint(save)
