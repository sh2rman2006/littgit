from ipaddress import *
for i in range(1,9):
    c=int('1'*i+'0'*(8-i),2)
    a=ip_network(f"199.59.129.3/255.255.{c}.0",False)
    for i in a:
        s=bin(int(i))[2:]
        if (s[:-16].count("1")>=s[-16:].count("1"))==False:
            break
    else:
        print(c)
