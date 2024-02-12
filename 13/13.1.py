from ipaddress import *
for mask in range(32):
    net=ip_network(f"224.128.112.142/{mask}",False)
    if str(net.network_address)=="224.128.64.0":
        print(IPv4Address(int("1"*mask+"0"*(32-mask),2)))




