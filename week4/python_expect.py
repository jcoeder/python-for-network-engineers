#!/usr/bin/python

import pexpect
import sys
import re

def main():
    ip_addr = '172.31.33.81'
    username = 'admin'
    password = 'admin'
    port = 22

    #Start SSH connection
    ssh_conn = pexpect.spawn('ssh -l {} {} -p {}'.format(username, ip_addr, port))
    #Log stuff to stdout
    ssh_conn.logfile = sys.stdout
    #Set SSH timeout
    ssh_conn.timeout = 3

    ssh_conn.expect('ssword:')
    ssh_conn.sendline(password)

    ssh_conn.expect('router#')
    #print (ssh_conn.before)

    def send_command(cmd, expect):
        '''
       Sends command and if the expect is not found
       print PyExpect has timed out.
       '''
        try:
            ssh_conn.sendline(cmd + '\n')
            ssh_conn.expect(expect)
            #print(ssh_conn.before)
            #print(ssh_conn.after)
        except pexpect.TIMEOUT:
            print ('PyExpect has timed out')

    send_command('terminal length 0', 'router#')
    #send_command('show ip interface brief', 'router#')
    #send_command('show version', 'router#')
    #This will timeout and meet the except statement
    #send_command('show version', 'YOLO')

    #Regular Expressions should always be raw 'r' strings
    #Begins with '^' Lic
    #Any squence of 0 or more caracters endings in DI:
    #Any squence of 0 or more caracters end of the line
    #Multiline - Line by line match
    #pattern = re.compile(r'^Lic.*DI:.*$', re.MULTILINE)
    #ssh_conn.sendline('show version')
    #ssh_conn.expect(pattern)


    #Regular Expressions should always be raw 'r' strings
    #Begins with '^' ROM
    #Any squence of 0 or more caracters end of the line
    #Multiline - Line by line match
    pattern = re.compile(r'^ROM:.*$', re.MULTILINE)
    ssh_conn.sendline('show version')
    ssh_conn.expect(pattern)
    print (ssh_conn.readline())

if __name__ == "__main__":
    main()