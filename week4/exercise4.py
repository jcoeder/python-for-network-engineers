'''
4. Use Pexpect to change the logging buffer size (logging buffered <size>)
on pynet-rtr2. Verify this change by examining the output of 'show run'.
'''

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
        print('SENDING  "' + cmd + '"')
        ssh_conn.sendline(cmd)
        ssh_conn.expect(expect)
        time.sleep(5)
        print(ssh_conn.before.decode('utf-8', 'ignore') + ssh_conn.after.decode('utf-8', 'ignore'))
    except pexpect.TIMEOUT:
        print ('PyExpect has timed out')

send_command('terminal length 0', '#')
send_command('configure  terminal', '#')
send_command('logging buffered 7777', '#')
send_command('exit', '#')
send_command('show running-config | section logging', '#')

