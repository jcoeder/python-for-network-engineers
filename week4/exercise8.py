'''
8. Use Netmiko to change the logging buffer size (logging buffered <size>)
and to disable console logging (no logging console) from a file on both
pynet-rtr1 and pynet-rtr2 (see 'Errata and Other Info, item #4).
'''

from netmiko import ConnectHandler

router1 = {'device_type': 'cisco_ios','ip': '172.31.33.250','username': 'admin','password': 'admin',}

rtr = ConnectHandler(**router1)
print(rtr)

output = rtr.send_config_from_file(config_file='/Users/justin/python-for-network-engineers/week4/config.txt')
print(output)
