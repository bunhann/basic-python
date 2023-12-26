import socket as sc
import requests

hostname = sc.gethostname()
IPAddr = sc.gethostbyname(hostname)
fqdn = sc.getfqdn()
print("\nYour computer name is: " + hostname)
print("\nYour IP Address: " + IPAddr)
print("\nYour FQDN: " + fqdn)

ip = requests.get('https://api.ipify.org').content.decode('utf8')

print('My public IP address is: {}'.format(ip))