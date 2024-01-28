from ipaddress import *
a=ip_network("192.168.32.48/255.255.255.240",False)
count=0
for i in a:
    c=bin(int(i))[2:]
    print(c,a)
    if c.count("1")%2!=0:
        count+=1
print(count)
