'''
2. Use Paramiko to change the 'logging buffered <size>' configuration on
pynet-rtr2. This will require that you enter into configuration mode.
'''

import paramiko
import time

ip_addr = '172.31.33.250'
username = 'admin'
password = 'admin'
port = 22

#Act as a SSH client
remote_conn_pre = paramiko.SSHClient()

#Accept all host keys
remote_conn_pre.set_missing_host_key_policy(paramiko.AutoAddPolicy())

#Create SSH connection
remote_conn_pre.connect(ip_addr, username=username, password=password, look_for_keys=False, allow_agent=False, port=port)

#invoke shell to read from SSH channel
remote_conn = remote_conn_pre.invoke_shell()

#set timeout to 6 seconds
remote_conn.settimeout(6.0)

#check to see if there is data to receive
remote_conn.recv_ready()

#recieve up to 5000 bytes MAX is 65535
outp1 = remote_conn.recv(5000)
print(outp1)

#send commands and wait for response
remote_conn.send('terminal length 0\n')
remote_conn.send('conf t\n')
remote_conn.send('logging buffered 19999\n')
time.sleep(1)
outp = remote_conn.recv(5000)
print (outp)
