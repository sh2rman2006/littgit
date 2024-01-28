from ipaddress import *
for mask in range(32):
    net=ip_network(f'20.24.110.42/{mask}',False)
    if str(net.network_address)=="20.24.96.0":
        print(mask)