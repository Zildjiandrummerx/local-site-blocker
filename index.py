import time
import os 
import platform
from datetime import datetime as dt
from sys import platform as _platform

PATH_FOR_PLATFORM = {
    "linux": "/etc/hosts", 
    "darwin": "/etc/hosts",
    "win32": r"C:\Windows\System32\drivers\etc\hosts"
}

# Host Files PATH:
# windows_path = r"C:\Windows\System32\drivers\etc\hosts"
# unix_path = "/etc/hosts"
temp_path = PATH_FOR_PLATFORM[_platform]

redirect = "127.0.0.1"

sitesList = [
    "www.facebook.com",
    "www.twitter.com",
    "www.reddit.com",
    "www.netflix.com",
    "www.youtube.com"
]

from_hour = 7
to_hour = 16

while True:
    if dt(dt.now().year, dt.now().month, dt.now().day, from_hour) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, to_hour):
        print("Firewall is ON")
        with open(temp_path, 'r+') as file:
            content = file.read()
            for site in sitesList:
                if site in content:
                    pass
                else:
                    file.write(redirect + " " + site + "\n")
    else:
        print("Firewall is OFF")
        with open(temp_path, 'r+') as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(site in line for site in sitesList):
                    file.write(line)
            file.truncate()
    time.sleep(1)