from ipaddress import  *
for i in range(32):
    a=ip_network(f"224.128.114.142/{i}",False)
    if str(a.network_address)=="224.128.64.0":
        print(IPv4Address(int("1"*i+"0"*(32-i),2)))