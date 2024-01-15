# from ipaddress import *
# a=set()
# for i in range(256):
#     net=ip_network(f"126.255.{i}.100/255.255.240.0",False)
#     for i in net:
#         s=bin(int(i))[2:]
#         if s[:-16].count("1")<s[-16:].count("1"):
#             break
#     else:
#         a.add(i)
#         print(i)
# print(len(a))
for i in range(2,13):
    count=0
    for d in range(2,int(i**0.5)+1):
        if i%d==0:
            count+=2
    if i**0.5%1==0:
        count-=1
    print(i,count)