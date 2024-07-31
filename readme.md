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
