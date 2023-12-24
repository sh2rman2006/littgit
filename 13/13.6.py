from ipaddress import *
for mask in range(32):
    d=ip_network(f"227.138.127.144/{mask}",False)
    if str(d.network_address)=="227.138.64.0":
        print(IPv4Address(int("1"*mask+"0"*(32-mask),2)))