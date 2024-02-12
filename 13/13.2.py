from ipaddress import *
for A in range(252):
    net=ip_network(f'183.192.{A}.0/255.255.252.0',False)
    for i in net:
        s=bin(int(i))[2:]
        if s[-16:].count("1")<=3:
            break
    else:
        print(A)




