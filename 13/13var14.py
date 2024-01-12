from ipaddress import *
a=set()
for i in range(256):
    net=ip_network(f"126.255.{i}.100/255.255.240.0",False)
    for i in net:
        s=bin(int(i))[2:]
        if s[:-16].count("1")<s[-16:].count("1"):
            break
    else:
        a.add(i)
        print(i)
print(len(a))