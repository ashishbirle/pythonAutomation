
#!/usr/bin/env python3

import requests
import socket

def check_localhost():
    localhost = socket.gethostbyname('localhost')
    return localhost

def check_connectivity():
    request = requests.get("https://www.google.com")
    return str(request)


print(check_localhost())
print(check_connectivity())