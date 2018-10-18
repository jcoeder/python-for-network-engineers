import paramiko
import time

ip_addr = '172.31.33.80'
username = 'admin'
password = 'admin'
port = 22

#Act as a SSH client
remote_conn_pre = paramiko.SSHClient()

#Blindly accept host keys
#remote_conn_pre.set_missing_host_key_policy(paramiko.AutoAddPolicy())

#Load system host keys
remote_conn_pre.load_system_host_keys()

#Create SSH connection
remote_conn_pre.connect(ip_addr, username=username, password=password, look_for_keys=False, allow_agent=False, port=port)

#invoke shell to read from SSH channel
remote_conn = remote_conn_pre.invoke_shell()

#set timeout to 6 seconds
remote_conn.settimeout(6.0)

#get and return timeout
#timeout = remote_conn.gettimeout()
#print(timeout)

#check to see if there is data to receive
remote_conn.recv_ready()

#recieve up to 5000 bytes MAX is 65535
outp1 = remote_conn.recv(5000)
print(outp1)

#send commands
sent = remote_conn.send('terminal length 0\n')
time.sleep(1)
sent = remote_conn.send('show ip interface brief\n')
time.sleep(1)
outp2 = remote_conn.recv(5000)
time.sleep(1)
print (outp2)
 