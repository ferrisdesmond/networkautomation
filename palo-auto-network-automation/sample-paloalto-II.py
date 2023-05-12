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

# Allow traffic between zone 1 and zone 2
config_commands = [    'set rulebase security rules allow-zone1-zone2',    'set rulebase security rules allow-zone1-zone2 to zone2',    'set rulebase security rules allow-zone1-zone2 from zone1',    'set rulebase security rules allow-zone1-zone2 source any',    'set rulebase security rules allow-zone1-zone2 destination any',    'set rulebase security rules allow-zone1-zone2 application any',    'set rulebase security rules allow-zone1-zone2 action allow',    'set rulebase security rules allow-zone1-zone2 log-start yes',    'set rulebase security rules allow-zone1-zone2 log-end yes',    'commit']
output = net_connect.send_config_set(config_commands)
print(output)

# Disconnect from device
net_connect.disconnect()

