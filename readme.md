# MikroTik IP Importer Scripts

This repository contains Python scripts for importing IP addresses into MikroTik routers. The scripts handle IP addresses from two sources:

1. **Google IP Address Ranges**
2. **IP Address Ranges for Tajikistan** (using IP2Location.com)

Both scripts generate MikroTik CLI commands to update address lists on a MikroTik router.

## Overview

### Google IP Importer Script

This script downloads Google IP address ranges, processes the data, and generates MikroTik CLI commands to add these IP addresses to an address list.

### Tajikistan IP Importer Script

This script downloads a ZIP file from IP2Location.com containing IP address data, extracts and processes it to generate MikroTik CLI commands for adding IP addresses from Tajikistan to an address list.

## Prerequisites

- Python 3.x
- Required Python libraries: `requests`, `pandas`, `ipaddress`

You can install the necessary libraries using pip:

```sh
pip install requests pandas
```

## Script Usage

1. Save the Script:
Save the script as mikrotik_google_ip_importer.py.

2. Run the Script:
Execute the script using Python:
```sh
python mikrotik_google_ip_importer.py
```
3. Check Output:
The script will print MikroTik CLI commands for adding Google IP ranges to the specified address list.

### Example Output
```sh
/ip firewall address-list remove [find list=goog_list]
/ip firewall address-list add list=goog_list address=8.8.8.0/24
/ip firewall address-list add list=goog_list address=8.8.4.0/24
```
and for TJ ip's:
```sh
/ip firewall address-list remove [find list=tj_list]
/ip firewall address-list add list=tj_list address=1.1.1.0/24
/ip firewall address-list add list=tj_list address=2.2.2.0/24
```

## Configuration
For both scripts, modify the following constants as needed:

- zip_url or URL for Google IP list.
- csv_file_name for the CSV file inside the ZIP (Tajikistan script only).
- address_list_name: The name of the MikroTik address list to update.
- country_code: For Tajikistan, specify the country code (e.g., "TJ").

### Notes
Ensure that the data structure and column names in the CSV or JSON files match those expected by the scripts.
For CIDR conversion, the scripts assume IP addresses and ranges are properly formatted and can be converted into MikroTik-compatible CIDR blocks.
