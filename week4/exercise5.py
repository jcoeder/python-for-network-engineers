'''
5. Use Netmiko to enter into configuration mode on router1.
Also use Netmiko to verify your state (i.e. that you are currently
in configuration mode).


'''

from netmiko import ConnectHandler

router1 = {'device_type': 'cisco_ios','ip': '172.31.33.250','username': 'admin','password': 'admin',}

router1_rtr = ConnectHandler(**router1)

router1_rtr.config_mode()

if router1_rtr.check_config_mode() == True:
    print('You are in configuraiton mode')
else:
    print('You are not in configuration mode')
