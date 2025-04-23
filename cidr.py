from ipwhois import IPWhois
import socket

domain = "newegg.ca"
ip = socket.gethostbyname(domain)

obj = IPWhois(ip)
res = obj.lookup_rdap()

print(f"IP: {ip}")
print(f"Network Range: {res['network']['cidr']}")
