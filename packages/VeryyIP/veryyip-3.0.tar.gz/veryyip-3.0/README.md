# VeryyIP

**VeryyIP** is a Python library for handling IP addresses (local and public). It can detect your operating system and run OS-specific commands to manage IP addresses, DNS, and more.

## Features

- Get local and public IP addresses
- Set and change IP configuration (OS-specific)
- Manage DNS settings

## Installation

Install via pip:

```bash
pip install VeryyIP
-----------------------------

Usage Example
python
Copy
Edit
from veryyip import VeryyIP

ip = VeryyIP()

# Get local IP address
print(ip.get('private'))

# Get public IP address
print(ip.get('public'))

-----------------------------

Run Script with "python {scriptName}.py"
-----------------------------------------------
And... You are Done! 
----------------------
Thanks for using VeryyIP!
-------------------------
