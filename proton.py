#Proton is a Python-coded tools
#Made by Leak#5749
#Github : leak37
import pyfiglet
from urllib import request
import json
import os
 
result = pyfiglet.figlet_format("PROTON", font = "banner3-D" ) 
print(result)

print("[+] Proton - Python-coded IP-Scanner")
print("[+] Made by Leak")
print("[+] Github : https://github.com/leak37")
print("#===============================================#")
print("[>] Type IP Adresses")

ip = input("> ")

from urllib import request
import json
import os

while True:
    url = "http://ip-api.com/json/"
    r = request.urlopen(url + ip)
    data = r.read()
    m = json.loads(data)

    print(f"""
    Status : {m['status']}
    IP : {m['query']}
    ISP : {m['isp']}
    Organization : {m['org']}
    Country : {m['country']}
    Region : {m['region']}
    City : {m['city']}
    Time Zone : {m['timezone']}
    """)