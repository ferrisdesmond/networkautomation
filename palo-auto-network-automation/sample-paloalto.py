from netmiko import ConnectHandler

# Define device parameters
device = {
    'device_type': 'paloalto_panos',
    'ip': '10.0.0.1',
    'username': 'admin',
    'password': 'password'
}

# Connect to device
net_connect = ConnectHandler(**device)

# Configure zone 1
config_commands = [    'set zone name zone1',    'set zone network layer3 network 10.1.1.0/24',    'commit']
output = net_connect.send_config_set(config_commands)
print(output)

# Configure zone 2
config_commands = [    'set zone name zone2',    'set zone network layer3 network 10.2.2.0/24',    'commit']
output = net_connect.send_config_set(config_commands)
print(output)

# Disconnect from device
net_connect.disconnect()

