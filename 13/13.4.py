from ipaddress import *
for mask in range(32):
    a=ip_network(f'118.187.59.255/{mask}',False)
    b = ip_network(f'118.187.65.115/{mask}', False)
    if a.network_address!=b.network_address:
        print(mask)
