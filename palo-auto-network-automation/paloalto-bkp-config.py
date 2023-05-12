#!/usr/bin/env python3

from netmiko import ConnectHandler
from sys import argv

# Define device parameters
device = {
    'device_type': 'paloalto_panos',
    'ip': argv[1],
    'username': 'admin',
    'password': 'admin'
}

# Connect to device
net_connect = ConnectHandler(**device)

# Send command to backup configuration
command = 'show config running'
output = net_connect.send_command(command)

# Save output to file
with open('pa_config.xml', 'w') as f:
    f.write(output)

# Disconnect from device
net_connect.disconnect()

