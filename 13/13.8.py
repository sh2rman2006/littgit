from ipaddress import *
net = ip_network("99.64.0.0/255.192.0.0",False)
count=0
for i in net :
    ln=bin(int(i))[2:]
    if ln[-2:]=="11":
        count+=1
print(count)

