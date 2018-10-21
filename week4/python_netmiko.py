from netmiko import ConnectHandler

pynet1 = {'device_type': 'cisco_ios','ip': '172.31.33.81','username': 'admin','password': 'admin',}

pynet1_rtr = ConnectHandler(**pynet1)

'''
METHODS
>>> dir(pynet1_rtr)
['RESPONSE_RETURN', 'RETURN', 'TELNET_RETURN', '__class__', '__delattr__', '__dict__', '__doc__', '__enter__', '__exit__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_autodetect_fs', '_build_ssh_client', '_connect_params_dict', '_first_line_handler', '_lock_netmiko_session', '_modify_connection_params', '_read_channel', '_read_channel_expect', '_read_channel_timing', '_sanitize_output', '_session_locker', '_session_log_close', '_session_log_fin', '_test_channel_read', '_timeout_exceeded', '_try_session_preparation', '_unlock_netmiko_session', '_use_ssh_config', '_write_channel', '_write_session_log', 'allow_agent', 'allow_auto_change', 'alt_host_keys', 'alt_key_file', 'ansi_escape_codes', 'auth_timeout', 'base_prompt', 'blocking_timeout', 'check_config_mode', 'check_enable_mode', 'cleanup', 'clear_buffer', 'close_session_log', 'commit', 'config_mode', 'device_type', 'disable_paging', 'disconnect', 'enable', 'encoding', 'establish_connection', 'exit_config_mode', 'exit_enable_mode', 'fast_cli', 'find_prompt', 'global_delay_factor', 'host', 'ip', 'is_alive', 'keepalive', 'key_file', 'key_policy', 'normalize_cmd', 'normalize_linefeeds', 'open_session_log', 'paramiko_cleanup', 'passphrase', 'password', 'pkey', 'port', 'protocol', 'read_channel', 'read_until_pattern', 'read_until_prompt', 'read_until_prompt_or_pattern', 'remote_conn', 'remote_conn_pre', 'save_config', 'secret', 'select_delay_factor', 'send_command', 'send_command_expect', 'send_command_timing', 'send_config_from_file', 'send_config_set', 'serial_login', 'serial_settings', 'session_log', 'session_log_record_writes', 'session_preparation', 'session_timeout', 'set_base_prompt', 'set_terminal_width', 'special_login_handler', 'ssh_config_file', 'strip_ansi_escape_codes', 'strip_backspaces', 'strip_command', 'strip_prompt', 'system_host_keys', 'telnet_login', 'timeout', 'use_keys', 'username', 'verbose', 'write_channel']
>>> pynet1_rtr.find_prompt()
u'router#'
'''

pynet1_rtr.config_mode()
pynet1_rtr.check_config_mode()
pynet1_rtr.exit_config_mode()
pynet1_rtr.check_config_mode()


outp = pynet1_rtr.send_command('show ip interface brief')
print (outp)

outp = pynet1_rtr.send_command('show version')
print (outp)

#Make configuration changes and show that the changes have been made
config_commands = ['logging buffered 19999', 'no logging console']
output = pynet1_rtr.send_config_set(config_commands)
outp = pynet1_rtr.send_command('show run | inc logging')
print(outp)

#Show the running configuration
outp = pynet1_rtr.send_command('show running-config')
print (outp)

#Write the configuration and show that is has been saved
config_commands = ['do wr']
output = pynet1_rtr.send_config_set(config_commands)
print(output)





'''
Juniper commands:

#Shows current prompt
srx.find_prompt()

#Make configuration changes and show that the changes have been made
config_commands = ['set system hostname srx01']
output = srx.send_config_set(config_commands)
outp = pynet1_rtr.send_command('show run | match hostname')
print(outp)
'''

'''
