#!/usr/bin/env python3

from netmiko import ConnectHandler
import sys

rtrs = {
	"device_type": "cisco_ios",
	"ip": str(sys.argv[1]),
	"username" : "admin",
	"password" : "cisco",
}


devconn = ConnectHandler(**rtrs)
com_output = devconn.send_command(sys.argv[2])
print(com_output)

devconn.disconnect()


