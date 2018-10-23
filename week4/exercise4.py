import pexpect
import sys
import re
import time

ip_addr = '172.31.33.250'
username = 'admin'
password = 'admin'
port = 22
hostname = 'router1'

#Start SSH connection
ssh_conn = pexpect.spawn('ssh -l {} {} -p {}'.format(username, ip_addr, port))

#Set SSH timeout
ssh_conn.timeout = 5

ssh_conn.expect('ssword:')
ssh_conn.sendline(password)
ssh_conn.expect(hostname + '#')

#Log stuff to stdout
#ssh_conn.logfile = sys.stdout

def send_command(cmd, expect):
    '''
    Sends command and if the expect is not found
    print PyExpect has timed out.
    '''
    try:
        ssh_conn.sendline(cmd + '\n')
        ssh_conn.expect(expect)
        time.sleep(3)
    except pexpect.TIMEOUT:
        print ('PyExpect has timed out')

send_command('terminal length 0', '#')
send_command('configure  terminal', '#')
#send_command('logging buffered 9999', '#')
#send_command('exit', '#')
send_command('show running-config | section logging', '#')
print('\n>>>>')
print(ssh_conn.before.decode('utf-8', 'ignore'))
print('>>>>\n')
