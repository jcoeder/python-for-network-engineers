'''
7. Use Netmiko to change the logging buffer size
(logging buffered <size>) on pynet-rtr2.
'''

from netmiko import ConnectHandler

router1 = {'device_type': 'cisco_ios','ip': '172.31.33.250','username': 'admin','password': 'admin',}

rtr = ConnectHandler(**router1)

output = rtr.send_config_set('logging buffered 11666')
print(output)
