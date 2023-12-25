from ipaddress import *
a=ip_network("142.108.56.118/255.255.255.240",False)
count=0
for i in a:
    c=bin(int(i))[2:]
    if c[:-16].count("1")<c[-16:].count("1"):
        count+=1
print(count)


