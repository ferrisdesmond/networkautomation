#!/usr/bin/env python3


import sys
from netmiko import ConnectHandler

setup = { "device_type" : "cisco_ios",
        "ip": str(sys.argv[1]),
        "username" : "admin",
        "password" : "cisco",
        }
try:
        connection = ConnectHandler(**setup)
        conf_cmds = ['configure terminal', \
                    'interface gi1/0', \
                    'description \".. netmiko setup ..\"']
        output = connection.send_config_set(conf_cmds)
        print(output)
        connection.disconnect()



except Exception as err:
        print(f'[-] {err}')

finally:
	    connection.disconnect()
