#!/usr/bin/python

import pexpect
import sys


def main():
    ip_addr = '172.31.33.80'
    username = 'admin'
    password = 'admin'
    port = 22

    #Start SSH connection
    ssh_conn = pexpect.spawn('ssh -l {} {} -p {}'.format(username, ip_addr, port))
    #Log stuff to stdout
    ssh_conn.logfile = sys.stdout
    #Set SSH timeout
    ssh_conn.timout = 3

    ssh_conn.expect('ssword:')
    ssh_conn.sendline(password)

    ssh_conn.expect('#')
    print (ssh_conn.before)

    def send_command(cmd, expect):
        ssh_conn.sendline(cmd)
        ssh_conn.expect('router#')

    send_command('terminal length 0', 'router#')
    print ('')
    send_command('show ip interface brief', 'router#')
    print ('')
    send_command('show version', 'router#')

    try:
        ssh_conn.sendline('show version')
        ssh_conn.expect('WILL NOT SHOW UP')        
    except pexpect.TIMEOUT:
        print 'Found timeout'

if __name__ == "__main__":
    main()