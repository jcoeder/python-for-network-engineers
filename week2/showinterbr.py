#!/usr/bin/env python

import telnetlib
import time

TELNET_PORT = 23
TELNET_TIMEOUT = 6

def send_command_return_output(remote_conn, cmd):
    cmd = cmd.rstrip()
    remote_conn.write(cmd + '\n')
    time.sleep(1)
    return remote_conn.read_very_eager()

def send_command_return_nothing(remote_conn, cmd):
     remote_conn.write(cmd + '\n')
     time.sleep(1)


def log_into_router_without_enable(ip_addr, username, password, TELNET_PORT, TELNET_TIMEOUT):
    remote_conn = telnetlib.Telnet(ip_addr, TELNET_PORT, TELNET_TIMEOUT)
    remote_conn.read_until('ername:', TELNET_TIMEOUT)
    remote_conn.write(username + '\n')
    remote_conn.read_until('ssword:', TELNET_TIMEOUT)
    remote_conn.write(password + '\n')
    return remote_conn
    time.sleep(1)

def main():
    ip_addr = '184.105.247.70'
    username = 'pyclass'
    password = '88newclass'

    remote_conn = log_into_router_without_enable(ip_addr, username, password, TELNET_PORT, TELNET_TIMEOUT)
    
    send_command_return_nothing(remote_conn, 'terminal length 0')
    print(send_command_return_output(remote_conn, 'show ip interface brief'))

    remote_conn.close()

if __name__ == "__main__":
    main()
