
#!/usr/bin/env python3

import requests
import socket

def check_localhost():
    localhost = socket.gethostbyname('localhost')
    return str(localhost) == '127.0.0.1'

def check_connectivity():
    request = requests.get("https://www.google.com")
    code = request.status_code
    return code == 200

