from ipaddress import *
count=0
net = ip_network('112.154.133.208/255.255.252.0',False)
for i in net :
    ln=bin(int(i))[2:]
    if ln[:-16].count("1") <= ln[-16:].count("0") and ln[-16:].count("0")%2!=0:
        count+=1
print(count)
