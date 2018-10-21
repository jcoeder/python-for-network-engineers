import pexpect
import sys
import re

ip_addr = '172.31.33.250'
username = 'admin'
password = 'admin'
port = 22
hostname = 'router1'

#Start SSH connection
ssh_conn = pexpect.spawn('ssh -l {} {} -p {}'.format(username, ip_addr, port))

#Set SSH timeout
ssh_conn.timeout = 3

ssh_conn.expect('ssword:')
ssh_conn.sendline(password)
ssh_conn.expect('#')

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
        print(ssh_conn.before)
        #print(ssh_conn.after)
    except pexpect.TIMEOUT:
        print ('PyExpect has timed out')

send_command('show ip int brief', hostname + '#')