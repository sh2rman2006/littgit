from ipaddress import *
a=ip_network("186.135.80.0/255.255.252.0",False)
count=0
for i in a:
    c=bin(int(i))[2:]
    if c[:-16].count("1")>c[-16:].count("1"):
        count+=1
print(count)