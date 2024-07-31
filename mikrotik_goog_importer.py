import requests
import json

# URL to download the IP list
url = "https://www.gstatic.com/ipranges/goog.json"
address_list_name = "goog_list"

# Fetch the IP list file
response = requests.get(url)
data = response.json()

# Extract IPv4 prefixes
ipv4_prefixes = [prefix['ipv4Prefix'] for prefix in data['prefixes'] if 'ipv4Prefix' in prefix]

# Generate MikroTik CLI commands
commands = [
    f'/ip firewall address-list remove [find list={address_list_name}]'
] + [
    f'/ip firewall address-list add list={address_list_name} address={prefix}'
    for prefix in ipv4_prefixes
]

# Print the CLI commands
for command in commands:
    print(command)
