'''
6. Use Netmiko to execute 'show arp' on pynet-rtr1, pynet-rtr2, and juniper-srx.
'''

from netmiko import ConnectHandler
import time

router1 = {'device_type': 'cisco_ios','ip': '172.31.33.250','username': 'admin','password': 'admin',}
router2 = {'device_type': 'juniper','ip': '172.31.33.248','username': 'admin','password': 'admin123',}
router3 = {'device_type': 'arista_eos','ip': '172.31.33.249','username': 'admin','password': 'admin',}

routers = [router1, router2, router3]

for router in routers:
    #VMs are running a little hot, give them some time.
    time.sleep(5)
    #Print the dictionary used to establish the connection
    print(router)
    rtr = ConnectHandler(**router)
    #Print the established connection
    print(rtr)
    #Enter enable mode if one exists
    rtr.enable()

    #Send the command show version and print the output
    output = rtr.send_command('show version')
    print(output)

    #Send the command show version and print the output
    output = rtr.send_command('show arp')
    print(output)

    #show the current prompt
    print(rtr.find_prompt())
    #Enter config mode
    rtr.config_mode()
    #show the current prompt
    print(rtr.find_prompt())
    #Check if or if not in config mode
    print(rtr.check_config_mode())
