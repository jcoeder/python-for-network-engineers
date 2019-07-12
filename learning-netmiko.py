from netmiko import ConnectHandler

net_connect = ConnectHandler(host='iol1', username='justin', password='Lab12345!', device_type='cisco_ios')
#or
device1 = {
    'host': 'iol1',
    'username': 'justin',
    'password': 'Lab12345!',
    'device_type': 'cisco_ios',
    'session_log': '/Users/justin/Desktop/iol1.log',  # can log session to file
}

net_connect = ConnectHandler(**device1)

print(net_connect.send_command('show version'))
print(net_connect.send_command('show ip inter br', expect_string=r'#')) # can set expect vs default
