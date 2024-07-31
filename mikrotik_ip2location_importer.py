import requests
import zipfile
import io
import pandas as pd
import ipaddress

# Constants
zip_url = "https://download.ip2location.com/lite/IP2LOCATION-LITE-DB1.CSV.ZIP"
csv_file_name = "IP2LOCATION-LITE-DB1.CSV"
address_list_name = "tj_list"
country_code = "TJ"  # Country code for Tajikistan

# Step 1: Download the ZIP file
response = requests.get(zip_url)
with zipfile.ZipFile(io.BytesIO(response.content)) as z:
    # Extract the CSV file from the ZIP
    with z.open(csv_file_name) as csv_file:
        # Step 2: Read the CSV into a DataFrame with manual headers
        df = pd.read_csv(csv_file, header=None, names=['IPFrom', 'IPTo', 'CountryCode', 'Country'])

# Step 3: Filter for addresses belonging to the specified country code
tj_addresses = df[df['CountryCode'] == country_code]

# Function to calculate CIDR notation from IP range
def ip_range_to_cidr(start_ip, end_ip):
    start = ipaddress.IPv4Address(int(start_ip))
    end = ipaddress.IPv4Address(int(end_ip))
    return ipaddress.summarize_address_range(start, end)

# Generate MikroTik CLI commands
commands = [
    f'/ip firewall address-list remove [find list={address_list_name}]'
] + [
    f'/ip firewall address-list add list={address_list_name} address={cidr}'
    for index, row in tj_addresses.iterrows()
    for cidr in ip_range_to_cidr(row['IPFrom'], row['IPTo'])
]

# Print the CLI commands
for command in commands:
    print(command)
