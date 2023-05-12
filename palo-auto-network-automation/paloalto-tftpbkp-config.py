from netmiko import ConnectHandler
from sys import argv

# Define device parameters
device = {
    'device_type': 'paloalto_panos',
    'ip': sys.argv[1],
    'username': 'admin',
    'password': 'admin'
}

# Connect to device
net_connect = ConnectHandler(**device)

# Send command to backup configuration
command = f'save config to tftp://{}/pa_config.xml'
output = net_connect.send_command(command)
print(output)

# Disconnect from device
net_connect.disconnect()

